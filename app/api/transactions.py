from fastapi import APIRouter, HTTPException, status
from app.schemas.transaction import ( TransactionCreate,TransactionResponse)

router = APIRouter()

@router.get("/")
def get_transactions():
    return {"message":"All Transactions"}

@router.get("/{transaction_id}",response_model=TransactionResponse)
def get_transactions(transaction_id: int):
    #temp mock database
    transaction={
        1:{
            "id":1,
            "user_id": 101,
            "amount": 2500,
            "merchant": "Amazon",
            "location": "Banglore",
            "status": "pending"
        }
    }
    transaction=transaction.get(transaction_id)
    if transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction Not Found"
        )
    return transaction

@router.post("/", 
    response_model=TransactionResponse,
    status_code= status.HTTP_201_CREATED
    )
def create_transaction(transaction: TransactionCreate):
    if transaction.amount <=0:
        raise HTTPException(
            status_code=400,
            detail="Transaction amount must be greater than 0"
        )
    
    return {
        "id": 1,
        "user_id": transaction.user_id,
        "amount": transaction.amount,
        "merchant": transaction.merchant,
        "location": transaction.location,
        "status":"pending"
        
    }