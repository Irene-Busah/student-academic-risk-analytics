from fastapi import FastAPI
from api.schema import StudentFeatures, PredictionResponse
from api.utils import load_model, load_scaler, load_encoders, prepare_features, predict

# ------------------- Configuration ------------------- #
# Define which features are used in the model
MODEL_FEATURES = [
    "GPA",
    "AttendanceRate",
    "TestScore_Math",
    "StudyHours",
    "ParentalEducation",
    "SchoolType",
    "Gender"
]

NUMERICAL_FEATURES = ["GPA", "AttendanceRate", "TestScore_Math", "StudyHours"]
CATEGORICAL_FEATURES = ["ParentalEducation", "SchoolType", "Gender"]  # any categorical in model_features

# ------------------- Load artifacts ------------------- #
model = load_model()
scaler = load_scaler()
encoders = load_encoders(CATEGORICAL_FEATURES)

# ------------------- FastAPI app ------------------- #
app = FastAPI(
    title="Student Academic Risk Prediction API",
    version="1.0.0"
)


@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.post("/predict", response_model=PredictionResponse)
def predict_academic_risk(data: StudentFeatures):
    """
    Generate prediction for academic risk
    """
    # Prepare features with proper scaling and encoding
    features_array = prepare_features(
        data=data,
        model_features=MODEL_FEATURES,
        categorical_columns=CATEGORICAL_FEATURES,
        numerical_columns=NUMERICAL_FEATURES,
        encoders=encoders,
        scaler=scaler
    )

    # Make prediction
    prediction, probability = predict(model, features_array)

    return {
        "academic_risk": int(prediction),
        "probability": float(probability),
    }
