import discord
import re
import yatg
import markdownify

def table_converter(html: str) -> str:
    tables = re.findall(r'<table.*>.*</table>', html)
    if len(tables) == 0:
        return html
    
    for table in tables:
        ascii_table = yatg.html_2_ascii_table(html_content=table, output_style="orgmode")
        html = html.replace(table, "```" + ascii_table + "```")
    return html

def to_markdown(html: str) -> str:
    html = table_converter(html)
    html = html.replace("<span", "\t|\t<span")
    md = markdownify.markdownify(html=html)
    return md

def foure_embed(data):
    title = data.get('Name')
    description = to_markdown(data.get('description'))
    source = description.split("Published in ")[-1]
    description = description.split("Published in ")[0]
    if len(description) > 2000:
        description = description[:2000] + "... (too long)"
    url = "https://www.dyasdesigns.com/dnd4e/?view={}".format(data.get('iws_id'))
    embed = discord.Embed(title=title, url=url, description=description)
    embed.set_footer(text=source)

    return embed

