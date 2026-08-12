from fastapi import FastAPI, Request
from app.api.transactions import router as transaction_router
from fastapi.responses import JSONResponse

app = FastAPI()
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )
@app.get("/")
def root():
    return {"message":"Fraud Detection API is running."}

app.include_router(
    transaction_router,
    prefix="/transactions",
    tags=["Transactions"]
)