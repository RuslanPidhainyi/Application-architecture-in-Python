def licznik():
    print("Start")
    yield 1 # Zwracamy 1, ale nie kończymy funkcji
    yield 2 # Po kolejnym wywołaniu nastąpi powrót do tej linii
    yield 3 # I ponownie czekamy na kolejne next()

# Tworzymy generator
gen = licznik()

# Każde wywołanie next(gen) zwróci kolejną wartość
print(next(gen))  # "Startujemy!" -> 1
print(next(gen))  # 2
print(next(gen))  # 3

# Kolejne wywołanie next() rzuci wyjątek StopIteration, bo generator się wyczerpał.
# print(next(gen))
