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