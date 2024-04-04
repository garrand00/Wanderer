import os
from dotenv import load_dotenv

from tools.fetch_data import fetch_data
from tools.data_helper import rebuild_json

# Links
load_dotenv('.env')
base_url = os.getenv("EH_BASE_URL")

archetype_url = base_url + "Archetype"
class_url = base_url + "Class"
background_url = base_url + "Background"
plan_url = base_url + "Plans"
talent_url = base_url + "Talents"
feat_url = base_url + "Feats"
rule_url = base_url + "Rules"
profession_url = base_url + "Profession"
companion_url = base_url + "Companions"

# Get Data
archetype_data = fetch_data(archetype_url)
archetype_data = rebuild_json(archetype_data)

class_data = fetch_data(class_url)
class_data = rebuild_json(class_data)

background_data = fetch_data(background_url)
background_data = rebuild_json(background_data)

plan_data = fetch_data(plan_url)
plan_data = rebuild_json(plan_data)

talent_data = fetch_data(talent_url)
talent_data = rebuild_json(talent_data)

feat_data = fetch_data(feat_url)
feat_data = rebuild_json(feat_data)

rule_data = fetch_data(rule_url)
rule_data = rebuild_json(rule_data)

profession_data = fetch_data(profession_url)
profession_data = rebuild_json(profession_data)

companion_data = fetch_data(companion_url)
companion_data = rebuild_json(companion_data)