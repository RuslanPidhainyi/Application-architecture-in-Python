#Instrukcja yield działa podobnie do return, ale zamiast zakończenia funkcji i zwrócenia 
#wartości do miejsca wywołania, tymczasowo zatrzymuje funkcję, zwracając wartość do 
#miejsca wywołania. Następnie, gdy funkcja zostanie wznowiona, będzie kontynuować 
#działanie od miejsca, w którym została zatrzymana, zamiast rozpoczynać od nowa.

def generator_liczb(n):
    for i in range(n):
        yield i

#Dzieki for mozemy iterowac po generatorze w ktorym znajduje sié yield
gen = generator_liczb(10)
for n in gen:
    print(n)
# 0 1 2 3 4 5 6 7 8 9