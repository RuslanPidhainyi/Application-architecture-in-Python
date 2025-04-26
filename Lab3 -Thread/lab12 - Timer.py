# threading.Timer w Pythonie to klasa, która umożliwia wykonywanie określonych funkcji lub
#kodu w określonym interwale czasowym. Pozwala to na wykonywanie operacji cyklicznych
#lub opóźnionych bez blokowania głównego wątku.

import threading

def function():
    print("Funkcja została wywołana po 5 sekundach opóźnienia.")


time = threading.Timer(5, function)
time.start() 

#Wynik: Funkcja została wywołana po 5 sekundach opóźnienia