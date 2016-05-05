from .base import *
from colorama import Fore
import Pyro4


class NewCaseState(State):

    def run(self, arguments={}):
        print()
        print()
        print()
        print_data("< INCOMING CASE >")

        print()
        print_data("This is Watchtower supernatural contenance task force")
        print_data("Please inform your server uri to continue")
        server_uri = input("")

        print()
        print_data("Estabilishing connection...")
        watchtower = self.open_case(server_uri)
        print_data("Connected...")

        print()
        input("Press enter to continue...")
        print()

        case_id = watchtower.start_case()
        print_data("Ocurrence ID #%d" % case_id)
        print_data("A new case of murder has been detected. A suspicious "
                   "creature was spotted in the crime scene")
        print_data("Please start the preparations for the purge immediately")

        print()
        input("Press enter to continue...")
        print()

        print_data("There are the clues the investigation team collected")
        print_data("Clues and tips", Fore.CYAN)

        clues = watchtower.search_clues(case_id)
        for clue in clues:
            print_data("  - %s" % clue, Fore.MAGENTA)

        print()
        input("Press enter to continue...")
        return 'equipment', {
            "case_id": case_id,
            "watchtower": watchtower
        }

    def open_case(self, uri):
        return Pyro4.Proxy(uri)
