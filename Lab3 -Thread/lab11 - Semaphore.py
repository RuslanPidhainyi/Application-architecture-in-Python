#Semafor (Semaphore) pozwala na kontrolowanie ilości dostępnych zasobów i zapewnia, że
#tylko określona liczba wątków lub procesów może uzyskać dostęp do zasobów
#jednocześnie. Semafor zapewnia liczbę dostępnych "przepustek", które określają, ile wątków
#może jednocześnie uzyskać dostęp do chronionego zasobu

import logging
import threading
import time


semaphore = threading.Semaphore(3) # Tworzenie semafora z maksymalnie 2 "przepustkami"

def watek(numer):
    logging.warning(f"Wątek {numer} próbuje uzyskać dostep do semafora")
    with semaphore:
        logging.warning(f'Wątek {numer} uzyskał dostęp do semafora')
        time.sleep(2)
        logging.warning(f'Wątek {numer} zwalnia dostęp do semafora')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    for i in range(6):
        threading.Thread(target=watek, args=(i,)).start()

#tip: ~ próbuje, + uzyskuje, - zwalnia 

#Wynik
#WARNING:root:Wątek 0 próbuje uzyskać dostep do semafora    0 ~
#WARNING:root:Wątek 0 uzyskał dostęp do semafora            0 +

#WARNING:root:Wątek 1 próbuje uzyskać dostep do semafora    1 ~
#WARNING:root:Wątek 1 uzyskał dostęp do semafora            1 +

#WARNING:root:Wątek 2 próbuje uzyskać dostep do semafora    2 ~
#WARNING:root:Wątek 2 uzyskał dostęp do semafora            2 +

#WARNING:root:Wątek 3 próbuje uzyskać dostep do semafora    3 ~
#WARNING:root:Wątek 4 próbuje uzyskać dostep do semafora    4 ~
#WARNING:root:Wątek 5 próbuje uzyskać dostep do semafora    5 ~

#WARNING:root:Wątek 0 zwalnia dostęp do semafora            0 -
#WARNING:root:Wątek 1 zwalnia dostęp do semafora            1 -

#WARNING:root:Wątek 3 uzyskał dostęp do semafora            3 +

#WARNING:root:Wątek 2 zwalnia dostęp do semafora            2 -

#WARNING:root:Wątek 4 uzyskał dostęp do semafora            4 +
#WARNING:root:Wątek 5 uzyskał dostęp do semafora            5 +

#WARNING:root:Wątek 3 zwalnia dostęp do semafora            3 -
#WARNING:root:Wątek 4 zwalnia dostęp do semafora            4 -
#WARNING:root:Wątek 5 zwalnia dostęp do semafora            5 -