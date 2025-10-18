from src.Calorie_Burn_Prediction.utils.common import create_dir,read_yaml 
from src.Calorie_Burn_Prediction.entity.config_entity import DataIngestionConfig,DataValidationConfig
from src.Calorie_Burn_Prediction.constants import *


"""
    The ConfigManager class is responsible for:
    - Reading configuration, schema, and parameter files.
    - Creating necessary directories.
    - Returning configuration objects for different pipeline components.
"""
class ConfigManager: 
    def __init__(
        self, 
        config_file=CONFIG_FILE_PATH, 
        schema_file=SCHEMA_FILE_PATH, 
        params_file=PARAMS_FILE_PATH): 

        # Read YAML configuration files
        self.config=read_yaml(config_file)   # Loads main pipeline configuration
        self.schema=read_yaml(schema_file)   # Loads dataset schema definitions
        self.params=read_yaml(params_file)   # Loads model and training parameters

        # Create the root directory where all artifacts will be stored
        create_dir([self.config.artifacts_root])

    # method to get data ingestion config object
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        # Access data ingestion-related configuration details 
        config=self.config.data_ingestion 

        # Create the data ingestion root directory
        create_dir([config.root_dir])

        # Create and return the DataIngestionConfig dataclass instance
        data_ingestion_config=DataIngestionConfig( 
            root_dir=config.root_dir,
            source_url=config.source_url, 
            local_data_file=config.local_data_file, 
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    # method to get data validation config object
    def get_data_validation_config(self)-> DataValidationConfig: 
        # Access data validation-related configuration details 
        config=self.config.data_validation 
        schema=self.schema.COLUMNS 

        # Create the data validation root directory
        create_dir([config.root_dir])

        # Create and return the DataValidationConfig dataclass instance
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir, 
            unzip_data=config.unzip_data, 
            status_file=config.status_file, 
            all_schema=schema
        )
        return data_validation_config


