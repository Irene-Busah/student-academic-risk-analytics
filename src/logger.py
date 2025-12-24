"""
logger.py
==========

Custom logging setup
"""

# implementing the relevant libraries
import os
import sys
import logging


log_text = "[%(asctime)s: %(levelname)s: %(message)s]"

# defining the logging file
log_dir = 'logs'
log_filepath = os.path.join(log_dir, 'logging.log')

os.makedirs(log_dir, exist_ok=True)

# setting up the basic logging
logging.basicConfig(
    level=logging.INFO,
    format=log_text,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("student_academic_risk_model_logger")
