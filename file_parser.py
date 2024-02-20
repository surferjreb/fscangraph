# the parser for the file
# by James R. Brown

import pandas as pd

# determine type of file
# open file
# retrieve data specified
# output in a specified format


class FileParser:

    FILE_TYPE = {1: "csv", 2: "json", 3: "xml"}

    def __init__(self, file_path, file_type=1):
        self.file_path = file_path
        self.file_type = self.FILE_TYPE.get(file_type)
        self.data = None

    def parse_file(self):
        # parse file according to file type
        temp_data = None

        try:
            with open(self.file_path, 'r') as file:
                match self.file_type:
                    case "xml":
                        temp_data = pd.read_xml(file)
                    case "json":
                        temp_data = pd.read_json(file)
                    case "csv":
                        temp_data = pd.read_csv(file)
                    case _:
                        print("Invalid file type")

                self.set_file_data(temp_data)

        except Exception:
            print("Unabel to parse, check file format")

    def get_file_data(self):
        # output raw data
        return self.data

    def set_file_data(self, data):
        # TODO: put raw data into data object
        if data is not None:
            self.data = data
        else:
            raise ValueError("The data is of NoneType")
