#---------------------------------------------------------------------------------------------------#
#__set__(self, instance, value) Ta metoda jest wywoływana, gdy próbujemy ustawić wartość atrybutu, którego deskryptorem jest dana klasa. Parametr instance to instancja klasy, do której deskryptor jest przypisany, a value to nowa wartość, którą próbujemy przypisać do atrybutu

#Prezentacja metody set w deskryptorze
class Initial_Dyskryptor:
    def __set__(self, instance, value):
        print("Ustawianie wartości ... ")
        instance.wartosc = value

class MyClass:
    deskryptor = Initial_Dyskryptor()

obj = MyClass()
obj.deskryptor = 24

print(obj.deskryptor)  # Wywołanie __set__() deskryptora
#Wynik: Ustawianie wartości ...