"""
entity.py
==========

Implements the entities for the various components of the implementation pipeline
"""


# libraries
from dataclasses import dataclass
from pathlib import Path
from typing import List



# data ingestion entity
@dataclass
class DataIngestionConfig:
    root_dir: Path
    train_data_file_path: Path
    val_data_file_path: Path
    test_data_file_path: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    train_data_file_path: Path
    val_data_file_path: Path
    test_data_file_path: Path
    categorical_columns: List[str]
    numerical_columns: List[str]
    target_column: str


@dataclass
class ModelTrainingConfig:
    root_dir: Path
    train_data_file_path: Path
    val_data_file_path: Path
    test_data_file_path: Path
    model_name: str
    target_column: str
    model_features: List[str]
    scaled_features: List[str]

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    model_path: Path
    eval_data_file_path: Path
    target_column: str
    mlflow_experiment_name: str

