"""
       ____                                     ___                
  ____/ / /_  ____  ____  _________ ___  ____ _/ (_)___  ___  _____
 / __  / __ \/ __ \/ __ \/ ___/ __ `__ \/ __ `/ / /_  / / _ \/ ___/
/ /_/ / /_/ / / / / /_/ / /  / / / / / / /_/ / / / / /_/  __/ /    
\__,_/_.___/_/ /_/\____/_/  /_/ /_/ /_/\__,_/_/_/ /___/\___/_/     
                                                                   
Make normalizations about data.
"""
import asyncpg, asyncio, click
from tqdm import tqdm
connection_options = {
    "user":"enem",
    "password":"catapimbas",
    "port":5432,
    "max_size":20,
    "min_size":20,
}
async def get_connection_pool(**options):
    return await asyncpg.connect(**options)

get_commands = lambda sql_script: [(command.split("\n")[0], command,) for command in [command + ";" for command in sql_script.split(";")]]

def show(cmds):
    click.clear()
    print("Remains: ",[c[0] for c in cmd["remains"]])
    print("Processing: ",[c[0] for c in cmd["processing"]])
    print("Finished: ",[c[0] for c in cmd["finished"]])

async def main():
    # Open fill production schema file 
    with open("../schemas/fill_production_schema.sql") as f:
        cmds = {
            "remains": get_commands(f.read()),
            "processing": [],
            "finished": [],
        }
    async def command_executor(queue:asyncio.Queue, pool:pool, cmds: dict):
        async with pool.acquire() as conn:
            while True:
                item = await queue.get()

                # Move cmd to processing
                cmds["remains"].remove(item)
                cmds["processing"].append(item)
                show(cmds)
                # Process cmd
                await conn.execute(item[1])
                show(cmds)
                # Process 
                cmds["processing"].remove(item)
                cmds["remains"].append(item)
                queue.task_done()

    pool = await get_connection_pool(connection_options)
    queue = asyncio.Queue(maxsize=40)
    tasks = []
    for i in range(20):
        task = asyncio.create_task(command_executor(queue, pool, cmds))
        tasks.append(task)
    for item in cmds["remains"]:
        await queue.put(item)

asyncio.run(main)
