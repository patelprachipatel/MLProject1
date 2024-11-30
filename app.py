from src.mlproject1.logger import logging
from src.mlproject1.exception import CustomException
import sys



if __name__ =="__main__":
    logging.info("the excution has started")

    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)


