import os 
import yaml
import json
from pathlib import Path 
from ensure import ensure_annotations 
from box import ConfigBox 
from box.exceptions import BoxValueError 
from src.Calorie_Burn_Prediction.logging import logger

# Function to read YAML file and return contents as ConfigBox (dict-like object)
@ensure_annotations 
def read_yaml(path_to_yaml:Path)-> ConfigBox: 
    try: 
        with open(path_to_yaml,"r")as yaml_file: 
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file loaded sucessfully from path: {path_to_yaml}")

    # Raised when YAML file is empty
    except BoxValueError: 
        raise ValueError("yaml file is empty")
    
    except Exception as e: 
        raise e 
     
    return ConfigBox(content)

# Function to create directories from a list of paths
@ensure_annotations 
def create_dir(path_file=list,verbose=True): 
    for path in path_file: 
        os.makedirs(path,exist_ok=True) 
        if verbose: 
            logger.info(f"{path} create sucessfully")

# Function to get file size in KB
@ensure_annotations
def get_size(file): 
    size_in_kb=round(os.path.getsize(file)/1024)
    return f"file size: {size_in_kb} KB"

# Function to save a Python dict as JSON file
@ensure_annotations 
def save_json(path:Path,data:dict): 
    with open(path,"w")as file: 
        json.dump(data,file,indent=4)
        logger.info(f"json file saved sucessfully at {path}")