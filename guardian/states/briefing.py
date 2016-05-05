from .base import *
from colorama import Fore
import Pyro4


class BriefingState(State):

    def run(self, arguments={}):
        case_id = arguments['case_id']
        watchtower = arguments['watchtower']
        print()
        print()
        print_data("< CHOICES BRIEFING >", Fore.MAGENTA)
        print()
        print_data("You have summoned your enemy to the battleground")
        print_data("These are the stats")

        enemy_data = watchtower.generate_opponent(case_id)
        print()

        for field, value in enemy_data.items():
            if field == 'guesses':
                continue
            print_data(field, Fore.BLUE, end='')
            print_data(value, Fore.MAGENTA)

        print()
        print_data("Choices result")
        print()
        for field, value in enemy_data['guesses'].items():
            result = "Correct"
            color = Fore.GREEN
            if not value:
                result = "Incorrect"
                color = Fore.RED

            print_data(field, Fore.BLUE, end='')
            print_data(result.title(), color)

        print()
        print_data("Commencing battle...")

        print()
        input("Press enter to continue...")
        print()

        return 'battle', {
            "case_id": case_id,
            "watchtower": watchtower
        }

    def open_case(self, uri):
        return Pyro4.Proxy(uri)
