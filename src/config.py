"""
config.py
===============

Configs the entities of the pipeline
"""


# importing libraries
from logging import config
from utils import create_dictionaries, read_yaml
from entity import DataIngestionConfig, DataTransformationConfig, ModelTrainingConfig, ModelEvaluationConfig

from pathlib import Path
from box import ConfigBox



# defining the constants
CONFIG_FILE_PATH = Path('config.yaml')
# PARAM_FILE_PATH = Path('params.yaml')
# SCHEMA_FILE_PATH = Path('schema.yaml')



class ConfigurationManager:
    def __init__(self, config_path=CONFIG_FILE_PATH):
        self.config = read_yaml(config_path)
        # self.param = read_yaml(param_path)
        # self.schema = read_yaml(schema_path)

    def get_data_ingestion_config(self) -> ConfigBox:
        """
        Reads the data ingestion configuration 
        
        :return: Returns a dictionary with data loading configuration
        :rtype: ConfigBox
        """

        config = self.config.data_ingestion

        create_dictionaries([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            train_data_file_path=config.train_data_file_path,
            val_data_file_path=config.val_data_file_path,
            test_data_file_path=config.test_data_file_path
        )

        return data_ingestion_config
    
    def get_data_transformation_config(self) -> ConfigBox:
        """
        Gets the configurations for data transformation

        :return: Returns data transformation configuration
        :rtype: ConfigBox
        """

        config = self.config.data_transformation

        root_dir = Path(config.root_dir)
        create_dictionaries([root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=root_dir,
            train_data_file_path=Path(config.train_data_file_path),
            val_data_file_path=Path(config.val_data_file_path),
            test_data_file_path=Path(config.test_data_file_path),
            categorical_columns=config.categorical_columns,
            numerical_columns=config.numerical_columns,
            target_column=config.target_column
        )

        return data_transformation_config

    


    def get_model_training_config(self) -> ConfigBox:
        """
        Gets the configurations for model training

        :return: Returns model training configuration
        :rtype: ConfigBox
        """

        config = self.config.model_training

        root_dir = Path(config.root_dir)
        create_dictionaries([root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir=root_dir,
            train_data_file_path=Path(config.train_data_file_path),
            val_data_file_path=Path(config.val_data_file_path),
            test_data_file_path=Path(config.test_data_file_path),
            model_name=config.model_name,
            target_column=config.target_column,
            model_features=config.model_features,
            scaled_features=config.scaled_features
        )

        return model_training_config

    



    def get_model_evaluation_config(self) -> ConfigBox:
        config = self.config.model_evaluation

        create_dictionaries([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            model_path=config.model_path,
            eval_data_file_path=config.eval_data_file_path,
            target_column=config.target_column,
            mlflow_experiment_name=config.mlflow_experiment_name
        )

        return model_evaluation_config



