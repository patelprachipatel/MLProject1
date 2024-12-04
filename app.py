from src.mlproject1.logger import logging
from src.mlproject1.exception import CustomException
import sys
from src.mlproject1.components.data_ingestion import DataIngestion
from src.mlproject1.components.data_ingestion import DataIngestionConfig




if __name__ =="__main__":
    logging.info("the excution has started")

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)


