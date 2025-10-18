import os
import zipfile
from urllib.request import urlretrieve
from src.Calorie_Burn_Prediction.entity.config_entity import DataIngestionConfig 
from src.Calorie_Burn_Prediction.utils.common import get_size
from src.Calorie_Burn_Prediction.logging import logger


"""
Initialize the DataIngestion class with a DataIngestionConfig object.
param config: DataIngestionConfig containing source URL, local file path, and unzip directory
"""
class DataIngestion: 
    def __init__(self,config:DataIngestionConfig):
        self.config=config 

    # method for Download the dataset file from the source URL to the local path specified in config.
    def download_file(self): 
        try: 
            # Check if the file already exists locally
            if not os.path.exists(self.config.local_data_file): 
                filename,header=urlretrieve(
                    url=self.config.source_url, 
                    filename=self.config.local_data_file
                    )
                logger.info(f"{self.config.local_data_file} download sucessfully from folllowing header:\n{header}")

            # If file exists, log its size
            else: 
                logger.info(f"{self.config.local_data_file} is already exits of size:{get_size(self.config.local_data_file)}")

        # Raise any exceptions encountered during download
        except Exception as e: 
            raise e 
    
    #  Extract the downloaded ZIP file to the directory specified in config.
    def extract_file(self): 
        unzip_path=self.config.unzip_dir
        
        # Ensure the unzip directory exists
        os.makedirs(unzip_path,exist_ok=True)

        # Open the zip file and extract all contents
        with zipfile.ZipFile(self.config.local_data_file,"r")as zip_ref: 
            zip_ref.extractall(unzip_path)
        