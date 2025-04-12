#Потік запускається окремо.

#Основна програма закінчує роботу ще до того, як потік завершить своє виконання.

#Потік логічно "живе паралельно".



import logging
import threading
import time


def funkcja_watku(nazwa):
    logging.info(f"Rozpoczęcie wątku: {nazwa}")
    time.sleep(2)  # symulacja długotrwałej operacji
    logging.info(f"Zakończenie wątku: {nazwa}")

#Це умовна конструкція, яка перевіряє, чи запускається файл напряму, а не імпортується як модуль. Якщо так — виконується код нижче.
#Це запобігає небажаному запуску коду при імпорті цього файлу в інші скрипти.
if __name__ == "__main__":

    #Налаштовуємо логування на рівні INFO (щоб бачити наші повідомлення).
    #Потім виводимо повідомлення: "Main: перед створенням потоку"
    logging.basicConfig(level=logging.INFO)
    logging.info("Main: Przed stworzeniem wątku")
    
    #             Thread(target=VALUE, ARGS=KEY_WORD_ARGUMENTS)
    x = threading.Thread(target=funkcja_watku, args=("Wątek 1",)) # Tworzenie wątku  
    logging.info("Main: Przed uruchomieniem wątku")
    x.start()   # Uruchomienie wątku

    logging.info("Main: Zakonczenie programu")

#INFO:root:Main: Przed stworzeniem wątku
#INFO:root:Main: Przed uruchomieniem wątku
#INFO:root:Rozpoczęcie wątku: Wątek 1
#INFO:root:Main: Zakonczenie programu
#INFO:root:Zakończenie wątku: Wątek 1
