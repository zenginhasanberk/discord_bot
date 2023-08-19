import os
import json
from settings import *
import random
from discord.ext import commands

def mods_or_owner():
    def predicate(ctx):
        return commands.check_any(commands.is_owner(), commands.has_role(MODERATOR_ROLE_NAME))
    return commands.check(predicate)

async def get_momma_jokes():
    with open(os.path.join((DATA_DIR), "jokes.json"), encoding="utf8") as joke_file:
        jokes = json.load(joke_file)
        random_category = random.choice(list(jokes.keys()))
        insult = random.choice(list(jokes[random_category]))
        return insult