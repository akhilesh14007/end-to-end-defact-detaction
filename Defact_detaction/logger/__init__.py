# import logging
import os
import logging

from datetime import datetime
from from_root import from_root

# Define the log file name based on current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log directory path
log_dir = os.path.join(from_root(), 'log')

# Ensure the log directory exists
os.makedirs(log_dir, exist_ok=True)

# Define the full path to the log file
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
