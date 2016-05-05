import random


class PercentageChance:

    def __init__(self, chance):
        self.chance = chance

    def set_chance(self, chance):
        self.chance = chance

    def roll(self):
        selected = self.roll_for_number()
        if selected < self.chance:
            return True
        else:
            return False

    def roll_for_number(self):
        return random.randint(0, 100)


class StartEndChance:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def roll(self):
        return random.randint(self.start, self.end)
