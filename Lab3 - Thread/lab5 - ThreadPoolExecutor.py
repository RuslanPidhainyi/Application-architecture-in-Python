#ThreadPoolExecutor to część modułu concurrent.futures w Pythonie, która zapewnia interfejs do tworzenia i zarządzania pulą wątków dla równoległego wykonywania zadań

#Możemy przekazać funkcje lub wyrażenia do wykonania do puli wątków za pomocą metody submit() lub map().

#ThreadPoolExecutor automatycznie zarządza cyklem życia wątków w puli, takimi jak startowanie, zatrzymywanie i ponowne uruchamianie

import concurrent.futures
import logging
import time
import concurrent


def funkcja_watku(nazwa):
    logging.info(f"Rozpoczęcie wątku: {nazwa}")
    time.sleep(4) 
    logging.info(f"Zakończenie wątku: {nazwa}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
                                                
                                                #max_workers=3 - Ilość wątków w puli
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(funkcja_watku, range(3))
        #map - mapa z funkcją i zestawem argumentów