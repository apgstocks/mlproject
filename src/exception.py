import sys
import logging
def error_msg_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    errmsg=exc_tb.tb_lineno
    error_message="Error occured in python script name:[{0}] line no [{1}] error msg [{2}]".format(filename,errmsg,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_msg_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message    

if __name__=='__main__':
    try:
        a=1/0
    except Exception as e:
        logging.info('Divide by zero exception')
        raise CustomException(e,sys)
        

