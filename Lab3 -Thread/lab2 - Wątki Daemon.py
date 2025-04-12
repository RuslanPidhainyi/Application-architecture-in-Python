#W wyniku na poprzednim labie1 Wątek zakończył się po zakończeniu programu głównego

#Wynik z labu1:

#INFO:root:Main: Przed stworzeniem wątku
#INFO:root:Main: Przed uruchomieniem wątku
#INFO:root:Rozpoczęcie wątku: Wątek 1
#INFO:root:Main: Zakonczenie programu
#INFO:root:Zakończenie wątku: Wątek 1


#Wątki Daemon w Pythonie są zamykane automatycznie, gdy główny wątek programu zakończy swoje działanie. Jeśli program uruchamia wątki, które nie są wątkami daemon, to program będzie oczekiwać, aż te wątki zakończą swoje działanie przed zakończeniem pracy programu.

import logging
import threading
import time


def funkcja_watku(nazwa):
    logging.info(f"Rozpoczęcie wątku: {nazwa}")
    time.sleep(2) 
    logging.info(f"Zakończenie wątku: {nazwa}")


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)
    logging.info("Main: Przed stworzeniem wątku")
    
    x = threading.Thread(target=funkcja_watku, args=("Wątek 1",), daemon=True) # Tworzenie wątku  
                                                                #Wątek Daemon
                                                                
                                                                #Wątki Daemon w Pythonie są zamykane automatycznie, gdy główny wątek programu zakończy swoje działanie. Jeśli program uruchamia wątki, które nie są wątkami daemon, to program będzie oczekiwać, aż te wątki zakończą swoje działanie przed zakończeniem pracy programu.
    logging.info("Main: Przed uruchomieniem wątku")
    x.start()   # Uruchomienie wątku

    logging.info("Main: Zakonczenie programu")

#INFO:root:Main: Przed stworzeniem wątku
#INFO:root:Main: Przed uruchomieniem wątku
#INFO:root:Rozpoczęcie wątku: Wątek 1
#INFO:root:Main: Zakonczenie programu