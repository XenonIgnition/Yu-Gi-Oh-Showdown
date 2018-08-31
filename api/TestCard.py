"""

"""

import api.GlobalMethods as glob
import json

rand_monster_card = '3-Hump Lacooda'
rand_spell_card = '"A" Cell Scatter Burst'
rand_trap_card = '"A" Cell Breeding Device'

card = glob.fetchCardAPI(rand_monster_card)
print(json.dumps(card, indent=4, sort_keys=True))
