import sys


def error_message_details(error,error_detail:sys):
    exc_type,exc_value,exc_tb=error_detail.exc_info()

    if exec_type is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "unknow file (raised outside try-except block)"
        line_number = "Unknown line" 

    error_message="Error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
    file_name,line_number,str(error)
    )
    return error_message

    
class CustomException(Exception):
    def _init__(self,error_message,error_detail:sys):
        #super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail=error_detail)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message



