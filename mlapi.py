from fastapi import FastAPI
from pydantic import BaseModel

class item(BaseModel):
    NPPM: int
    LoanStatus: str
    Objective: str
    Amount: int
    Guarantee: str
    Experience: str
    M_Status: str
    ExistingLoan: int
    Age: int
    CA_Balance: str
    SA_Balance: str
    PI_Balance: int
    WorkAB: str
    PhNum: int
    Tenure: int
    prop: str
    JobTyp: str
    HouseT: str
    NOE: int

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}