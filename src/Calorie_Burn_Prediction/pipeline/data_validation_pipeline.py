from src.Calorie_Burn_Prediction.config.configuration import ConfigManager
from src.Calorie_Burn_Prediction.components.data_validation import DataValidation

"""
    This class orchestrates the data validation process:
    1. Loads configuration using ConfigManager.
    2. Retrieves the DataValidationConfig dataclass instance.
    3. Performs schema validation on the dataset.
"""
class DataValidationPipeline: 
    def __init__(self):
        pass
    
    # Main method to run the data validation pipeline
    def main(self): 
        config=ConfigManager()                                         # Step 1: Load pipeline configuration
        data_validation_config=config.get_data_validation_config()     # Step 2: Get DataValidationConfig dataclass instance
        data_validation=DataValidation(config=data_validation_config)  # Step 3: Initialize the DataValidation component with config
        data_validation.schema_validation()                            # Step 4: Perform schema validation on the dataset