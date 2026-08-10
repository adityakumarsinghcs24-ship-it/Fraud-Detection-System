from pydantic import BaseModel

class TransactionCreate(BaseModel):
    user_id: int 
    amount: float
    merchant: str
    location: str
    