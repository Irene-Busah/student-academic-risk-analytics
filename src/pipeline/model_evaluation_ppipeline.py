"""
model_evaluation_pipeline.py
==========================

Orchestrates the model evaluation pipeline
"""


# libraries
from logger import logger
from config import ConfigurationManager
from components.model_evaluation import ModelEvaluation


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            logger.info("Model Evaluation Pipeline Started")

            config = ConfigurationManager()
            eval_config = config.get_model_evaluation_config()

            evaluator = ModelEvaluation(eval_config)

            model = evaluator.load_model()
            eval_df = evaluator.load_evaluation_data()

            X_eval, y_eval = evaluator.split_features_and_target(eval_df, model)


            metrics = evaluator.evaluate(model, X_eval, y_eval)
            evaluator.log_to_mlflow(model, metrics)

            logger.info("Model Evaluation Pipeline Completed")

        except Exception as e:
            logger.exception("Error in Model Evaluation Pipeline")
            raise e
