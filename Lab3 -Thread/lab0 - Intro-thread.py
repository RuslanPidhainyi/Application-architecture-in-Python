# Python jest językiem interpretowanym – kod jest wykonywany linijka po linijce. Jednakże to nie oznacza, że każda instrukcja jest wykonywana wyłącznie sekwencyjnie bez możliwości wykonywania zadań równolegle.

# Moduł threading w Pythonie jest wbudowanym modułem, który umożliwia programowanie wielowątkowe.

#Moduł Thread(Wątki\Поток) - pozwalają na współbieżne wykonywanie fragmentów kodu. Dzięki wątkom możesz uruchomić kilka funkcji (czy bloków kodu) jednocześnie, co jest szczególnie przydatne przy operacjach, które mogą czekać na jakieś zdarzenia (np. operacje I/O) lub gdy chcesz, aby program reagował na różne zdarzenia jednocześnie.

##########################################################################################################################################

#За замовчуванням у кожної програми (процесу) є принаймні один потік — головний потік, який виконує ваш код «лінійно».

#Коли ви імпортуєте та використовуєте модуль threading (або інші засоби створення потоків), ви можете створити додаткові потоки і таким чином виконувати кілька завдань «паралельно» в межах одного процесу.

#Wątek posiada stany:
    # - Utworzenia
    # - Wykonywania
    # - (opcjonalnie) zablokowania
    # - Zakończeni

# Moduł implementuje funkcjonalności:
# - Tworzenia wątków--
# - Zarządzania wątkami
# - Synchronizacji
# - Obsługi wyjątków

import threading

def print_cube(num):
    print("Cube: {}" .format(num * num * num) )

def print_square(num):
    print("Square: {}" .format(num * num) )

if __name__ == "__main__":
    # Tworzenie wątków  
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()  # Uruchomienie wątku t1
    t2.start()  # Uruchomienie wątku t2

    t1.join()  # Czekanie na zakończenie wątku t1
    t2.join()  # Czekanie na zakończenie wątku t2
    
    print("Wątki zakończone.")
