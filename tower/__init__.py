from .creature import SPECIES, ELEMENTS, CreatureVessel
from .utils import StartEndChance
from .traces import get_trace_description


class Watchtower(object):

    def __init__(self):
        self.cases = []

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
        traces = []
        for trace_type in species['traces']:
            this_type_traces = species['traces'][trace_type]
            selected_trace = StartEndChance(0,
                                            len(this_type_traces) - 1).roll()
            traces.append(get_trace_description(
                this_type_traces[selected_trace]
            ))

        return traces


class Case(object):

    def __init__(self, creature):
        self.creature = creature
