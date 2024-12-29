from src.mlproject1.logger import logging
from src.mlproject1.exception import CustomException
import sys
from src.mlproject1.components.data_ingestion import DataIngestion
from src.mlproject1.components.data_ingestion import DataIngestionConfig
from src.mlproject1.components.data_transformation import DataTransformation
from src.mlproject1.components.data_transformation import DataTransformationConfig



if __name__ =="__main__":
    logging.info("the excution has started")

    try:
        data_ingestion = DataIngestion()
        train_data_path , test_data_path = data_ingestion.initiate_data_ingestion()
        print(train_data_path, '  ---------------', test_data_path)

        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path , test_data_path)

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)


