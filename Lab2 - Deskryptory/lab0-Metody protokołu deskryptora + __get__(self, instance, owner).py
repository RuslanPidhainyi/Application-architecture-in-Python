# Deskryptory są mechanizmem w języku Python, który umożliwia kontrolę dostępu do atrybutów w klasach.
#Pozwalają one na zdefiniowanie niestandardowego zachowania przy dostępie do atrybutu klasy, takiego jak jego odczyt, zapis lub usunięcie 

#(get, set, delete). Deskryptory są używane w Pythonie do implementacji właściwości (properties) oraz do zarządzania dostępem do atrybutów klas.

#Dobra praktyka:
    #Powinniśmy używać deskryptorów do szczególnych przypadków, takich jak projektowanie wewnętrznych API, bibliotek czy frameworków.


#---------------------------------------------------------------------------------------------------#
# Protokół deskryptora definiuje metody specjalne, które można zaimplementować w klasie deskryptora:

# __get__(self, instance, owner)- jest wywoływana, gdy próbujemy pobrać wartość atrybutu, którego deskryptorem jest dana klasa. Czyli Get wyswietla wartosc deskryptora.


# Перша частина — це оголошення дескриптора (Протокув дискриптора дефінює/декларуєми методу спеціальну наприкладі "Get",  яка приймає властивість атрибуту, також можна її визвати з класи для прийнядтя вартості атрибуту).

#Параметр self - це посилання на сам дескриптор, який реалізує методи протоколу дескриптора.
#Параметр instance - це інстанція класу, до якого дескриптор прив'язаний, 
#Параметр owner - це клас, екземпляр якого був створений.

#Prezentacja metody get w deskryptorze
class Initial_Deskryptor:
    def __get__(self, instance, owner):
        print("Pobieranie wartości ... ")
        return instance.wartosc
    

class MyClass:
    deskryptor = Initial_Deskryptor()

obj = MyClass()
obj.wartosc = 42

print(obj.deskryptor)  # Wywołanie __get__() deskryptora
#Wynik: Pobieranie wartości ...
#       42
