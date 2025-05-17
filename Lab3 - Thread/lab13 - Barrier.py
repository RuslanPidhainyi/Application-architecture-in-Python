#threading.Barrier w Pythonie to klasa synchronizująca, która umożliwia grupie wątków synchroniczne oczekiwanie na siebie nawzajem przed kontynuacją dalszego wykonywania kodu.

import logging
import threading


def zadanie(barrier):
    logging.info("Wątek przed punktem synchronizacji")
    barrier.wait()  # Czekanie na inne wątki
    logging.info("Wątek po punkcie synchronizacji")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    barrier = threading.Barrier(3)  # Ustalamy barierę dla 3 wątków
    for _ in range(3):
        threading.Thread(target=zadanie, args=(barrier,)).start()

#Wynik:
#INFO:root:Wątek przed punktem synchronizacji
#INFO:root:Wątek przed punktem synchronizacji
#INFO:root:Wątek przed punktem synchronizacji

#INFO:root:Wątek po punkcie synchronizacji
#INFO:root:Wątek po punkcie synchronizacji
#INFO:root:Wątek po punkcie synchronizacji