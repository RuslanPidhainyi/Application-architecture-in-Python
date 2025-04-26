# Race condition to sytuacja, w której wynik działania programu zależy od kolejności lub
#czasu wykonania różnych wątków lub procesów. W Pythonie, race conditions mogą wystąpić,
#gdy kilka wątków próbuje równocześnie modyfikować współdzielone zasoby bez
#odpowiedniej synchronizacji


#На цьому слайді показано приклад race condition (змагання потоків) — це ситуація, коли результат роботи програми залежить від того, в якому порядку потоки отримують доступ до спільної змінної.


import threading
import time


wspoldzielona_zmienna = 0

def increment():
    global wspoldzielona_zmienna #??!! global дозволяє змінювати глобальну змінну зсередини функції.
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

print("Koncowa wartosc wspoldzielonej zmiennej: ", wspoldzielona_zmienna) # Koncowa wartosc wspoldzielonej zmiennej:  1