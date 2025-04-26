#Deadlock (zakleszczenie) to sytuacja, gdy dwa lub więcej wątków są zablokowanewzajemnie i oczekują na siebie nawzajem, aby zwolnić zasoby, które trzymają, przed kontynuacją swojego działania.

import threading

l = threading.Lock()
print("Przed pierwszym zablokowaniem") #Przed pierwszym zablokowaniem

l.acquire() #Metoda .acquire() na Lock w wątku tworzy "blokadę", a .release() ją zwalnia.
print("Przed drugime zablokowanie") #Przed drugime zablokowanie

l.acquire()
print("Po zablokowaniu")

#W rezultacie żaden z wątków lub procesów nie może kontynuować pracy, co prowadzi do zatrzymania się całego systemu