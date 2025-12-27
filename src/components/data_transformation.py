"""
data_transformation.py
====================

Implements the data transformation components
"""



import scipy as sp
from logger import logger
from entity import DataTransformationConfig
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline
from pathlib import Path
import joblib



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        """
        Initialize DataTransformation component
        
        :param config: Data transformation configuration
        :type config: DataTransformationConfig
        """
        self.config = config
        self.encoders = {} 
        self.scaler = None

    def cast_categorical_columns(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Convert categorical columns to the correct data type - category
        
        :param dataframe: The dataframe to be transformed
        :type dataframe: pd.DataFrame
        :return: Transformed dataframe with categorical columns casted
        :rtype: pd.DataFrame
        """
        logger.info("Changing Categorical Columns")
        for col in self.config.categorical_columns:
            dataframe[col] = dataframe[col].astype('category')
        logger.info("Data Type Conversion Complete")
        return dataframe

    def create_target_feature(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Create the target feature 'academic_risk' based on GPA, AttendanceRate, and TestScore_Math
        
        :param dataframe: The dataset to be transformed
        :type dataframe: pd.DataFrame
        :return: Dataframe with a new target column
        :rtype: pd.DataFrame
        """
        dataframe[self.config.target_column] = (
            (dataframe['GPA'] < 2.5) |
            (dataframe['AttendanceRate'] < 0.85) |
            (dataframe['TestScore_Math'] < 50)
        ).astype(int)
        logger.info(f"Target Feature Created Successfully")
        return dataframe

    def fit_scaler(self, dataframe: pd.DataFrame):
        """
        Fit a StandardScaler on the numerical columns
        
        :param dataframe: The dataset to fit the scaler
        :type dataframe: pd.DataFrame
        """
        self.scaler = StandardScaler()
        self.scaler.fit(dataframe[self.config.numerical_columns])
        logger.info("Scaler Fitting Complete")

    def scale_numeric_features(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Scale the numerical features using the fitted StandardScaler
        
        :param dataframe: The dataframe to scale
        :type dataframe: pd.DataFrame
        :return: Dataframe with scaled numerical features
        :rtype: pd.DataFrame
        """

        dataframe = dataframe.copy()
        dataframe[self.config.numerical_columns] = self.scaler.transform(dataframe[self.config.numerical_columns])
        logger.info("Numeric Features Scaled Successfully!")
        return dataframe

    def fit_encoder(self, dataframe: pd.DataFrame):
        """
        Fit LabelEncoders on all categorical columns and store them
        
        :param dataframe: The dataframe to fit the encoders
        :type dataframe: pd.DataFrame
        """
        for col in self.config.categorical_columns:
            le = LabelEncoder()
            dataframe[col] = dataframe[col].astype(str)
            le.fit(dataframe[col])
            self.encoders[col] = le
        logger.info("Label Encoders Fitted Successfully!")
    


    def save_scaler(self):
        """
        Saves the fitted scaler to disk
        """

        scaler_path = Path(self.config.root_dir) / "scaler.joblib"
        joblib.dump(self.scaler, scaler_path)

        logger.info(f"Scaler saved at {scaler_path}")


    def encode_categorical_columns(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Encode categorical columns using fitted LabelEncoders
        
        :param dataframe: The dataframe to encode
        :type dataframe: pd.DataFrame
        :return: Dataframe with encoded categorical features
        :rtype: pd.DataFrame
        """

        dataframe = dataframe.copy()

        for col, le in self.encoders.items():
            dataframe[col] = dataframe[col].astype(str)

            known = dataframe[col].isin(le.classes_)
            dataframe.loc[known, col] = le.transform(dataframe.loc[known, col])
            dataframe.loc[~known, col] = -1

            dataframe[col] = dataframe[col].astype(int)

        logger.info("Categorical Encoding Complete!")
        return dataframe
    


    def save_transformed_data(self, dataframe: pd.DataFrame, file_path: Path):
        """
        Save the transformed dataframe to a CSV file
        
        :param dataframe: The dataframe to save
        :type dataframe: pd.DataFrame
        :param file_path: Path to save the transformed CSV
        :type file_path: Path
        """
        file_path.parent.mkdir(parents=True, exist_ok=True)
        dataframe.to_csv(file_path, index=False)
        logger.info(f"Successfully Saved the Transformed Data - {file_path}")

    
    def save_encoders(self):
        encoders_path = Path(self.config.root_dir) / "label_encoders.joblib"
        joblib.dump(self.encoders, encoders_path)
        logger.info(f"Encoders saved at {encoders_path}")

    
    def save_feature_metadata(self):
        metadata = {
            "categorical_columns": self.config.categorical_columns,
            "numerical_columns": self.config.numerical_columns,
            "target_column": self.config.target_column
        }

        metadata_path = Path(self.config.root_dir) / "feature_metadata.joblib"
        joblib.dump(metadata, metadata_path)

        logger.info("Feature metadata saved")

