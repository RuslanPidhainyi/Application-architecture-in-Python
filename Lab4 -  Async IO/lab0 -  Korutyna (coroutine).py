# Korutyna (coroutine) - to funkcja asynchroniczna zdefiniowana za pomocą słowa kluczowego 
# async. Umożliwia czasowe wstrzymanie wykonania przy użyciu await, co pozwala na 
# oczekiwanie na wynik operacji bez blokowania głównego wątku programu.

import asyncio
import time


async def count():
    print('jeden')
    await asyncio.sleep(1)
    print("dwa")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    t = time.time()
    asyncio.run(main())

    print(f"Czas wykonywania {time.time() - t}")