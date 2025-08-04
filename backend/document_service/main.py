from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from datetime import datetime
import shutil, os

from database import SessionLocal, engine
import models
from models import File_model, Document_model
from typing import Annotated

app = FastAPI(title='Document service')

UPLOAD_DIR = 'upload'
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount('/uploadfile', StaticFiles(directory=UPLOAD_DIR), name='uploadfile')

models.Base.metadata.create_all(bind=engine)

# Tipos permitidos
ALLOWED_EXTENSIONS = {'.pdf', '.doc', '.docx', '.odt', '.txt'}

# Dependencia de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post('/document/{id}/file', tags=['document service'])
async def upload_document(id: str, upload_file: UploadFile = File(...),  db: Session = Depends(get_db)):
    # Buscar si el usuario existe
    db_id_file = db.query(Document_model).filter(Document_model.dni == id).first()
    if not db_id_file:
        raise HTTPException(status_code=404, detail='Usuario no encontrado o inexistente')

    # Verificar extensión
    ext = os.path.splitext(upload_file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail='El tipo de archivo no es válido')

    try: 
        # Guardar archivo en disco
        path = os.path.join(UPLOAD_DIR, upload_file.filename)
        with open(path, 'wb') as buffer:
            shutil.copyfileobj(upload_file.file, buffer)

        # Guardar en base de datos
        db_file = File_model(
            filename=upload_file.filename,
            content_type=upload_file.content_type,
            upload_date=datetime.now(),
            file_path=path,
            owner_dni=id
        )

        db.add(db_file)
        db.commit()
        db.refresh(db_file)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'Ocurrio un error al intentar guardar el archivo: {str(e)}')

    return {
        'detail': 'Archivo subido y guardado exitosamente',
        'file_id': db_file.id,
        'filename': db_file.filename
    }

@app.get('/document/{id}', tags=['document service'])
async def get_document_by_id(id: str, db: db_dependency):
    db_document = db.query(models.Document_model).filter(models.Document_model.dni == id).first()
    if not db_document:
        raise HTTPException(status_code=404, detail='Documento no encontrado o inexistente')
    return db_document

@app.delete('/document/{id}', tags=['document service'])
async def delete_document_by_id(id: str, db: db_dependency):
    db_document = db.query(models.Document_model).filter(models.Document_model.dni == id).first()
    if not db_document:
        raise HTTPException(status_code=404, detail='Documento no encontrado o inexistente')
    try:
        db.delete(db_document)
        db.commit()
        return {'detail':'Registro eliminado con éxito'}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f'Ocurrio un error intentando eliminar el documneto: {str(e)}')    