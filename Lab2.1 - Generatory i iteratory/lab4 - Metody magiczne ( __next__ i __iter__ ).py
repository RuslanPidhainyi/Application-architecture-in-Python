# Metody magiczne __next__ i __iter__ umożliwiają iterowanie przez obiekty klasy Są elementami wykorzystywanymi przy tworzeniu klas, które zachowują się jak iteratory.

#__next__(): ta metoda definiuje, co ma być zwrócone przy wywoływaniu funkcji next() na obiekcie klasy

# __iter__(): Ta metoda definiuje, co ma się dziać, gdy obiekt klasy jest iterowany. Powinna zwracać iterator, który będzie używany do iteracji przez obiekt

# Mamy listę
my_list = [10, 20, 30]

# 1) Funkcja iter() wywołuje my_list.__iter__() i zwraca iterator
iterator_obj = iter(my_list)
print("Typ iteratora:", type(iterator_obj))  # <class 'list_iterator'>

# 2) Funkcja next() wywołuje iterator_obj.__next__()
print(next(iterator_obj))  # 10
print(next(iterator_obj))  # 20
print(next(iterator_obj))  # 30

# Kolejne wywołanie next() podniesie błąd StopIteration
print(next(iterator_obj))  # StopIteration
