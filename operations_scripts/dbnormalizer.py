"""
       ____                                     ___                
  ____/ / /_  ____  ____  _________ ___  ____ _/ (_)___  ___  _____
 / __  / __ \/ __ \/ __ \/ ___/ __ `__ \/ __ `/ / /_  / / _ \/ ___/
/ /_/ / /_/ / / / / /_/ / /  / / / / / / /_/ / / / / /_/  __/ /    
\__,_/_.___/_/ /_/\____/_/  /_/ /_/ /_/\__,_/_/_/ /___/\___/_/     
                                                                   
Make normalizations about data.
"""
import asyncpg, asyncio, click, copy
from tqdm import tqdm
from pprint import pprint

connection_options = {
    "user":"enem",
    "password":"catapimbas",
    "port":5432,
    "max_size":20,
    "min_size":20,
}
async def get_connection_pool(**options):
    return await asyncpg.create_pool(**options)
def gcs(cmd):
    for line in cmd.split("\n"):
        if line.startswith("INSERT"):
            return line.split("(")[0]
    return None
get_commands = lambda sql_script: [
    (
        "TRUNCATE" if "TRUNCATE" in command else gcs(command),
        command,
    )
    for command in map(lambda x: x + ";", sql_script.split(";"))
]

def show(cmds):
    click.clear()
    print("Remains: ")
    pprint([c[0] for c in cmds["remains"]])
    print("Processing: ")
    pprint([c[0] for c in cmds["processing"]])
    print("Finished: ")
    pprint([c[0] for c in cmds["finished"]])

async def main():
    # Open fill production schema file 
    with open("../schemas/fill_production_schema.sql") as f:
        cmds = {
            "remains": get_commands(f.read()),
            "processing": [],
            "finished": [],
        }

    pool = await get_connection_pool(**connection_options)
    pprint(cmds)
    async with pool.acquire() as conn:
        for item in copy.deepcopy(cmds["remains"]):

            # Move cmd to processing
            cmds["remains"].remove(item)
            cmds["processing"].append(item)
            show(cmds)
            # Process cmd
            if item[1]:
                await conn.execute(item[1])
            # Process 
            cmds["processing"].remove(item)
            cmds["finished"].append(item)
            show(cmds)

asyncio.run(main())
