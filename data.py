class Data:

    def __init__(self, data=None):
        self.data = data

    def set_data(self, new_data):
        if new_data:
            self.data = new_data

    def __repr__(self):
        return str(self.data)
