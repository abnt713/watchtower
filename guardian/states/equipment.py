from .base import *
from colorama import Fore


class EquipmentState(State):

    def run(self, arguments={}):
        case_id = arguments['case_id']
        watchtower = arguments['watchtower']

        print()
        print_data("Equipment select", Fore.MAGENTA)
        print()

        # Material
        material = self.ask_item('weapon material',
                                 watchtower.get_material_list())

        watchtower.set_material(material)
        print()

        # Place
        place = self.ask_item('place of action',
                              watchtower.get_places_list())

        watchtower.set_place(place)
        print()

        # Amulet
        amulet = self.ask_item('amulet',
                               watchtower.get_amulets_list())

        watchtower.set_amulet(amulet)
        print()

        # Potion
        potion = self.ask_item('potion',
                               watchtower.get_potions_list())

        watchtower.set_potion(potion)
        print()

        # Summoning
        summon = self.ask_item('summoning',
                               watchtower.get_summonings_list())

        watchtower.set_summoning(summon)
        print()

        # Banishment
        banishment = self.ask_item('banishment',
                                   watchtower.get_banishments_list())

        watchtower.set_banishment(banishment)
        print()
        # input("Press enter to continue...")
        print()
        return 'briefing', {
            "case_id": case_id,
            "watchtower": watchtower
        }

    def ask_item(self, item_name, item_list):
        print_data("- %s" % item_name.title(), Fore.CYAN)
        print_data("Please select one %s from the list" % item_name)
        for item in item_list:
            print_data(" * %s" % item['prefix'], end='')
            print_data("%s" % item['item'], Fore.RED)

        print_data("Type below your choice for this mission")
        chosen_material = input("")
        return chosen_material

    def open_case(self, uri):
        return Pyro4.Proxy(uri)
