import importlib
import os

ELEMENTS = ['fire', 'water', 'wind', 'earth']
SPECIES = ['undead']


class CreatureVessel(object):

    def __init__(self, species, element):
        self.species = self.load_aspect('species', species)
        self.element = self.load_aspect('elements', element)

        self.health = self.species['health']
        self.block = self.species['block']

    def load_aspect(self, package, item):
        module = importlib.import_module('.%s.%s' % (package, item), 'tower')
        return module.exports

    def get_species(self):
        return self.species

    def get_element(self):
        return self.element
