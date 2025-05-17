# Kolejki (Queue) w module multiprocessing są używane do bezpiecznego komunikowania się między procesami. Pozwalają one na przekazywanie danych między procesami w sposób, który jest odporny. Działają analogicznie do kolejek Queue z modułu queue.

import logging
from multiprocessing import Process, Queue
import time


logging.basicConfig(level = logging.INFO)

def producer(queue):
    for i in range(5):
        time.sleep(1)
        item = f'Element {i}'
        queue.put(item)
        logging.info(f'Producent: {item}')

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        logging.warning(f'Consumend: {item}')

if __name__ == "__main__":
    queue = Queue()

    producer_process = Process(target=producer, args=(queue,))
    consumer_process = Process(target=consumer, args=(queue,))
    producer_process.start()
    consumer_process.start()
    producer_process.join()
    queue.put(None)  # Wysłanie sygnału zakończenia do konsumenta
    consumer_process.join()

#INFO:root:Producent: Element 0
#WARNING:root:Consumend: Element 0
#INFO:root:Producent: Element 1
#WARNING:root:Consumend: Element 1
#INFO:root:Producent: Element 2
#WARNING:root:Consumend: Element 2
#INFO:root:Producent: Element 3
#WARNING:root:Consumend: Element 3
#INFO:root:Producent: Element 4
#WARNING:root:Consumend: Element 4

