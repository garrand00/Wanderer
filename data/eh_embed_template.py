import discord
from tools.embed_builder import embed_builder

def class_embed(data):
    proficiency_value = f'**Saving Throws:** {data.get("Save Throw")}\n**Skills:** {data.get("Skills")}\n**Equipment**: {data.get("Equipment")}'
    if data.get("Additional Expertise"):
        add_exp = data.get("Additional Expertise").split(':')
        add_exp_text = f'\n**{add_exp[0]} Expertise:** {add_exp[1]}'
        proficiency_value += add_exp_text
    
    equipment_value = f'**Equipment Pack:** {data.get("Equipment Pack")}\n**Weapons:** {data.get("Weapons")}\n'

    embed_data = {
    "title": data.get('Name').upper(),
    "description": f'> *{data.get("Desc")}*\n\n```{data.get("Table Code Block")}```',
    
    "footer": {
        "text": f'{data.get("Archetype")} Archetype | {data.get("Source")}',
    },
    "fields": [
        {"name": "PROFICIENCEIS",
         "value": proficiency_value,
         "inline": False},
         {"name": "EQUIPMENT RECOMMENDATION",
         "value": equipment_value,
         "inline": False}
        ],
    "author": {
        "name": "Class"
    }
    }


    embed = embed_builder(embed_data)
    
    return embed

def background_embed(data):
    embed_data = {
        "title": data.get('Name').upper(),
        "description": f'> *{data.get("Flavor")}*\n\n**Ability Score Increase:** {data.get("ASI")}\n**Skill Proficiencies:** {data.get("Skill ")}\n\n**Special Feature:** {data.get("Feature")}',
        
        "footer": {
            "text": f'{data.get("Source")}',
        },
        "author": {
            "name": "Backgrounds"
        }
    }

    embed = embed_builder(embed_data)

    return embed

def profession_embed(data):
    embed_data = {
        "title": data.get('Name').upper(),
        "description": f'> *{data.get("Flavor")}*\n> \n> *__Sample Careers:__ {data.get("Sample Career")}*\n\n**Ability Score Increase:** {data.get("ASI")}\n**Skill Proficiencies:** {data.get("Skill ")}\n**Iconic Equipment:** {data.get("Iconic")}\n**Wealth Level:** {data.get("Wealth")}\n\n**Special Feature:** {data.get("Feature")}',
        
        "footer": {
            "text": f'{data.get("Source")}',
        },
        "author": {
            "name": "Professions"
        }
    }

    embed = embed_builder(embed_data)

    return embed

def plan_embed(data):
    embed_data = {
        "title": data.get('Name').upper(),
        "description": data.get("Content"),
        
        "footer": {
            "text": f'{data.get("Archetype")} Plans | {data.get("Source")}',
        },
        "author": {
            "name": "Plans"
        },"fields": [
        {"name": "Level 3",
         "value": data.get("Level 3"),
         "inline": False},
         {"name": "Level 5",
         "value": data.get("Level 5"),
         "inline": False},
         {"name": "Level 7",
         "value": data.get("Level 7"),
         "inline": False},
         {"name": "Level 9",
         "value": data.get("Level 9"),
         "inline": False},
        ]
    }

    if data.get("Image"):
        embed_data["image_url"] = data.get("Image")

    embed = embed_builder(embed_data)

    return embed

def archetype_embed(data):
    embed_data = {
        "title": f'{data.get("Name").upper()} HERO',
        "description": f'> *{data.get("Flavor")}*\n\n ```{data.get("Table")}```\n**Hit Dice:** {data.get("Hit Dice")}\n**Starting Hit Points:** {data.get("Start HP")}\n** Hit Points at Higher Levels:** {data.get("Level HP")}\n**Defense ({data.get("Defense Type")}):** {data.get("Defense")}',
        
        "footer": {
            "text": data.get("Source"),
        },
        "author": {
            "name": "Archetype"
        }
    }

    embed = embed_builder(embed_data)

    return embed

def talent_embed(data):
    footer_text = ""

    if data.get("Class"):
        footer_text += f'{data.get("Class")} Classs | '

    if data.get("Archetype"):
        footer_text += f'{data.get("Archetype")} Archetype | '

    footer_text += data.get("Source")

    embed_data = {
        "title": data.get('Name').upper(),
        "description": f'**Level {data.get("Level")}**\n\n{data.get("Content")}',
        
        "footer": {
            "text": footer_text,
        },
        "author": {
            "name": "Talent"
        }
    }

    embed = embed_builder(embed_data)

    return embed

def feat_embed(data):
    embed_data = {
        "title": data.get('Name').upper(),
        "description": data.get('Content'),
        
        "footer": {
            "text": f'{data.get("Subtype")} Feats | {data.get("Source")}',
        },
        "author": {
            "name": f'{data.get("Type")} Feat'
        }
    }

    embed = embed_builder(embed_data)

    return embed

def rule_embed(data):
    return 0

def companion_embed(data):
    return 0