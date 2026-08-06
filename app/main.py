from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"message":"Fraud Detection API is running."}
    