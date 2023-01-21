from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
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
    "NPPM": 1,
    "LoanStatus": "no loans taken/all loans paid back duly",
    "Objective": "New Car Purchase",
    "Amount": 50000,
    "Guarantee": "co-applicant",
    "Experience": "between 1 and 4 years",
    "M_Status": "male and divorced/seperated",
    "ExistingLoan": 0,
    "Age": 35,
    "CA_Balance": "no current account",
    "SA_Balance": "greater than 1000",
    "PI_Balance": 15000,
    "WorkAB": "Yes",
    "PhNum": 0,
    "Tenure": 3,
    "prop": "Real Estate",
    "JobTyp": "skilled employee / official",
    "HouseT": "own",
    "NOE": 2
}
"""

def Preprocessing(df):
    df.Objective = df.Objective.replace({"New Car Purchase": 0, "Purchase of radio/television" : 1,'Purchase of furniture/equipment' : 2,'Old Car Repair': 3,'Education Loan': 4,
                                    'Loan for business establishment': 5,'Other repairs': 6,'Purchase of domestic appliances': 7,'Loan for retraining': 8})
    df.Guarantee = df.Guarantee.replace({'none' : 0,'gaurantor' : 1,'co-applicant':  2})
    df.LoanStatus = df.LoanStatus.replace({'critical account/other loans existing (not at this bank)' : 0,'existing loans paid back duly till now' : 1,'all loans at this bank paid back duly':  2,'delay in paying off loans in the past' : 3,
                                        'no loans taken/all loans paid back duly': 4})
    df.Experience = df.Experience.replace({'between 1 and 4 years': 0, 'greater than 4 years': 1,'less than a year': 2,'unemployed': 3})
    df.M_Status = df.M_Status.replace({'female and divorced/seperated/married': 0,'male and single': 1,'male and married/widowed': 2,
                                    'male and divorced/seperated': 3})
    df.CA_Balance = df.CA_Balance.replace({'no current account': 0,'less than 0': 1,'between 0 and 200': 3,'greater than 200': 4})
    df.SA_Balance = df.SA_Balance.replace({'less than 100': 0,'no savings account': 1,'between 500 and 1000': 2,
                                        'between 100 and 500': 3,'greater than 1000': 4})
    df.WorkAB = df.WorkAB.replace({'Yes': 1,'No': 0})
    df.PhNum = df.PhNum.replace({'Yes': 1,'No': 0})
    df.prop = df.prop.replace({'Real Estate': 0,'car or other property': 1,'No property': 2,'building society savings agreement/life insurance': 3})
    df.JobTyp = df.JobTyp.replace({'skilled employee / official': 0,'unskilled - resident': 1,'unemployed/ unskilled - non-resident': 2,'management/ self-employed/highly qualified employee/ officer': 3})
    df.HouseT = df.HouseT.replace({'own': 0,'for free': 1,'rent': 3})
    return df

with open("/Users/hemangjiwnani/Desktop/Projects/Hackathon_IITII/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/predict")
async def predict(item: DataType):
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    df = Preprocessing(df)
    temp = list(df.iloc[0])
    ans1 = list(model.predict([temp]))
    return int(ans1[0])

@app.get("/")
async def root():
    return {"message": "This API Only Has Get Method as of now"}