"""
 Data Class
 A simple class for holding the data gathered from the file.
 @author: James R. Brown
"""


class Data:

    def __init__(self, data=None):
        self.data = data

    def set_data(self, new_data):
        """
            Sets some data to the data object
        """
        if new_data:
            self.data = new_data

    def __repr__(self):
        return str(self.data)
