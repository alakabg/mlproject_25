import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    line_number = exc_tb.tb_lineno
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = f"Error occurred in the python script: {file_name} at line: {line_number} | Error message: {str(error)}"
    return error_msg

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    
# # #Check the exception handling code
# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logging.info("Dividing by zero error caught")   #Its not logged in log file. WHY? --> Need to import logger.py ie src.logger tehn import logger
#         raise CustomException(e, sys)