# Lock jest mechanizmem synchronizacji, który pozwala kontrolować dostęp wielu wątków do
#współdzielonych zasobów. Jest obiektem, który działa jak przepustka do zasobów.
#Każdy wątek, który chce przepustkę, musi poczekać, aż zostanie zwolniona

#Metoda .acquire() na Lock w wątku tworzy "blokadę", a .release() ją zwalnia.

#Lock może działać jako menadżer konteksu, więc można go używać z "with"


import threading
import time


wspoldzielona_zmienna = 0
lock = threading.Lock() # Tworzenie obiektu lock

def increment():
    global wspoldzielona_zmienna # global дозволяє змінювати глобальну змінну зсередини функції.
    with lock:
        temp = wspoldzielona_zmienna 
        time.sleep(0.01)
        temp += 1
        wspoldzielona_zmienna = temp

watek1 = threading.Thread(target=increment)
watek2 = threading.Thread(target=increment)

watek1.start()
watek2.start()

watek1.join() # Czekanie na zakończenie wątku || join blokuje program główny do zakończenia wątku x
watek2.join()

print("Koncowa wartosc wspoldzielonej zmiennej: ", wspoldzielona_zmienna) # Koncowa wartosc wspoldzielonej zmiennej:  2