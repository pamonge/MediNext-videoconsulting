from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def gateway_root():
    return {"message": "Gateway is running"}