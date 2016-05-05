from .base import *
from colorama import Fore
import Pyro4


class BattleState(State):

    def run(self, arguments={}):
        case_id = arguments['case_id']
        watchtower = arguments['watchtower']
        keep_going = True
        rounds = 0
        print()
        print()
        print_data("< BATTLE START >", Fore.MAGENTA)
        print()
        while keep_going:
            rounds += 1
            player_lives, enemy_lives = watchtower.get_lives(case_id)
            if player_lives == 0:
                print()
                print_data('The player was defeated', Fore.RED)
                keep_going = False
                continue

            if enemy_lives == 0:
                print()
                print_data('The evil being was defeated', Fore.CYAN)
                keep_going = False
                continue
            print()
            print()
            print()
            print_data("< Round %d >" % rounds, Fore.MAGENTA)
            print()
            print_data("Player HP: %d" % player_lives)
            print_data("Enemy HP: %d" % enemy_lives)
            print()

            print_data("Select your attack", Fore.CYAN)
            print("*", end='')
            print_data("Melee", Fore.RED)
            print("*", end='')
            print_data("Arcane", Fore.RED)
            print("*", end='')
            print_data("Prayer", Fore.RED)

            print_data("Type your attack below")
            print()
            attack = input("")
            result = watchtower.start_attack(case_id, attack.lower())

            print()
            print_data("Player used %s" % result['player'],
                       Fore.CYAN)
            print_data("Enemy used %s" % result['enemy'],
                       Fore.LIGHTRED_EX)
            print()

            result = watchtower.check_impact(case_id)
            print_data(result)

            attack = watchtower.get_current_attack(case_id)
            if attack['has_draw']:
                print()
                input("Press enter to continue...")
                print()
                continue

            print_data('Player has a %d%% '
                       'chance to hit' % attack['hit_chance'])
            print()
            input("Press enter to continue...")
            print()
            player_hit = watchtower.roll_hit(case_id)
            print_data('Player has rolled a %d / %d' % (player_hit,
                                                        attack['hit_chance']))
            if watchtower.try_hit(case_id):
                print_data("Player attack WORKED!", Fore.CYAN)
                print_data("Evil being loses 1 health point!", Fore.CYAN)

            else:
                print_data("Player attack FAILED!", Fore.RED)
                print_data("Player let his guard open "
                           "and lost 1 health point!", Fore.RED)

            print()
            input("Press enter to continue...")
            print()

        print()
        print()

        print_data("< Battle has ended >", Fore.MAGENTA)
        print()
        input("Press enter to continue...")

        return 'ending', {}
