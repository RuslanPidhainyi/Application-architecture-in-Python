# Kolejka (asyncio.Queue) to narzędzie służące do asynchronicznej komunikacji między 
# zadaniami w ramach jednej pętli zdarzeń. Umożliwia nieblokujące przekazywanie danych 
# pomiędzy różnymi korutynami, wspierając współbieżne przetwarzanie informacji. Kolejki są 
# szczególnie przydatne w architekturach opartych na producentach i konsumentach

import asyncio


async def producent(kolejka):
    for i in range(5):
        await asyncio.sleep(1)
        await kolejka.put(i)
        print(f"Dodano do kolejki: {i}")

async def konsument(kolejka):
    while True:
        item = await kolejka.get()
        print(f"Pobrano z kolejki: {item}")

async def main():
    kolejka = asyncio.Queue()

    producent_task = asyncio.create_task(producent(kolejka))
    konsument_task = asyncio.create_task(producent(kolejka))

    await asyncio.gather(producent_task, konsument_task)

asyncio.run(main())