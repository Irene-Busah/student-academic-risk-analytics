"""
main.py
==========


Sets up the entire project pipeline
"""


# importing the libraries
from logger import logger
from pipeline.data_ingestion_pipeline import DataIngestionPipeline
from pipeline.data_transform_pipeline import DataTransformationPipeline
from pipeline.model_training_pipeline import ModelTrainingPipeline
from pipeline.model_evaluation_ppipeline import ModelEvaluationPipeline

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



# ====================== Model Training ======================

STAGE_NAME = "Model Training Stage"

try:
    logger.info(f"------------ {STAGE_NAME} Started ------------")
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.initiate_model_training()
    logger.info(f"------------ {STAGE_NAME} Completed ------------")

except Exception as e:
    logger.exception(e)
    raise e



# ====================== Model Evaluation ======================

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f"------------ {STAGE_NAME} Started ------------")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.initiate_model_evaluation()
    logger.info(f"------------ {STAGE_NAME} Completed ------------")

except Exception as e:
    logger.exception(e)
    raise e


