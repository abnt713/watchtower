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

    def get_element_indexes(self, macro):
        indexes = []
        for aspect in self.element['aspects'][macro]:
            indexes.append(aspect['item'])

        return indexes

    def get_element_aspect(self, macro, aspect):
        for listed_aspect in self.element['aspects'][macro]:
            if listed_aspect['item'] == aspect:
                return listed_aspect

    def get_element_value(self, macro, nature):
        return self.species['aspects'][macro][nature]

    def get_aspect_indexes(self, macro):
        indexes = []
        for aspect in self.species['aspects'][macro]:
            indexes.append(aspect['item'])

        return indexes

    def get_aspect(self, macro, aspect):
        for listed_aspect in self.species['aspects'][macro]:
            if listed_aspect['item'] == aspect:
                return listed_aspect

    def get_element(self):
        return self.element


class Enemy(object):

    def __init__(self, health, block, hit, guesses):
        self.health = health
        self.block = block
        self.hit = hit
        self.guesses = guesses
