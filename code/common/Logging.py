import logging
import datetime

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"

class LoggingException(Exception):
    def __init__(self):
        self.msg = 'Could not start app.'
        super().__init__(self.msg)

class Logging():

    def __init__ (self, file_name:str, log_level:int):
        try:

            logging.Formatter('%(asctime)s %(message)s')
            logging.basicConfig(filename=file_name, filemode='w', level=log_level,format=' %(asctime)s  %(message)s')
            self._log_level = int(log_level)
        except:
            raise LoggingException

    def info (self,message):
        if self._log_level ==logging.INFO :
            logging.info(str(message))

    def warning (self,message):
        if self._log_level == logging.WARNING :
            logging.warning(str(message))

    def error (self,message):
        if self._log_level == logging.ERROR :
            logging.error(str(message))

    def debug (self,message):
        if self._log_level == logging.DEBUG :
            logging.debug(str(message))

