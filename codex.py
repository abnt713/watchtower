import sys
from tower.creature import CreatureVessel
from tower.traces import get_trace_description
from colorama import Fore, Style


def main(element, creature_name):
    print()

    creature = CreatureVessel(creature_name, element)
    infos = creature.get_species()
    element = creature.get_element()
    vul_list = vulnerabilites(creature)
    traces_list = traces(creature)

    print(data("Name", infos['name']))
    print(data("Description", infos['description']))
    print(data("Element", element['name']))
    print()
    print(data("Block", str(infos['block']) + '%'))
    print(data("Normal Health", str(infos['health'])))
    print(data("Min Health",
               str(infos['health'] - mod_value(infos, 'health'))))
    print()
    print(data("Normal Hit chance",
               str(infos['hit']) + "%"))

    print(data("Max Hit chance",
               str(infos['hit'] + mod_value(infos, 'hit')) + "%"))
    print()
    print(data("Traces", ""))
    for trace_list in traces_list:
        print(data("- " + trace_list, "", color=Fore.BLUE))
        print()
    print()
    print(data("Vulnerabilites", ""))
    for vul in vul_list:
        print(data("- " + vul['item'], "", color=Fore.GREEN))
        print('    ' + vul['description'])
        print()


def mod_value(creature, item):
    targets = [
        'materials', 'places', 'summonings', 'banishments'
    ]
    elemental = [
        'amulets', 'potions'
    ]
    value = 0
    for target in targets:
        for modifier in creature['aspects'][target]:
            if modifier['effect'] == item:
                value = value + modifier['power']

    for element in elemental:
        value = value + creature['aspects'][element][item]

    return value


def vulnerabilites(creature):
    species = creature.get_species()
    element = creature.get_element()
    vul = []
    targets = {
        'materials': "weapon of",
        'places': "in a",
        'summonings': "summoned by",
        'banishments': "banished by"
    }
    elemental = {
        'amulets': "amulet of",
        'potions': "potion of"
    }

    for target, prefix in targets.items():
        for modifier in species['aspects'][target]:
            item = {
                "item": "%s %s" % (prefix, modifier['item']),
                "description": modifier['description']
            }
            vul.append(item)

    for element_item, prefix in elemental.items():
        for modifier in element['aspects'][element_item]:
            item = {
                "item": "%s %s" % (prefix, modifier['item']),
                "description": modifier['description']
            }
            vul.append(item)

    return vul


def traces(creature):
    species = creature.get_species()
    element = creature.get_element()
    traces = []

    for trace_type in species['traces']:
        for single_trace in species['traces'][trace_type]:
            print(single_trace)
            traces.append(get_trace_description(single_trace))

    for single_trace in element['traces']:
            traces.append(get_trace_description(single_trace))

    return traces


def data(header, info="", color=Fore.RED):
    return "%s %s%s %s" % (color, header, Fore.RESET, info)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Argument error: No creature name or element")
        exit()

    element = sys.argv[1]
    creature_name = sys.argv[2]
    main(element, creature_name)
