from pydantic import BaseModel
from typing import List


class StudentFeatures(BaseModel):
    """
    Input schema for academic risk prediction
    """
    GPA: float
    AttendanceRate: float
    TestScore_Math: float
    StudyHours: float 
    ParentalEducation: str  
    SchoolType: str         
    Gender: str             



class PredictionResponse(BaseModel):
    """
    Output schema for prediction response
    """
    academic_risk: int
    probability: float
