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

        # capture dataframe info as string
        buffer = io.StringIO()
        train_data.info(buf=buffer)
        val_data.info(buf=buffer)
        test_data.info(buf=buffer)

        info_str = buffer.getvalue()

        with open(self.config.status_file) as file:
            file.write(f"Training Data Shape: {train_data.shape}")
            file.write(f"Validation Data Shape: {val_data.shape}")
            file.write(f"Testing Data Shape: {test_data.shape}")

            file.write(info_str)
        
        logger.info("Data Summary Loaded Successfully")
