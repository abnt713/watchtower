from .base import *
from colorama import Fore


class TutorialState(State):

    def run(self, arguments={}):
        print()
        print_data("Watchtower", Fore.MAGENTA)
        print_data("- The last stand against the unknow", Fore.CYAN)
        print()
        print()

        print_data("Welcome, hunter. Press enter to continue at any point")
        print_data("It is important to keep track of the creatures you "
                   "discover")
        print_data("Use a simple notebook or sheet of paper to keep track"
                   "of the creatures you will find")
        print_data("Use the codex to find out more about that creature")
        print()

        input("Press enter to continue...")
        print_data("Texts highlited in", end='')
        print_data("red", Fore.RED, end='')
        print_data("are options. You can enter them as input")

        print()

        input("Press enter to continue...")
        return 'new_case', {}
