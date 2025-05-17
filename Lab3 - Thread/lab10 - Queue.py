#  WPythonie klasa Queue z modułu queue umożliwia tworzenie kolejek FIFO

#Najważniejsze metody w klasie Queue to:
# - put(item): Dodaje element do kolejki.----
# - get(): Pobiera element z kolejki, usuwając go z kolejki.
# - empty(): Zwraca True, jeśli kolejka jest pusta.
# - full(): Zwraca True, jeśli kolejka jest pełna.
# - qsize(): Zwraca liczbę elementów w kolejce

import queue
import threading
import time
import logging

def producent(q):
    for i in range(5):
        item = f"wiadomość {i}"
        q.put(item)
        logging.info(f"Dodano do kolejki: {item}  \n")
        time.sleep(1)

def konsument(q):
    while True:
        item = q.get()
        logging.info(f"Pobrano z kolejki: {item}  \n")
        q.task_done()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    q = queue.Queue()

    threading.Thread(target=producent, args=(q,)).start()
    threading.Thread(target=konsument, args=(q,)).start() 

#Wynik
#INFO:root:Dodano do kolejki: wiadomość 0  
#INFO:root:Pobrano z kolejki: wiadomość 0  

#INFO:root:Dodano do kolejki: wiadomość 1  
#INFO:root:Pobrano z kolejki: wiadomość 1  

#INFO:root:Dodano do kolejki: wiadomość 2  
#INFO:root:Pobrano z kolejki: wiadomość 2

#INFO:root:Dodano do kolejki: wiadomość 3  
#INFO:root:Pobrano z kolejki: wiadomość 3

#INFO:root:Dodano do kolejki: wiadomość 4  
#INFO:root:Pobrano z kolejki: wiadomość 4