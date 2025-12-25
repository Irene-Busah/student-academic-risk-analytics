"""
data_ingestion.py
====================

Implements the data ingestion components
"""


# libraries
from logger import logger
from entity import DataIngestionConfig
import pandas as pd
import io


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    # method to laod the data
    def load_data(self):
        train_data = pd.read_csv(self.config.train_data_file_path)
        val_data = pd.read_csv(self.config.val_data_file_path)
        test_data = pd.read_csv(self.config.test_data_file_path)

        logger.info(f"Loading the Data from the local directory")

        logger.info(f"Training data shape: {train_data.shape}")
        logger.info(f"Validation data shape: {val_data.shape}")
        logger.info(f"Testing data shape: {test_data.shape}")
        
        logger.info("Data Summary Loaded Successfully")

        return train_data, val_data, test_data
