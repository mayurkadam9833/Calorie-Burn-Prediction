from src.Calorie_Burn_Prediction.config.configuration import ConfigManager 
from src.Calorie_Burn_Prediction.components.data_ingestion import DataIngestion

"""
    This class orchestrates the data ingestion process:
    1. Loads configuration using ConfigManager.
    2. Downloads the dataset from the source URL.
    3. Extracts the downloaded ZIP file to the specified directory.
"""
class DataIngestionPipeline: 
    def __init__(self):
        pass
    #  Main method to run the data ingestion pipeline.
    def main(self):
        config=ConfigManager()                                     # Step 1: Load pipeline configuration
        data_ingestion_config=config.get_data_ingestion_config()   # Step 2: Get DataIngestionConfig dataclass instance
        data_ingestion=DataIngestion(config=data_ingestion_config) # Step 3: Initialize the DataIngestion component with config
        data_ingestion.download_file()                             # Step 4: Download the dataset if not already present
        data_ingestion.extract_file()                              # Step 5: Extract the downloaded ZIP file