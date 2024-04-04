import discord 

embed_json = {
    "title": "",
    "description": "",
    "url": None,
    "colour": "",
    "timestamp": "",
    "image_url": "",
    "thumbnail_url": "",
    "author": {
        "name": "",
        "url": "",
        "icon_url": ""
    },
    "footer": {
        "text": "",
        "icon_url": ""
    },
    "fields": [
        {"name": "",
         "value": "",
         "inline": True},
         {"name": "",
         "value": "",
         "inline": True}
    ],
}

def embed_builder(data):
    embed = discord.Embed(title=data.get('title'),
                          description=data.get('description'),
                          color=data.get('color') ,
                          url=data.get('url'),
                          timestamp=data.get('timestamp'),
                          )

    author_data = data.get('author')
    if author_data:
        embed.set_author(name=author_data.get('name'), 
                        url=author_data.get('url'), 
                        icon_url=author_data.get('icon_url'))
    
    if data.get('thumbnail_url'):
        embed.set_thumbnail(url=data.get('thumbnail_url'))
    
    if data.get('image_url'):
        embed.set_image(url=data.get('image_url'))
    
    fields_data = data.get('fields')
    if fields_data:
        for field in fields_data:
            if field.get('name') and field.get('value'):
                embed.add_field(name=field.get('name'), 
                                value=field.get('value'), 
                                inline=field.get('inline'))
    
    footer_data = data.get('footer')
    if footer_data:
        embed.set_footer(text=footer_data.get('text'), 
                        icon_url=footer_data.get('icon_url'))
    
    return embed