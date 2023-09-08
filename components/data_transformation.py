import numpy as np
import os,sys
from dataclasses import dataclass
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
@dataclass
class DataTransformConfig():
    preprocessor_ob_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransform():
    def __init__(self):
        self.transformconfig=DataTransformConfig()

    def get_transform(self):
        try:
            numerical_column=['reading score','writing score']
            categorical_column=['gender','race_ethnicity','parental_level_of_education','lunch',
                                'test_preparation_course']
            num_pipeline=Pipeline(steps=[('imputer',SimpleImputer(strategy='median')),
                                         ('scaler',StandardScaler())
            ])
            cat_pipeline=Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                #('scaler',StandardScaler()),
                ('one hot',OneHotEncoder())

            ])
            logging.info('Categorical columsn enconding completed')
            preprocessor=ColumnTransformer(
                [
                    ('num_pipeline',num_pipeline,numerical_column),
                    ('cat_pipeline',cat_pipeline,categorical_column)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(sys,e)

    def initiate_datatransformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info('read test/train data success')
            logging.info('proceeding with preprocessing')
            preprocessor_obj=self.get_transform()
            target=['math score']
            numerical_col=['writing score','reading score']
            input_feature_train_df=train_df.drop(columns=target)
            input_feature_test_df=test_df.drop(columns=target)
            target_feature_train_df=train_df[target]
            target_feature_test_df=test_df[target]
            logging.info('applying preprocessing on dataframes')
            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.fit_transform(input_feature_test_df)
            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]
            logging.info('saving the preprocessing object')
            save_object(
                file_path=self.transformconfig.preprocessor_ob_file_path,
                obj=preprocessor_obj
            )
            return(
                train_arr,test_arr,self.transformconfig.preprocessor_ob_file_path,
            )

        except Exception as e:
            raise CustomException(e,sys)
