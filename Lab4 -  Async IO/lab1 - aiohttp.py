#aiohttp - to biblioteka do obsługi asynchronicznych operacji HTTP w Pythonie. Umożliwia 
#zarówno tworzenie serwerów HTTP, jak i realizację asynchronicznych żądań po stronie 
#klienta, z pełnym wsparciem dla protokołu WebSocket. Dzięki integracji z asyncio, pozwala na 
#obsługę wielu jednoczesnych połączeń bez blokowania wątków, co czyni ją przydatną w 
#aplikacjach sieciowych o wysokiej skalowalności

#WebSocket — це протокол, що призначений для обміну інформацією між браузером та вебсервером в режимі реального часу. Він забезпечує двонаправлений повнодуплексний канал зв'язку через один TCP-сокет. WebSocket спроектовано для втілення у веббраузерах та вебсерверах, але може також використовуватись будь-яким клієнт-серверним застосунком. Прикладний програмний інтерфейс WebSocket був стандартизований W3C, крім того протокол WebSocket стандартизований IETF як RFC 6455.[1]


#INFO: Aby skorzystac z biblioteki aiohttp, potrzebno zainstalowac biblioteke za pomocy komendy w CLI:
# pip install aiohttp


import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    response = await fetch('https://catfact.ninja/fact')
    print(response)

if __name__ == '__main__':
    asyncio.run(main())