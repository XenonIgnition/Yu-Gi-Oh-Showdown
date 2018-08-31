"""
Company: XenonT
Author: Adesina Bros
Date: 16/07/2018
Script: Formats.py


This module will house all the information pertaining to all the formats that will be available
for Yu-Gi-Oh Showdown.
"""

import json

class FormatManager:
    """
    Holds the information regarding the formats that will be used in Yu-Gi-Oh Showdown.
    """

    def __init__(self):
        pass


format_dict = [
    # GENERATION
    {
        "section": "Generations"
    },
    {
        "sub-section": "Vrains",
     },
    {
        "name": "[Gen 6] Ranked Random Battle",
        "desc": "Randomized deck of cards pertaining to a competitively viable meta/offmeta deck"
                "May add filter to choose meta/offmeta archetype.",
        "threads": [""],
        "rated": True,
        "mod": "genVrains",
        "team": "random",
        "ruleset":["ranked"],
        "banlist":["latest"]
    },
    {
        "name": "[Gen 6] Unranked Random Battle",
        "desc": "Randomized deck of cards pertaining to a competitively viable meta/offmeta deck"
                "May add filter to choose meta/offmeta archetype." "Unranked",
        "threads": [""],
        "rated": False,
        "challengeShow": False,
        "mod": "genVrains",
        "team": "random",
        "ruleset":["unranked"],
        "banlist":["latest", "custom"]
    },
    {
        "name": "[Gen 6] Ranked Battle",
        "desc": "Use user's deck of cards to participate in a rated battle",
        "threads": [""],
        "rated": True,
        "mod": "genVrains",
        "team": "random",
        "ruleset":["ranked"],
        "banlist":["latest"]
    },
    {
        "sub-section": "Arc-V"
    },
    {
        "name": "[Gen 5] Ranked Random Battle",
        "desc": "Randomized deck of cards pertaining to a competitively viable meta/offmeta deck featuring "
                "May add filter to choose meta/offmeta archetype.",
        "threads": [""],
        "rated": True,
        "mod": "genArc",
        "team": "random",
        "ruleset":["ranked"],
        "banlist":["arcv", "chains"]
    },
    {
        "name": "[Gen 5] Unranked Random Battle",
        "desc": "Randomized deck of cards pertaining to a competitively viable meta/offmeta deck featuring "
                "May add filter to choose meta/offmeta archetype." "Unranked",
        "threads": [""],
        "rated": False,
        "mod": "genArc",
        "team": "random",
        "ruleset":["unranked"],
        "banlist":["arcv", "chains", "custom"]
    },
    {
        "name": "[Gen 5] Ranked Battle",
        "desc": "Use user's deck of cards to participate in a rated battle",
        "threads": [""],
        "rated": True,
        "mod": "genArc",
        "team": "set",
        "ruleset":["ranked"],
        "banlist":["arcv", "chains"]
    },
    {
        "sub-section": "Zexal"
    },
    {
        "name": "[Gen 4] Ranked Random Battle",
        "desc": "Randomized deck of cards pertaining to a competitively viable meta/offmeta deck featuring "
                "May add filter to choose meta/offmeta archetype.",
        "threads": [""],
        "rated": True,
        "mod": "genZexal",
        "team": "random",
        "ruleset":["ranked"],
        "banlist":["arcv", "pendulums", "chains"]
    },
    {
        "name": "[Gen 4] Unranked Random Battle",
        "desc": "Randomized deck of cards pertaining to a competitively viable meta/offmeta deck featuring "
                "May add filter to choose meta/offmeta archetype." "Unranked",
        "threads": [""],
        "rated": False,
        "mod": "genZexal",
        "team": "random",
        "ruleset":["unranked"],
        "banlist":["arcv", "chains", "pendulums", "custom"]
    },
    {
        "name": "[Gen 4] Ranked Battle",
        "desc": "Use user's deck of cards to participate in a rated battle",
        "threads": [""],
        "rated": True,
        "mod": "genZexal",
        "team": "set",
        "ruleset":["ranked"],
        "banlist":["arcv", "pendulums", "chains"]
    },
    {
        "sub-section": "5Ds"
    },
    {
        "name": "[Gen 3] Ranked Random Battle",
        "desc": "Randomized deck of cards pertaining to a competitively viable meta/offmeta deck featuring "
                "May add filter to choose meta/offmeta archetype.",
        "threads": [""],
        "rated": True,
        "mod": "gen5ds",
        "team": "random",
        "ruleset":["ranked"],
        "banlist":["arcv", "pendulums", "chains", "xyz"]
    },
    {
        "name": "[Gen 3] Unranked Random Battle",
        "desc": "Randomized deck of cards pertaining to a competitively viable meta/offmeta deck featuring "
                "May add filter to choose meta/offmeta archetype." "Unranked",
        "threads": [""],
        "rated": False,
        "mod": "gen5ds",
        "team": "random",
        "ruleset":["unranked"],
        "banlist":["arcv", "chains", "pendulums", "custom", "xyz"]
    },
    {
        "name": "[Gen 3] Ranked Battle",
        "desc": "Use user's deck of cards to participate in a rated battle",
        "threads": [""],
        "rated": True,
        "mod": "gen5ds",
        "team": "set",
        "ruleset":["ranked"],
        "banlist":["arcv", "pendulums", "chains", "xyz"]
    },
    {
        "sub-section": "GX"
    },
    {
        "name": "[Gen 2] Unranked Random Battle",
        "desc": "Randomized deck of cards pertaining to a competitively viable meta/offmeta deck featuring "
                "May add filter to choose meta/offmeta archetype." "Unranked",
        "threads": [""],
        "rated": False,
        "mod": "genGX",
        "team": "random",
        "ruleset":["unranked"],
        "banlist":["arcv", "chains", "pendulums", "custom", "xyz", "synchro"]
    },
    {
        "name": "[Gen 2] Ranked Battle",
        "desc": "Use user's deck of cards to participate in a rated battle",
        "threads": [""],
        "rated": True,
        "mod": "genGX",
        "team": "set",
        "ruleset":["ranked"],
        "banlist":["arcv", "pendulums", "chains", "xyz", "synchro"]
    },
    {
        "sub-section": "Original"
    },
    {
        "name": "[Gen 1] Unranked Random Battle",
        "desc": "Randomized deck of cards pertaining to a competitively viable meta/offmeta deck featuring "
                "May add filter to choose meta/offmeta archetype." "Unranked",
        "threads": [""],
        "rated": False,
        "mod": "gen1",
        "team": "random",
        "ruleset":["unranked"],
        "banlist":["arcv", "chains", "pendulums", "custom", "xyz", "synchro", "gx"]
    },
    {
        "name": "[Gen 1] Ranked Battle",
        "desc": "Use user's deck of cards to participate in a rated battle",
        "threads": [""],
        "rated": True,
        "mod": "gen1",
        "team": "set",
        "ruleset":["ranked"],
        "banlist":["arcv", "pendulums", "chains", "xyz", "synchro", "gx"]
    },
]

print(format_dict)
