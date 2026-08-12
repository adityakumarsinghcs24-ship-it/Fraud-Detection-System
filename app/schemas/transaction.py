from pydantic import BaseModel

class TransactionCreate(BaseModel):
    user_id: int 
    amount: float
    merchant: str
    location: str

class TransactionResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    merchant: str
    location: str
    status: str
