"""
utils.py
=========


Implements the utility functions needed in the project
"""

# implementing the necessary libraries
import os, yaml
from logger import logger
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path


# function to read YAML file
@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    """
    Reads the yaml files with the parameters
    
    :param file_path: The path to the YAML file
    :type file_path: Path
    :return: A dictionary of the key parameters needed
    :rtype: ConfigBox
    """

    try:
        with open(file_path) as file:
            content = yaml.safe_load(file)

            logger.info(f"Successfully loaded the YAML file: {file.name}")

            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty or not found")
    except Exception as e:
        raise e


# function to create dictionaries
@ensure_annotations
def create_dictionaries(directory_name: list, verbose=True):
    """
    Creates different directories for the various stages of the modelling
    
    :param directory_name: The stage name used to create the directory
    :type directory_name: list
    """

    for path in directory_name:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logger.info(f"Directory Created Successfully - {path}")

