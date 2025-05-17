#---------------------------------------------------------------------------------------------------#
# __delete__(self, instance) - ta metoda jest wywoływana, gdy próbujemy usunąć wartość atrybut, którego deskryptorem jest dana klasa. Parametr instance to instancja klasy, do której deskryptor jest przypisany

class Initial_Dyskryptor:
    def __delete__(self, instance):
        print("Usuwania wartości ... ")
        instance._wartosc

class MyClass:
    deskryptor = Initial_Dyskryptor()

obj = MyClass()
obj._wartosc = 23

del obj.deskryptor  # Wywołanie __delete__() deskryptora
# #Wynik: Usuwania wartości ...