# Menu class
# by: James R. Brown

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


    def run_menu(self):
        """

        Calls the display, gets menu selection and passes is to the
        _get_selection method.  Checks is string entered is a digit.
        Exits if user enters a 0.

        """
        print('menu started')

        while self.running:
            self.print_menu()

            selection = input("Selection(0 to quit): ")

            num = self._check_numeric(selection)

            if num > 0:
                self._get_selection(num)
            else:
                self.running = False

    def print_menu(self):
        print(self._TITLE)
        print("Menu displayed here")

    def _get_selection(self, num):

        match num:
            case 1:
                print(1)
            case 2:
                print(2)
            case 3:
                print(3)
            case 4:
                print(4)
            case _:
                print('Not recognized')

    def _check_numeric(self, selection):
        try:
            num = int(selection)
            return num
        except ValueError:
            print("Please enter a valid menu selection.")
