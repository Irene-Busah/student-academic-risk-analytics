"""
model_evaluation.py
==========================

Orchestrates the model evaluation workflow:
- Loads trained model
- Evaluates the model performance
- Logs the results to MLFlow
"""



# libraries
import pandas as pd
import joblib
import mlflow
import mlflow.sklearn
from pathlib import Path
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score, roc_auc_score,
    confusion_matrix
)
from logger import logger
from entity import ModelEvaluationConfig


PARENT_ROOT = Path(__file__).resolve().parents[1]


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        """
        Initializes the ModelEvaluation component

        :param config: Model evaluation configuration
        """
        self.config = config

    
    def load_model(self):
        model_path = PARENT_ROOT / self.config.model_path
        model = joblib.load(model_path)

        logger.info(f"Model loaded from {model_path}")
        return model
    

    def load_evaluation_data(self):
        data_path = PARENT_ROOT / self.config.eval_data_file_path
        data = pd.read_csv(data_path)

        logger.info(f"Evaluation data loaded")
        return data
    

    def split_features_and_target(self, dataframe: pd.DataFrame, model):
        """
        Split evaluation dataframe into features and target,
        keeping only features used during model training.
        """

        # Target
        y = dataframe[self.config.target_column]

        # Features used during training
        trained_features = model.feature_names_in_

        # Select only those features (and preserve order)
        X = dataframe[trained_features]

        logger.info(f"Using evaluation features: {list(trained_features)}")

        return X, y

    

    def evaluate(self, model, X, y):
        y_pred = model.predict(X)
        y_prob = model.predict_proba(X)[:, 1]

        metrics = {
            "accuracy": accuracy_score(y, y_pred),
            "precision": precision_score(y, y_pred),
            "recall": recall_score(y, y_pred),
            "f1_score": f1_score(y, y_pred),
            "roc_auc": roc_auc_score(y, y_prob),
        }

        logger.info("Model evaluation metrics computed")
        return metrics
    

    def log_to_mlflow(self, model, metrics: dict):
        mlflow.set_experiment(self.config.mlflow_experiment_name)

        with mlflow.start_run():
            # Log model hyperparameters
            model_params = model.get_params()
            mlflow.log_params(model_params)

            # Log evaluation metrics
            mlflow.log_metrics(metrics)
            mlflow.sklearn.log_model(model, artifact_path="model")

            logger.info("Metrics and model logged to MLflow")

