from typing import Literal
from pydantic import BaseModel, Field

class CustomerInput(BaseModel):
    gender: Literal["Male", "Female"]
    country: Literal["France", "Germany", "Spain"]
    age: int = Field(..., ge=18, le=100)
    tenure: int = Field(..., ge=0, le=10)
    balance: float = Field(..., ge=0.0)
    products_number: int = Field(..., ge=1, le=4)
    active_member: Literal[0, 1]
    estimated_salary: float = Field(..., ge=0.0)

class PredictionResponse(BaseModel):
    churn_probability: float
    churn_prediction: int
    risk_label: str
