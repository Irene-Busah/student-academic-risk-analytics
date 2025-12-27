import joblib
import numpy as np
from pathlib import Path
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Paths
BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = BASE_DIR / "artifacts" / "model_training" / "model.joblib"
SCALER_PATH = BASE_DIR / "artifacts" / "data_transformation" / "scaler.joblib"
ENCODERS_PATH = BASE_DIR / "artifacts" / "data_transformation" / "label_encoders.joblib" 


# ------------------ Load artifacts ------------------ #
def load_model():
    return joblib.load(MODEL_PATH)


def load_scaler():
    return joblib.load(SCALER_PATH)


def load_encoders(categorical_columns):
    """
    Load LabelEncoders for all categorical features from a single joblib file
    """
    all_encoders = joblib.load(ENCODERS_PATH)

    # Keep only the encoders needed for inference
    encoders = {col: all_encoders[col] for col in categorical_columns}

    return encoders


# ------------------ Feature preprocessing ------------------ #
def prepare_features(data, model_features, categorical_columns, numerical_columns, encoders, scaler):
    """
    Prepare input array for prediction:
    - Encode categorical features
    - Scale numerical features
    - Arrange in correct order for model_features
    """

    feature_dict = data.dict()  # assume pydantic input

    # Encode categorical columns
    for col in categorical_columns:
        if col in feature_dict:
            feature_dict[col] = encoders[col].transform([str(feature_dict[col])])[0]

    # Scale numerical columns
    num_values = [feature_dict[col] for col in numerical_columns if col in feature_dict]
    if num_values:
        scaled_values = scaler.transform([num_values])[0]
        for i, col in enumerate([col for col in numerical_columns if col in feature_dict]):
            feature_dict[col] = scaled_values[i]

    # Create final array in order of model_features
    final_features = np.array([[feature_dict[col] for col in model_features]])

    return final_features


# ------------------ Prediction ------------------ #
def predict(model, features_array):
    """
    Generate prediction and probability
    """
    prediction = model.predict(features_array)[0]
    probability = model.predict_proba(features_array)[0][1]

    return prediction, probability
