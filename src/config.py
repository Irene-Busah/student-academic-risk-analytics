"""
config.py
===============

Configs the entities of the pipeline
"""


# importing libraries
from logging import config
from utils import create_dictionaries, read_yaml
from entity import DataIngestionConfig, DataTransformationConfig

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
            test_data_file_path=config.test_data_file_path,
            status_file=config.status_file
        )

        return data_ingestion_config
    
    def get_data_transformation_config(self) -> ConfigBox:
        """
        Gets the configurations for data transformation
        
        :return: Returns a dictionary of the configurations
        :rtype: ConfigBox
        """

        config = self.config.data_transformation

        create_dictionaries([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            train_data_file_path=config.train_data_file_path,
            val_data_file_path=config.val_data_file_path,
            test_data_file_path=config.test_data_file_path
        )

        return data_transformation_config

