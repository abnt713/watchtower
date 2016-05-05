TRACES = {
    'smell': 'A strange smell',
    'rotten_flesh': 'Rotten flesh',
    'scratches': "Scratch marks",
    'groaning': "Groaning sounds",
    'creature_dead': "Entity recognized as deceased",
    'creature_wounds': "Some wounds in the body of the entity",
    'creature_dirty': "Great amount of dirty covers the entity",
    'humanoid': "Humanoid form",
    'bites': "Bite marks",
    'dismemberment': "Missing members",

    'aquarius': "Influence of the zodiac sign Aquarius",
    'pisces': "Influence of the zodiac sign Pisces",
    'aries': "Influence of the zodiac sign Aries",
    'taurus': "Influence of the zodiac sign Taurus",
    'gemini': "Influence of the zodiac sign Gemini",
    'cancer': "Influence of the zodiac sign Cancer",
    'leo': "Influence of the zodiac sign Leo",
    'virgo': "Influence of the zodiac sign Virgo",
    'libra': "Influence of the zodiac sign Libra",
    'scorpio': "Influence of the zodiac sign Scorpio",
    'sagittarius': "Influence of the zodiac sign Sagittarius",
    'capricorn': "Influence of the zodiac sign Capricorn"
}


def get_trace_description(trace):
    global TRACES
    return TRACES[trace]
