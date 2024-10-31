import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(1, 6):
        await asyncio.sleep(6 - power)
        print(f"Силач {name} поднял {i} шар")
    print(f"Силач {name} закончил соревнования.'")


async def start_tournament():
    tasks = list()
    tasks.append(asyncio.create_task(start_strongman('Pasha', 3)))
    tasks.append(asyncio.create_task(start_strongman('Denis', 4)))
    tasks.append(asyncio.create_task(start_strongman('Apollon', 5)))
    for task in tasks:
        await task

asyncio.run(start_tournament())
