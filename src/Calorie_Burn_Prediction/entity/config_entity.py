from pathlib import Path 
from dataclasses import dataclass 

"""
Configuration class for the Data Ingestion component.
Contains all the necessary paths and URLs used during data download and extraction.
"""
@dataclass(frozen=True)
class DataIngestionConfig: 
    root_dir: Path           # Directory where all data ingestion-related files will be stored
    source_url: str          # URL to download the dataset from
    local_data_file: Path    # Path to store the downloaded dataset locally
    unzip_dir: Path          # Directory where the dataset will be extracted after download


"""
Configuration class for the Data Validation component.
Contains all the necessary paths used during data validation.
"""
@dataclass(frozen=True)
class DataValidationConfig: 
    root_dir: Path           # Directory where all data validation-related files will be stored
    unzip_data: Path         # Path to the unzipped dataset that needs to be validated
    status_file: str         # File path where the validation status (True/False) will be saved
    all_schema: dict         # Dictionary containing the expected schema (column names and data types)