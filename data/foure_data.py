import os
from dotenv import load_dotenv

from tools.fetch_data import fetch_data
from tools.data_helper import rebuild_json

# Links
load_dotenv('.env')
base_url = os.getenv("FE_BASE_URL")

glossary_url = base_url + "Glossary" 
race_url = base_url + "Race"
background_url = base_url + "Background"
theme_url = base_url + "Theme"
class_url = base_url + "Class"
paragon_url = base_url + "ParagonPath"
epic_url = base_url + "EpicDestiny"
power_url = base_url + "Power"
feat_url = base_url + "Feat"
ritual_url = base_url + "Ritual"
item_url = base_url + "Item"
weapon_url = base_url + "Weapon"
implement_url = base_url + "Implement"
armor_url = base_url + "Armor"
companion_url = base_url + "Companion"
deity_url = base_url + "Deity"
poison_url = base_url + "Poison"
disease_url = base_url + "Disease"
monster_url = base_url + "Monster"
trap_url = base_url + "Trap"

# Get Data
glossary_data = fetch_data(glossary_url)
glossary_data = rebuild_json(glossary_data)

race_data = fetch_data(race_url)
race_data = rebuild_json(race_data)

background_data = fetch_data(background_url)
background_data = rebuild_json(background_data)

theme_data = fetch_data(theme_url)
theme_data = rebuild_json(theme_data)

class_data = fetch_data(class_url)
class_data = rebuild_json(class_data)

paragon_data = fetch_data(paragon_url)
paragon_data = rebuild_json(paragon_data)

epic_data = fetch_data(epic_url)
epic_data = rebuild_json(epic_data)

power_data = fetch_data(power_url)
power_data = rebuild_json(power_data)

feat_data = fetch_data(feat_url)
feat_data = rebuild_json(feat_data)

ritual_data = fetch_data(ritual_url)
ritual_data = rebuild_json(ritual_data)

item_data = fetch_data(item_url)
item_data = rebuild_json(item_data)

weapon_data = fetch_data(weapon_url)
weapon_data = rebuild_json(weapon_data)

implement_data = fetch_data(implement_url)
implement_data = rebuild_json(implement_data)

armor_data = fetch_data(armor_url)
armor_data = rebuild_json(armor_data)

companion_data = fetch_data(companion_url)
companion_data = rebuild_json(companion_data)

deity_data = fetch_data(deity_url)
deity_data = rebuild_json(deity_data)

poison_data = fetch_data(poison_url)
poison_data = rebuild_json(poison_data)

disease_data = fetch_data(disease_url)
disease_data = rebuild_json(disease_data)

monster_data = fetch_data(monster_url)
monster_data = rebuild_json(monster_data)

trap_data = fetch_data(trap_url)
trap_data = rebuild_json(trap_data)