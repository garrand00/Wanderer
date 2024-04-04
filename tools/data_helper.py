import discord
import asyncio

def rebuild_json(data):
    """
    Rebuilds a list of dictionaries into a dictionary for name-based access.

    Args:
        data (list): List of dictionaries with a 'Name' key.

    Returns:
        dict: Dictionary with names as keys and corresponding dictionaries as values.
    """
    rebuild = {}

    for item in data:
        name = item.get('Name')
        if name:
            rebuild[name] = item
    return rebuild

def search_name(keyword, data):
    keyword = keyword.lower()
    items = list(data.keys())
    results = []
    results_data = {}

    # Check if there's an exact match
    for item in items:
        if keyword == item.lower():
            results.append(item)

    if len(results) > 0:
        results_data[results[0]] = data.get(results[0])
        return results_data
    
    # Check of a list of similar words for the user to choose
    for item in items:
        if keyword in item.lower():
            results.append(item)

    results.sort(key=lambda x: (
        1 if x.lower() == keyword.lower() else 
        2 if x.lower().startswith(keyword.lower()) else 
        4 if x.lower().endswith(keyword.lower()) else 
        3
    ))

    if len(results) > 0:
        idx = 10 if len(results) > 10 else len(results)

        for n in range(idx):
            results_data[results[n]] = data.get(results[n])

        return results_data

    # If there are no matches, it will return nothing

async def search_command_builder(self, ctx, keyword, data, embed_function):
    result = search_name(keyword, data)
    if result == None:
        await ctx.send("No results found.")
    elif len(result) == 1:
        result_data = next(iter(result.values()))

        embed = embed_function(result_data)
        await ctx.send(embed=embed)
    else:
        options = ""
        
        for key in result.keys():
            options = options + f"1. `{key}`\n"

        # Followup Message
        def followup(message):
            return (
                message.content.isnumeric() or message.content == "c"
            ) and message.author == ctx.message.author
        
        # Followup embed
        description = """Do you mean?\n{}""".format(options)
        embed = discord.Embed(title="Multiple Found", description=description)
        embed.set_footer(text="Type 1-10 to choose, or c to cancel.")

        # Wait for Message 
        option_message = await ctx.send(embed=embed)
        try:
            followup_message = await self.bot.wait_for(
                "message", timeout=60.0, check=followup
            )

        # Timeout
        except asyncio.TimeoutError:
            await option_message.delete()
            await ctx.send("Time Out")

        # Message option
        else:
            if followup_message.content == "c":
                await option_message.delete()
                await followup_message.delete()
                return

            chosen_data = list(result.values())[int(followup_message.content)-1]

            embed = embed_function(chosen_data)
            await ctx.send(embed=embed)



        