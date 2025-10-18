from src.Calorie_Burn_Prediction.pipeline.data_ingsetion_pipeline import DataIngestionPipeline 
from src.Calorie_Burn_Prediction.pipeline.data_validation_pipeline import DataValidationPipeline
from src.Calorie_Burn_Prediction.logging import logger 

# data ingestion pipeline [download data from source url and extract to defined path]
stage_one="Data Ingestion"
if __name__ =="__main__": 
    try: 
        logger.info(f"<<<< stage: {stage_one} started >>>>")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f"<<<< stage: {stage_one} completed >>>>")
    except Exception as e: 
        logger.info(e)
        raise e

# data validation pipeline [validate the dataset schema and save validation status]
stage_two="Data Validation"
if __name__ == "__main__": 
    try: 
        logger.info(f"<<<< stage: {stage_two} started >>>>")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f"<<<< stage: {stage_two} completed >>>>")
    except Exception as e: 
        logger.info(e)
        raise e