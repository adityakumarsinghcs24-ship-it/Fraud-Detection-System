from fastapi import FastAPI
from app.api.transactions import router as transaction_router

app = FastAPI()
@app.get("/")
def root():
    return {"message":"Fraud Detection API is running."}

app.include_router(
    transaction_router,
    prefix="/transactions",
    tags=["Transactions"]
)