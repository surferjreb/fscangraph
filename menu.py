"""
 Menu class
 A class for displaying the menu in command prompt and retrieving users
 selection.
 @author: James R. Brown
"""


class Menu:

    # title graphic for the program
    _TITLE = """
          _______  _______  _______
         |       ||       ||       |
         |    ___||  _____||    ___|
         |   |___ | |_____ |   | __
         |    ___||_____  ||   ||  |
         |   |     _____| ||   |_| |
         |___|    |_______||_______|

         """
    # menu that is displayed
    _MENU = """
            1. Read a CSV file
            2. Read a JSON file
            3. Read a XML file
            4. Show Data
            0. Exit
            """

    def __init__(self):
        pass

    def get_menu(self):
        """
         return menu str
        """
        return str(self._MENU)

    def get_title(self):
        """
         retrun graphic title
        """
        return str(self._TITLE)
