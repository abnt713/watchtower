from ..creature import Enemy


class EnemyGenerator(object):

    def __init__(self):
        self.health = None
        self.block = None
        self.hit = None

    def generate_enemy(self, creature, choices):
        species = creature.get_species()

        self.health = species['health']
        self.block = species['block']
        self.hit = species['hit']
        self.guesses = {}
        aspect_type = 'materials'
        self.get_modifier(creature, aspect_type, choices[aspect_type])

        aspect_type = 'places'
        self.get_modifier(creature, aspect_type, choices[aspect_type])

        aspect_type = 'summonings'
        self.get_modifier(creature, aspect_type, choices[aspect_type])

        aspect_type = 'banishments'
        self.get_modifier(creature, aspect_type, choices[aspect_type])

        aspect_type = 'amulets'
        self.get_element_modifier(creature, aspect_type, choices[aspect_type])

        aspect_type = 'potions'
        self.get_element_modifier(creature, aspect_type, choices[aspect_type])

        return Enemy(self.health, self.block, self.hit, self.guesses)

    def get_modifier(self, creature, aspect_type, item):
        if item in creature.get_aspect_indexes(aspect_type):
            self.guesses.update({aspect_type: True})
            aspect = creature.get_aspect(aspect_type, item)
            if aspect['effect'] == 'health':
                self.health += int(aspect['power'] * -1)
            elif aspect['effect'] == 'hit':
                self.hit += int(aspect['power'])
        else:
            self.guesses.update({aspect_type: False})

    def get_element_modifier(self, creature, aspect_type, item):
        elements = creature.get_element_indexes(aspect_type)
        if item in elements:
            self.guesses.update({aspect_type: True})
            aspect = creature.get_element_aspect(aspect_type, item)
            if aspect['effect'] == 'health':
                self.health += int(creature.get_element_value(aspect_type,
                                                              'health') * -1)
            elif aspect['effect'] == 'hit':
                self.hit += int(creature.get_element_value(aspect_type, 'hit'))
        else:
            self.guesses.update({aspect_type: False})
