from responses import Responses as responses
from magic8 import Magic8 as magic8
from menu import menu
from menu import MenuOption
from console_colors import CColors

class GameLoop:
    def __init__(self):
        self._done = False
        self._responses_object = responses
        self._magic8_object = magic8
        self._menu_object = menu

    def run(self):
        while True:
            print('\n')
            menu.select()
            print(menu._selected_menu)
            if menu._selected_menu == MenuOption.A:
                print('\n')
                responses.get_file(self)
                responses.read(self)
                print('\n')
                input(CColors.GREEN+CColors.BOLD+CColors.UNDERLINE+"Press enter to go back to the menu"+CColors.ENDC)
            elif menu._selected_menu == MenuOption.B:
                print('\n')
                question = str(input("What do you want to ask the almighty Magic 8 Ball? "))
                magic8.shake(self)
                print('\n')
                input(CColors.GREEN+CColors.BOLD+CColors.UNDERLINE+"Press enter to go back to the menu"+CColors.ENDC)
            elif menu._selected_menu == MenuOption.C:
                print('\n')
                responses.print(self)
                print('\n')
                input(CColors.GREEN+CColors.BOLD+CColors.UNDERLINE+"Press enter to go back to the menu"+CColors.ENDC)
            elif menu._selected_menu == MenuOption.D:
                print('\n')
                responses.sort_cat(self)
                print('\n')
                input(CColors.GREEN+CColors.BOLD+CColors.UNDERLINE+"Press enter to go back to the menu"+CColors.ENDC)
            elif menu._selected_menu == MenuOption.E:
                print('\n')
                responses.write(self)
                print('\n')
                input(CColors.GREEN+CColors.BOLD+CColors.UNDERLINE+"Press enter to go back to the menu"+CColors.ENDC)
            elif menu._selected_menu == MenuOption.F:
                print('\n')
                responses.set_update(self)
                print('\n')
                input(CColors.GREEN+CColors.BOLD+CColors.UNDERLINE+"Press enter to go back to the menu"+CColors.ENDC)
            else:
                break
                
                
game = GameLoop()
