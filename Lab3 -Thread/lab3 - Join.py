# join(timeout=None)- ta metoda blokuje wątek wywołujący, aż wątek, którego metoda join() została wywołana, zakończy działanie albo do momentu wystąpienia opcjonalnego limitu czasu.

import logging
import threading
import time


def funkcja_watku(nazwa):
    logging.info(f"Rozpoczęcie wątku: {nazwa}")
    time.sleep(4) 
    logging.info(f"Zakończenie wątku: {nazwa}")


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)
    logging.info("Main: Przed stworzeniem wątku")
    
    x = threading.Thread(target=funkcja_watku, args=("Wątek 1",))# Tworzenie wątku                                                         
    logging.info("Main: Przed uruchomieniem wątku")
    x.start()# Uruchomienie wątku
    x.join() # Czekanie na zakończenie wątku || join blokuje program główny do zakończenia wątku x

    logging.info("Main: Zakonczenie programu")

#INFO:root:Main: Przed stworzeniem wątku
#INFO:root:Main: Przed uruchomieniem wątku
#INFO:root:Rozpoczęcie wątku: Wątek 1
#INFO:root:Zakończenie wątku: Wątek 1
#INFO:root:Main: Zakonczenie programu