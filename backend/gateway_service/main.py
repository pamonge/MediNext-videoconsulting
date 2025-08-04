from fastapi import FastAPI, Request, HTTPException
import httpx

app = FastAPI(
    title='Gateway'
)

MICROSERVICES = {
    'user': 'http://user_service:8000',
    'profile': 'http://profile_service:8000',
    'plan': 'http://plan_service:8000',
    'payment': 'http://payment_service:8000',
    'med_hist': 'http://medical_history_service:8000',
    'document': 'http://document_service:8000',
    'authorization': 'http://authorization_service:8000',
    'affiliation': 'http://afiliation_service:8000',  
}

#Ruta para reenviar a user_service
@app.api_route('/{service}/{path:path}', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
async def gateway(service: str, path: str, request: Request):
    if service not in MICROSERVICES:
        raise HTTPException(status_code=404, detail='Servicio no encontrado')

    url = f'{MICROSERVICES[service]}/{path}'
    method = request.method
    headers = dict(request.headers)
    body = await request.body()

    async with httpx.AsyncClient() as client:
        response = await client.request(method, url, headers=headers, content=body)
        return response.json()