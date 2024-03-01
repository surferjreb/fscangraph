"""
    Data Operator class
    This class provides the ability to disect the data gathered by the
    file_parser.
    @author: James R Brown
"""


class DataOperator:
    def __init__(self, data):
        self.data = data

    def search_columns(self, column_name):
        pass

    def search_in_column(self, search_value):
        pass

    def get_column_names(self):
        pass

    def get_column_values(self):
        pass

    def get_all(self):
        """
            returns data
        """
        return self.data

    def __repr__(self):
        return self.__name__
