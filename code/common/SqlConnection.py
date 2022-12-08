import sqlite3
from common.BaseClass import BaseClass
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"


class ConnectFailed(Exception):
    def __init__(self):
        self.msg = 'Media Finder failed to initialize'
        super().__init__(self.msg)


class SQLConnection():

  def __init__(self,bc:BaseClass,database:str)
    self._bc=bc
    try:
      self._conn=sqlite3.connect(database)
    except:
      self._bc.log.error("\t"+":"+traceback.format_exc())
      raise ConnectFailed

