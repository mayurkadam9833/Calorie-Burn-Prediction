import os 
import pandas as pd 
from src.Calorie_Burn_Prediction.logging import logger 
from src.Calorie_Burn_Prediction.entity.config_entity import DataValidationConfig


"""
Initialize the DataValidation class with a DataValidationConfig object.
param config: DataValidationConfig containing dataset path, status file path, and expected schema.
"""
class DataValidation: 
    def __init__(self,config:DataValidationConfig):
        self.config=config 

    # Validate the dataset schema to ensure all expected columns are present.
    def schema_validation(self): 
        try: 
            # Assume schema is valid initially
            schema_validation=True

            # Load the dataset from the unzipped file path
            data=pd.read_csv(self.config.unzip_data)

            # Extract actual column names from the dataset
            all_col=list(data.columns)

            # Retrieve expected schema column names from configuration
            all_schema=list(self.config.all_schema.keys())

            # Compare actual dataset columns with expected schema
            for col in all_col: 
                # Skip the target column 'Calories' from validation
                if col == "Calories":
                    continue

                # If an unexpected column is found, mark validation as failed
                if col not in all_schema: 
                    schema_validation=False 

            # Write the final schema validation status to the status file
            with open(self.config.status_file,"w")as file: 
                file.write(f"schema validation:{schema_validation}")
            
            # Log successful completion of schema validation
            logger.info("schema validation completed")
        
        # Catch and raise any exceptions that occur during validation
        except Exception as e: 
            raise e 


