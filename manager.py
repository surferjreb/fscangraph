"""
    class Manager
    This class manages the execution of the program
    @author: James R. Brown
"""

from pathlib import Path
from data_operator import DataOperator
from data import Data
from menu import Menu
from file_parser import FileParser


class Manager:
    def __init__(self):
        self.running = True
        self.data = Data()
        self.dop = DataOperator(self.data)
        self.menu = Menu()

    def run_menu(self):
        """
        Displays title screen, gets menu selection.
        Exits if user enters a 0.
        """
        try:

            print(self.menu.get_title())

            while self.running:
                print(self.menu.get_menu())

                selection = int(input("\tSelection (0 to quit): "))

                self._run_menu_selection(selection)

        except ValueError:
            print('Invalid menu selection, please try again.')
            self.run_menu()
        except Exception:
            print('Hold On! Things have gone sideways...\nMenu failed')

    def _run_menu_selection(self, selection):
        """
         sets file path and executes the file parser
        """
        file_path = None
        file_type = None

        match selection:
            case 0:
                self.running = False
            case 1:
                print('\nRead a csv file')
                file_type = selection
            case 2:
                print('\nRead a JSON File')
                file_type = selection
            case 3:
                print('\nRead a XML File')
                file_type = selection
            case 4:
                # TODO: print the file data that is read in
                print(f'\n{self.dop.get_all()}\n')
            case 5:
                # TODO: output the file data in a format the users requests
                pass
            case 6:
                # TODO: Display column names, if any...
                pass
            case 7:
                # TODO: Display column values requested by column name?
                pass
            case 8:
                # TODO: Search column for value?
                pass
            case _:
                return

        if file_type is not None:
            new_path = input("\nPlease enter file path: ")
            file_path = Path(new_path)
            fp = FileParser(file_path, file_type)
            self.data.set_data(Data(fp.parse_file()))

    def __repr__(self):
        return "the Manager!"


"""
    def _check_numeric(self, selection):
        # check if entry is a number, if so make it a int
        if selection.isnumeric():
            num = int(selection)
            return num
        else:
            raise TypeError('Enter a menu choice please...')
"""
