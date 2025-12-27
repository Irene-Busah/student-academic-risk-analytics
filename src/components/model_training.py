"""
model_training.py
=================

Implements the model training component responsible for:
- Loading transformed datasets
- Splitting features and target
- Training the model
- Saving the trained model
"""


# libraries
import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from entity import ModelTrainingConfig
from pathlib import Path
import joblib
from logger import logger


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        """
        Initializes the ModelTraining component

        :param config: Model training configuration
        :type config: ModelTrainingConfig
        """

        self.config = config
        self.model = None

    def load_transformed_data(self):
        """
        Loads the transformed train, validation, and test datasets

        :return: Train, validation, and test DataFrames
        :rtype: tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]
        """

        train_data = pd.read_csv(PROJECT_ROOT / self.config.train_data_file_path)
        val_data = pd.read_csv(PROJECT_ROOT / self.config.val_data_file_path)
        test_data = pd.read_csv(PROJECT_ROOT / self.config.test_data_file_path)

        logger.info("Transformed datasets loaded successfully")

        return train_data, val_data, test_data
    

    def split_features_and_target(self, dataframe: pd.DataFrame):
        """
        Splits features and target variable

        :param dataframe: Input dataset
        :type dataframe: pd.DataFrame
        :return: Features (X) and target (y)
        :rtype: tuple[pd.DataFrame, pd.Series]
        """

        missing_features = set(self.config.model_features) - set(dataframe.columns)
        if missing_features:
            raise ValueError(f"Missing model features: {missing_features}")

        X = dataframe[self.config.model_features]
        y = dataframe[self.config.target_column]

        logger.info(f"Training with features: {self.config.model_features}")

        return X, y
    

    def train_model(self, x_train: pd.DataFrame, y_train: pd.Series):
        """
        Trains the classification model

        :param X_train: Training features
        :param y_train: Training labels
        """

        self.model = LogisticRegression(
            penalty="l2",
            C=1.0,
            solver="lbfgs",
            max_iter=1000,
            class_weight="balanced",
            random_state=42
        )

        self.model.fit(X=x_train, y=y_train)

        logger.info("Model Training Completed Successfully")

    
    def save_model(self):
        """
        Saves the trained model to disk
        """

        model_path = Path(self.config.root_dir) / self.config.model_name
        joblib.dump(self.model, model_path)

        logger.info(f"Model Saved Successfully - {model_path}")
        return model_path

