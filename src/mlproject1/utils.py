import os
import sys
import pandas as pd 
from src.mlproject1.exception import CustomException
from src.mlproject1.logger import logging
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    logging.info("Reading Mysql database started")
    try:
        mydb = pymysql.connect(
            host = host,
            db=db,
            password=password,
            user = user
        ) 
        logging.info("connection established", mydb)
        df= pd.read_sql_query('Select * from students', mydb)
        print(df.head())
        return df
        
    except Exception as e:
        raise CustomException(e,sys)