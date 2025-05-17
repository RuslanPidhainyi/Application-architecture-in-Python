import threading
import logging
import time

# Konfiguracja logowania: ustawiamy poziom INFO oraz format komunikatów
logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(message)s")

def thread_function(numer):

    logging.info("Wątek %d: rozpoczął pracę", numer)
    time.sleep(2)  # Symulacja zadania trwającego 2 sekundy
    logging.info("Wątek %d: zakończył pracę", numer)

if __name__ == "__main__":
    threads = []

    # Tworzenie i uruchamianie 3 wątków
    for index in range(3):
        logging.info("Main: Tworzenie wątku %d", index)
        t = threading.Thread(target=thread_function, args=(index,))
        threads.append(t)
        t.start()

    # Oczekiwanie na zakończenie wszystkich wątków
    for index, t in enumerate(threads):
        logging.info("Main: Czekanie na zakończenie wątku %d", index)
        t.join()

    logging.info("Main: Wszystkie wątki zakończone")
