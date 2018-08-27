from discord.ext.commands import Bot
from config import TOKEN, PREFIX
import random

client = Bot(command_prefix = PREFIX)

async def count_successes(raw_dice):
    await sum([1 if die >= 8 else 0 for die in raw_dice])

async def roll(pool):
    raw_dice = []
    counter = 0
    if pool > 0:
        while counter < pool:
            next_die = random.randint(1, 10)
            if next_die != 10:
                counter += 1
            raw_dice.append(next_die)
        await f"{count_successes(raw_dice)} successes ({raw_dice})"
    else:
        await f"{random.randint(1,10)} on a chance die"

client.run(TOKEN)