"""
data_transform_pipeline.py
============================


Sets up the data transformation pipeline
"""


# libraries
import pandas as pd
from components.data_transformation import DataTransformation
from config import ConfigurationManager
from logger import logger


class DataTransformationPipeline:
    def __init__(self):
        pass
    
    # method to initiate the transformation pipeline
    def initialize_data_transformation(self, train_data: pd.DataFrame, val_data: pd.DataFrame, test_data: pd.DataFrame):
        try:
            config = ConfigurationManager()

            data_transformation_config = config.get_data_transformation_config()
            data_transform = DataTransformation(data_transformation_config)

            # loading the train data frame
            train_data = data_transform.cast_categorical_columns(train_data)
            train_data = data_transform.create_target_feature(train_data)

            data_transform.fit_encoder(train_data)
            data_transform.fit_scaler(train_data)

            train_data = data_transform.encode_categorical_columns(train_data)
            train_data = data_transform.scale_numeric_features(train_data)


            # loading the validation data
            val_data = data_transform.cast_categorical_columns(val_data)
            val_data = data_transform.create_target_feature(val_data)

            val_data = data_transform.encode_categorical_columns(val_data)
            val_data = data_transform.scale_numeric_features(val_data)

            # loading the test data
            test_data = data_transform.cast_categorical_columns(test_data)
            test_data = data_transform.create_target_feature(test_data)
            test_data = data_transform.encode_categorical_columns(test_data)
            test_data = data_transform.scale_numeric_features(test_data)

            # saving the output
            data_transform.save_transformed_data(
                train_data, data_transformation_config.root_dir / "train.csv"
            )
            data_transform.save_transformed_data(
                val_data, data_transformation_config.root_dir / "val.csv"
            )
            data_transform.save_transformed_data(
                test_data, data_transformation_config.root_dir / "test.csv"
            )
        
        except Exception as e:
            raise e
