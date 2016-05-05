from .base import *
from colorama import Fore


class EndingState(State):

    def run(self, arguments={}):
        print_data("This is the end of the journey. You are welcome "
                   "back at any time in here")
        print()
        print_data("There will be always creatures in the shadows, "
                   "waiting for an oportunity to come out")

        print()
        print_data("But when that time comes, there will always be the ones "
                   "whose light shines as bright as the sun itself")

        print()
        print_data("For there humble, nameless heroes, I pray for your "
                   "strength and for your heart.")

        print()
        print_data("May the light guide your actions. ")

        print()
        print_data("< lost connection >", Fore.MAGENTA)
        print()
        input("Press enter to continue...")
        exit()
