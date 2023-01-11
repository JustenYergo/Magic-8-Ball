from game import game
from console_colors import CColors


def main():
    print(f"""{CColors.MENU}________________________________________________________________________________

                            Welcome to Magic 8 Ball

    This game has the power to predict your future. After you press enter,
    a menu will appear. Please choose from the available menu options to
    play the game. Have fun!

________________________________________________________________________________{CColors.ENDC}""")

    input("\n" + CColors.GREEN + CColors.BOLD + CColors.UNDERLINE + "Press Enter to Enter the Game!" + CColors.ENDC)

    game.run()


main()
