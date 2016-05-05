exports = {
    "name": "Undead",
    "description": "A souless body which walks among the mortals. "
                   "Hungry for flesh, no humanity",
    "block": 30,
    "health": 10,
    "hit": 60,
    "crime": "murder",
    "aspects": {
        "materials": [
            {
                "item": "copper",
                "effect": "health",
                "power": 2,
                "description": "Metal used on the coins for the ferryman. "
                               "Lower value, lower health"
            },
            {
                "item": "bronze",
                "effect": "hit",
                "power": 5,
                "description": "Metal used on the coins for the ferryman."
                               "Higher value, higher effectiveness"
            }
        ],
        "places": [
            {
                "item": "prison",
                "effect": "health",
                "power": 1,
                "description": "Undeads are basically evil "
                               "energy within empty bodies. "
                               "Prisons are natural sources of evil and "
                               "injustice. Each strike will make more damage"
            },
            {
                "item": "cemetery",
                "effect": "hit",
                "power": 15,
                "description": "Undeads are slower near places ruled by death."
                               "Attacks are more effective"
            }
        ],
        "amulets": {
            "health": 1,
            "hit": 5
        },
        "potions": {
            "health": 1,
            "hit": 5
        },
        "summonings": [
            {
                "item": "calling",
                "effect": "health",
                "power": 1,
                "description": "By calling the dead, the spirit will try to "
                               "find eternal rest. They shall perish sooner"
            },
            {
                "item": "luring",
                "effect": "hit",
                "power": 5,
                "description": "When lured, undead appears to grow hunger, "
                               "but easier to hit"
            }
        ],
        "banishments": [
            {
                "item": "burying",
                "effect": "health",
                "power": 2,
                "description": "By burying your deads, their time will finally"
                               "come. Less health for your foes"
            }
        ]
    },
    "traces": {
        "crime_scene": ['smell', 'rotten_flesh', 'scratches'],
        "witness": ['groaning', 'creature_dead', 'creature_wounds',
                    'creature_dirty', 'humanoid'],
        "victim": ['bites', 'dismemberment']
    }

}
