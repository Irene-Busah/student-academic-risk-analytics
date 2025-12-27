"""
model_training_pipeline.py
==========================

Orchestrates the model training workflow:
- Loads transformed data
- Splits features and target
- Trains the model
- Saves the trained model
"""


# libraries
from logger import logger
from config import ConfigurationManager
from components.model_training import ModelTraining


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        """
        Runs the end-to-end model training pipeline
        """

        try:
            logger.info("Starting Model Training Pipeline")


            # loading the configuration
            config = ConfigurationManager()
            model_training_config = config.get_model_training_config()

            # initializing component
            model_trainer = ModelTraining(config=model_training_config)

            # loading the transformed datasets
            train_data, val_data, test_data = model_trainer.load_transformed_data()


            # splitting the features and target feature
            x_train, y_train = model_trainer.split_features_and_target(train_data)

            # training the model
            model_trainer.train_model(x_train=x_train, y_train=y_train)

            # saving the model
            model_path = model_trainer.save_model()


            logger.info("Model Training Pipeline Completed Successfully")

            return model_path


        except Exception as e:
            logger.error(f"Error in Model Training Pipeline: {e}")
            raise e

