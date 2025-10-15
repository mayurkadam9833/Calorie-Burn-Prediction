from pathlib import Path 

# Define important file paths used across the Calorie Burn Prediction pipeline.

# Path to the main configuration file that stores project-wide settings 
# (e.g., directory paths, data source URLs, etc.)
CONFIG_FILE_PATH=Path("config/config.yaml")

# Path to the schema file which defines the structure, data types, 
# and validation rules for the dataset.
SCHEMA_FILE_PATH=Path("schema.yaml")

# Path to the parameters file containing model training parameters 
# such as learning rate, max depth etc.
PARAMS_FILE_PATH=Path("params.yaml")