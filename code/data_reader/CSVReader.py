from common.BaseClass import BaseClass,AppException
import csv
import traceback

class CSVReadException(Exception):
    def __init__(self):
        self.msg="Could not read from file"
        super().__init__(self.msg)

class CSVOpenException(Exception):
    def __init__(self):
        self.msg="Could not open CSV file"
        super().__init(self.msg)


## CSVRead open a text file and reads in lines like a SQL Query would read
## a table.
class CSVReader():
    records=[]
    record_pointer=-1
    def __init__(self,bc:str,file_name:str):
        self._bc=bc
        self._file_name=file_name
        try:
            self.read_record()
        except CSVOpenException as e:
            raise AppException
        except CSVReadException as e:
            pass
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise AppException

    def read_record(self):
        try:
            with open(self._file_name) as csvFile:
                try:
                    for row in csv.reader(csvFile,delimiter=','):
                        CSVReader.records.append(row)
                        print(row[0])
                except IOError as e:
                    self._bc.log.error("\t"+":"+traceback.format_exc())
                    raise CSVReadException
                except:
                    self._bc.log.error("\t"+":"+traceback.format_exc())
                    raise AppException
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise CSVOpenException

    def next_record(self):

        CSVReader.record_pointer=CSVReader.record_pointer+1
        if CSVReader.record_pointer> 100:
            raise IndexError
        return CSVReader.records[CSVReader.record_pointer]


