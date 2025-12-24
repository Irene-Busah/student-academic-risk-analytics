"""
main.py
==========


Sets up the entire project pipeline
"""


# importing the libraries
from logger import logger
from pipeline.data_ingestion_pipeline import DataIngestionPipeline

logger.info("End-to-end Machine Learning Project")


# =========================== Data Ingestion ===========================

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"------------ {STAGE_NAME} Started ------------")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initialize_data_ingestion()
    logger.info(f"------------ {STAGE_NAME} Completed ------------")

except Exception as e:
    logger.exception(e)
    raise e

