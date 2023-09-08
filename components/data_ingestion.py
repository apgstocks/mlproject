import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

class DataIngestionCOnfig():
    train_path:str=os.path.join('artifacts','train.csv')
    test_path:str=os.path.join('artifacts','test.csv')
    rawa_data_path:str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionCOnfig()

    def initiate_ingestion(self):
        logging.info('Entered into ingestion class')
        try:
            df=pd.read_csv(r'C:\Users\Apsara\Music\mlproject\src\notebook\Student_Marks.csv')
            logging.info('read the dataset as data')
            os.makedirs(os.path.dirname(self.ingestion_config.train_path),exist_ok=True)
            df.to_csv(self.ingestion_config.rawa_data_path,index=False,header=True)
            logging.info('train test split is initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_path,index=False,header=True)
            logging.info('Train test split is completed')
            return (
                self.ingestion_config.train_path,
                self.ingestion_config.test_path
            )
        except Exception as e:
            raise CustomException(sys,e)
        
if __name__=='__main__':
    obj=DataIngestion()
    obj.initiate_ingestion()