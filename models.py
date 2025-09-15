from pydantic import BaseModel 

class Users(BaseModel):
    id:str
    name:str
    phone:str
    userid:str
    password:str
    role:str

class DayBank(BaseModel):
    id:str
    date:str
    userid:str
    no_of_times_taken:int
    total_otpc_taken:int
    total_amount_spent:float
    remaining_otpc:int
    balance_otpc:int
    amount_gained:float

class MonthlyStatement(BaseModel):
    id:str
    userid:str
    balance_otpc:int
    amount_gained:float


    