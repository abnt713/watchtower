from .creature import SPECIES, ELEMENTS, CreatureVessel
from .utils import StartEndChance, PercentageChance
from .utils.enemygen import EnemyGenerator
from .traces import get_trace_description
from .assets import *


class Watchtower(object):

    def __init__(self):
        self.cases = []
        self.material = None
        self.place = None
        self.amulet = None
        self.place = None
        self.summoning = None
        self.banishment = None

    def start_case(self):
        selected_species_index = StartEndChance(0, len(SPECIES) - 1).roll()
        species = SPECIES[selected_species_index]

        selected_element_index = StartEndChance(0, len(ELEMENTS) - 1).roll()
        element = ELEMENTS[selected_element_index]

        creature = CreatureVessel(species, element)
        self.cases.append(Case(creature))

        return len(self.cases) - 1

    def search_clues(self, case_index):
        case = self.cases[case_index]
        creature = case.creature

        species = creature.get_species()
        element = creature.get_element()
        traces = []
        for trace_type in species['traces']:
            this_type_traces = species['traces'][trace_type]
            selected_trace = StartEndChance(0,
                                            len(this_type_traces) - 1).roll()
            traces.append(get_trace_description(
                this_type_traces[selected_trace]
            ))

        selected_trace = StartEndChance(0,
                                        len(element['traces']) - 1).roll()
        traces.append(get_trace_description(
            element['traces'][selected_trace]
        ))

        return traces

    def start_attack(self, case_id, attack):
        case = self.cases[case_id]

        if case.current_attack is None:
            case.current_attack = Attack()
        elif case.current_attack.has_draw:
            case.current_attack = Attack()

        case.current_attack.player_attack = attack
        attacks = ['melee', 'arcane', 'prayer']
        counter = StartEndChance(0, len(attacks) - 1).roll()

        case.current_attack.enemy_attack = attacks[counter]
        return {
            "player": case.current_attack.player_attack,
            "enemy": case.current_attack.enemy_attack
        }

    def check_impact(self, case_id):
        case = self.cases[case_id]
        attack = case.current_attack.player_attack
        counter = case.current_attack.enemy_attack
        sucess = False
        if attack == 'melee':
            if counter == 'arcane':
                success = False
                # return self.try_hit(case_id,
                #                     case.opponent.hit - case.opponent.block)
            elif counter == 'prayer':
                success = True
                # return self.try_hit(case_id,
                #                     case.opponent.hit)
            elif counter == 'melee':
                success = None

        if attack == 'arcane':
            if counter == 'prayer':
                success = False
            elif counter == 'melee':
                success = True
            elif counter == 'arcane':
                success = None

        if attack == 'prayer':
            if counter == 'melee':
                success = False
                # return self.try_hit(case_id,
                #                     case.opponent.hit - case.opponent.block)
            elif counter == 'arcane':
                success = True
                # return self.try_hit(case_id,
                #                     case.opponent.hit)
            elif counter == 'prayer':
                success = None

        if success is None:
            case.current_attack.has_draw = True
            return "It's a draw. Try again"
        elif success is False:
            op = case.opponent
            case.current_attack.hit_chance = op.hit - op.block
            return 'The enemy blocked your attack!'
        elif success is True:
            case.current_attack.hit_chance = case.opponent.hit
            return 'The enemy is defenseless against your attack!'

    def get_current_attack(self, case_id):
        case = self.cases[case_id]
        return {
            "has_draw": case.current_attack.has_draw,
            "player_attack": case.current_attack.player_attack,
            "enemy_attack": case.current_attack.enemy_attack,
            "hit_chance": case.current_attack.hit_chance,
            "given_hit_chance": case.current_attack.given_hit_chance,
            "result": case.current_attack.result
        }

    def roll_hit(self, case_id):
        case = self.cases[case_id]
        given_hit = PercentageChance(
            case.current_attack.hit_chance).roll_for_number()

        case.current_attack.given_hit_chance = given_hit
        return given_hit

    def try_hit(self, case_id):
        case = self.cases[case_id]
        ca = case.current_attack
        if ca.hit_chance > ca.given_hit_chance:
            case.opponent.health -= 1
            case.current_attack = None
            return True
        else:
            case.current_attack = None
            case.player_health -= 1
            return False

    # def set_win(case_id):
    #     case = self.cases[case_id]
    #     case.opponent.health -= 1
    #
    # def set_lose(case_id):
    #     case = self.cases[case_id]
    #     case.player_health -= 1

    def get_lives(self, case_id):
        case = self.cases[case_id]
        return case.player_health, case.opponent.health

    def get_material_list(self):
        return self.get_equip_list(MATERIALS)

    def get_places_list(self):
        return self.get_equip_list(PLACES)

    def get_amulets_list(self):
        return self.get_equip_list(AMULETS, "Amulet of")

    def get_potions_list(self):
        return self.get_equip_list(POTIONS, "Potion of")

    def get_summonings_list(self):
        return self.get_equip_list(SUMMONINGS, "Summon by")

    def get_banishments_list(self):
        return self.get_equip_list(BANISHMENTS, "Banish by")

    def get_equip_list(self, res_list, prefix=""):
        items = []
        for item in res_list:
            items.append({
                "item": item,
                "prefix": prefix
            })
        return items

    def set_material(self, material):
        self.material = material

    def set_place(self, place):
        self.place = place

    def set_amulet(self, amulet):
        self.amulet = amulet

    def set_potion(self, potion):
        self.potion = potion

    def set_summoning(self, summoning):
        self.summoning = summoning

    def set_banishment(self, banishment):
        self.banishment = banishment

    def generate_choices(self):
        return {
            "materials": self.material,
            "places": self.place,
            "amulets": self.amulet,
            "potions": self.potion,
            "summonings": self.summoning,
            "banishments": self.banishment
        }

    def generate_opponent(self, case_id):
        case = self.cases[case_id]
        choices = self.generate_choices()
        creature = case.creature
        case.opponent = EnemyGenerator().generate_enemy(creature, choices)
        opponent = case.opponent

        return {
            "name": creature.species['name'],
            "element": creature.element['name'],
            "health": opponent.health,
            "block": opponent.block,
            "hit": opponent.hit,
            "guesses": opponent.guesses
        }


class Case(object):

    def __init__(self, creature):
        self.creature = creature
        self.opponent = None
        self.player_health = 5
        self.current_attack = None


class Attack(object):

    def __init__(self):
        self.has_draw = False
        self.player_attack = ''
        self.enemy_attack = ''
        self.hit_chance = 0
        self.given_hit_chance = 0
        self.result = ''
