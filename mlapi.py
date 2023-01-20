from fastapi import FastAPI
from pydantic import BaseModel
import pickle

class DataType(BaseModel):
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

"""
Sample JSON Input:- 
{
    "NPPM": 123,
    "LoanStatus": "approved",
    "Objective": "business expansion",
    "Amount": 50000,
    "Guarantee": "collateral",
    "Experience": "5 years",
    "M_Status": "married",
    "ExistingLoan": 0,
    "Age": 35,
    "CA_Balance": "10000",
    "SA_Balance": "20000",
    "PI_Balance": 15000,
    "WorkAB": "private",
    "PhNum": 1234567890,
    "Tenure": 3,
    "prop": "commercial",
    "JobTyp": "self-employed",
    "HouseT": "own",
    "NOE": 2
}
"""

@app.post("/predict")
async def predict(item: DataType):
    return item

@app.get("/")
async def root():
    return {"message": "Hello World"}