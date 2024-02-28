# Menu class
# by: James R. Brown
from file_parser import FileParser
from pathlib import Path


class Menu:

    # title for the program
    _TITLE = """
          _______  _______  _______
         |       ||       ||       |
         |    ___||  _____||    ___|
         |   |___ | |_____ |   | __
         |    ___||_____  ||   ||  |
         |   |     _____| ||   |_| |
         |___|    |_______||_______|

         """

    def __init__(self):
        self.running = True
        self.data = None

    def run_menu(self):
        """

        Calls the display, gets menu selection and passes is to the
        _get_selection method.  Checks is string entered is a digit.
        Exits if user enters a 0.

        """
        print(self._TITLE)

        while self.running:
            self.print_menu()
            selection = input("Selection(0 to quit): ")

            num = self._check_numeric(selection)

            if num is not None:
                self._get_selection(num)
            else:
                print("Invalid input, please try again...")

    def print_menu(self):
        # print terminal menu
        menu = """
            1. Read a CSV file
            2. Read a XML file
            3. Read a JSON file
            4. Show Data
            0. Exit
               """
        print(menu)

    def _get_selection(self, num):
        """
         gets user selection and calls run_menu_selection
        """
        file_type = 1

        try:

            match num:
                case 0:
                    self.running = False
                case 1:
                    print('Read a csv')
                    file_type = 1
                case 2:
                    print('Read an XML')
                    file_type = 3
                case 3:
                    print('Read a JSON')
                    file_type = 2
                case 4:
                    print('Data')
                case _:
                    print('Not recognized...')

            self.run_menu_selection(file_type)

        except Exception:
            print("Well things have gone wrong...")

    def run_menu_selection(self, file_type):
        # sets file path and executes the file parser
        file_path = None

        try:
            file_path = Path(input("Please enter file path: "))

            if file_path is not None:
                fp = FileParser(file_path, file_type)
                self.data = fp.parse_file()

        except Exception:
            raise Exception('Failed to run parser...')

    def _check_numeric(self, selection):
        # check if entry is a number, if so make it a int
        if selection.isnumeric():
            num = int(selection)
            return num
        else:
            raise TypeError('Enter a number...')

    def print_data(self):
        return self.data
