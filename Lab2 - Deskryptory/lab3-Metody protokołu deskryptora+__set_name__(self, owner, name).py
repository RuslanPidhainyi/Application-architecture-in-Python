#  __set_name__(self, owner, name) - jest to metoda specjalna wprowadzona w Pythonie 3.6, która jest wywoływana podczas definiowania klasy  i umożliwia ustawienie nazwy atrybutu w klasie, do którego deskryptor jest przypisany.

# Parametr owner reprezentuje klasę, do której deskryptor jest przypisany, a name reprezentuje nazwę atrybutu

class BinarnyDeskryptor:
    def __set_name__(self, owner, name):
        self.nazwa = name
        self.nazwa_binarna = f"{name}_binarna"
    
    def  __get__(self, instance, owner):
        if instance is None:
            return self
        print(f"Pobieranie wartosci atrybutu {self.nazwa}")
        return instance.__dict__.get(self.nazwa)  
    
    def __set__(self, instance, value):
        print(f"Ustawianie wartosci atrybutu {self.nazwa} na {value}")  
        instance.__dict__[self.nazwa] = value
        instance.__dict__[self.nazwa_binarna] = bin(value)

class MyClass:
    atrybut = BinarnyDeskryptor()

obj = MyClass()
obj.atrybut = 10
print(obj.atrybut) # Wywołanie __get__() deskryptora
print(obj.atrybut_binarna) # Wywołanie __get__() deskryptora
#wynik: Ustrawianie wartosci atrybutu atrybut na 10
#        Pobieranie wartosci atrybutu atrybut
#        10
#        0b1010
