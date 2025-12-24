"""
entity.py
==========

Implements the entities for the various components of the implementation pipeline
"""


# libraries
from dataclasses import dataclass
from pathlib import Path

from matplotlib.pyplot import cla



# data ingestion entity
@dataclass
class DataIngestionConfig:
    root_dir: Path
    train_data_file_path: Path
    val_data_file_path: Path
    test_data_file_path: Path
    status_file: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    train_data_file_path: Path
    val_data_file_path: Path
    test_data_file_path: Path

