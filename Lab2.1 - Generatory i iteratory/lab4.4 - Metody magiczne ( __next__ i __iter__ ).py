# Metody magiczne __next__ i __iter__ umożliwiają iterowanie przez obiekty klasy Są elementami wykorzystywanymi przy tworzeniu klas, które zachowują się jak iteratory.

#__next__(): ta metoda definiuje, co ma być zwrócone przy wywoływaniu funkcji next() na obiekcie klasy

# __iter__(): Ta metoda definiuje, co ma się dziać, gdy obiekt klasy jest iterowany. Powinna zwracać iterator, który będzie używany do iteracji przez obiekt

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0  # Będziemy przechowywać bieżącą pozycję

    def __iter__(self):
        # __iter__ powinien zwrócić obiekt, który ma metodę __next__.
        # Najczęściej zwraca self, jeśli ta sama klasa implementuje __next__.
        return self

    def __next__(self):
        # Jeśli dotarliśmy do końca listy, rzucamy StopIteration
        if self.index >= len(self.data):
            raise StopIteration

        # Zwracamy bieżący element i przesuwamy indeks
        item = self.data[self.index]
        self.index += 1
        return item



def method1(arr):
    # 1) iter(my_iterable) wywoła my_iterable.__iter__()
    iterator_obj = iter(my_iterable)

    # 2) next(iterator_obj) wywoła iterator_obj.__next__()
    print(next(iterator_obj))  # 1
    print(next(iterator_obj))  # 2
    print(next(iterator_obj))  # 3

    # Kolejne wywołanie spowoduje StopIteration
    print(next(iterator_obj))  # StopIteration


def method2(arr):
    for i in arr:
        print(i)

# Tworzymy obiekt klasy MyIterator
my_iterable = MyIterator([1, 2, 3])


method1(my_iterable)

method2(my_iterable)



