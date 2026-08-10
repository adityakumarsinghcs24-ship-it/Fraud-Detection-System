from fastapi import APIRouter
from app.schemas.transaction import TransactionCreate

router = APIRouter()

@router.get("/")
def get_transactions():
    return {"message":"All Transactions"}

@router.post("/")
def create_transaction(transaction: TransactionCreate):
    return {
        "message":"Transaction recieved",
        "transaction": transaction
    }