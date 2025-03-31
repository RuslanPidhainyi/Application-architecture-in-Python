#itertools

# Moduł itertools w Pythonie oferuje zestaw narzędzi do efektywnego przetwarzania i manipulacji iteracji, co może znacząco upraszczać kod, szczególnie w przypadku wielokrotnych iteracji.

# Przykłady metod:
# - itertools.cycle() - pozwala na cykliczne przeglądanie kolekcji.
# - itertools.repeat() - powtarza określoną wartość określoną liczbę razy.
# - itertools.product() - tworzy iloczyn kartezjański dwóch lub więcej zbiorów.
# - itertools.combinations() - generuje kombinacje elementów z kolekcji bez powtórzeń.
# - itertools.permutations() - generuje permutacje elementów z kolekcji.

import itertools

# - itertools.cycle() - pozwala na cykliczne przeglądanie kolekcji.
colors = ['red', 'green', 'blue']
cycled = itertools.cycle(colors)

for i in range(10):
    print(next(cycled))  # red green blue red green blue red green blue red green blue