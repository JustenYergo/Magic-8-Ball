from console_colors import CColors


class MenuOption:
    A = 'a. Read Magic 8 Ball responses from a file'
    B = 'b. Play Magic 8 Ball'
    C = 'c. Print out responses (and their categories)'
    D = 'd. Print out responses by category'
    E = 'e. Write responses to a file'
    F = 'f. Add responses to a file'
    G = 'g. Exit'


class Menu:

    def __init__(self):
        self._menus = f"""{CColors.MENU + CColors.BOLD} ______________________________Magic8Ball_____________________________________
        {MenuOption.A}
        {MenuOption.B}
        {MenuOption.C}
        {MenuOption.D}
        {MenuOption.E}
        {MenuOption.F}
        {MenuOption.G}
_______________________________________________________________________________{CColors.ENDC}"""
        self._menu_map = {
            'a': MenuOption.A,
            'b': MenuOption.B,
            'c': MenuOption.C,
            'd': MenuOption.D,
            'e': MenuOption.E,
            'f': MenuOption.F,
            'g': MenuOption.G
        }

        self._selected_menu = None

    def _display_menu(self):
        print(self._menus)

        property

    def get_selected_menu(self):
        return self._selected_menu

    def select(self, user=''):
        self._selected_menu = None
        while (not self._selected_menu) and (not isinstance(self._selected_menu, MenuOption)):
            self._display_menu()
            get_selected_menu = str(input("Select a menu option: ")).lower()
            if get_selected_menu not in self._menu_map.keys():
                print('\n')
                print(f"{CColors.WARNING}Selected menu option doesnt exist. Please try again!{CColors.ENDC}")
                print('\n')
                continue
            self._selected_menu = self._menu_map[get_selected_menu]
            return self._selected_menu


menu = Menu()
