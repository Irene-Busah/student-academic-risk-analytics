"""
main.py
==========


Sets up the entire project pipeline
"""


# importing the libraries
from logger import logger
from pipeline.data_ingestion_pipeline import DataIngestionPipeline
from pipeline.data_transform_pipeline import DataTransformationPipeline

logger.info("End-to-end Machine Learning Project")


# =========================== Data Ingestion ===========================

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"------------ {STAGE_NAME} Started ------------")
    data_ingestion_pipeline = DataIngestionPipeline()
    train_df, val_df, test_df = data_ingestion_pipeline.initialize_data_ingestion()
    logger.info(f"------------ {STAGE_NAME} Completed ------------")

except Exception as e:
    logger.exception(e)
    raise e


# =========================== Data Transformation ===========================


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"------------ {STAGE_NAME} Started ------------")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.initialize_data_transformation(
        train_df, val_df, test_df
    )
    logger.info(f"------------ {STAGE_NAME} Completed ------------")

except Exception as e:
    logger.exception(e)
    raise e

