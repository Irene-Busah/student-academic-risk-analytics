"""
data_ingestion_pipeline.py
============================


Sets up the data ingestion pipeline
"""


# libraries
from components.data_ingestion import DataIngestion
from config import ConfigurationManager
from logger import logger


STAGE_NAME = "Data Ingestion Stage"


class DataIngestionPipeline:
    def __init__(self):
        pass


    def initialize_data_ingestion(self):
        config = ConfigurationManager()

        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)

        return data_ingestion


if __name__ == '__main__':
    try:
        logger.info(f"--------------- {STAGE_NAME} Started ---------------")
        obj = DataIngestionPipeline()
        obj.initialize_data_ingestion()
        logger.info(f"--------------- {STAGE_NAME} Completed ---------------")
    
    except Exception as e:
        logger.exception(e)
        raise e