#Декоратор використовується для того, щоб додати або змінити поведінку функції без необхідності змінювати її вихідний код. Це дозволяє розділяти основну логіку функції та допоміжні завдання. Наприклад, декоратор може:

    #Автоматично логувати виклики функції.

    #Перевіряти вхідні дані або права доступу.

    #Додавати кешування результатів.

    #Обробляти виключення або вимірювати час виконання.

# ALBO

    #Enkapsulacja, czyli separacja obowiązków: Dobry dekorator powinien efektywnie oddzielać różne odpowiedzialności pomiędzy tym, co robi, a tym, co dekoruje.

    #Ortogonalność: To, co robi dekorator, powinno być niezależne i jak najbardziej odłączone od obiektu, który  dekoruje.

    #Możliwość ponownego użycia: Dobrze byłoby, gdyby dekorator można było zastosować do wielu typów, a nie  tylko do jednej instancji jednej funkcji, ponieważ oznacza to, że mógłby być po prostu funkcją

#Таким чином, застосування декоратора робить код більш модульним і зручним для повторного використання, оскільки одна і та ж допоміжна логіка може бути застосована до різних функцій за допомогою одного декоратора.

##########################################################################################################################

# Перша частина — це оголошення декоратора (функції, яка приймає іншу функцію як аргумент і повертає нову/модифіковану).

def initial_decorator(func):
    def inside_func():
        print("Tekst wyświetlony przed funkcją")

        func()

        print("Tekst wyświetlony po funkcji")
    return inside_func
    


# А друга частина — це застосування декоратора до функції przykladowa_funkcja. 

# Коли Python бачить @mój_dekorator перед оголошенням функції, він фактично викликає initial_decorato(przykladowa_funkcja), і повернута від декоратора функція замінює оригінальну przykladowa_funkcja.

@initial_decorator
def przykladowa_func():
    print("To jest treść funkcji") #tekst nie wyswietli sie, bo funkcja zostala zadeklarowana w dekoratorze

przykladowa_func() #tak jak nadpisalismy nad func dekorator to otrzymamy tekst z dekoratora + tekst z funkcji

#Wynik:
#Tekst wyświetlony przed funkcją
    #To jest treść funkcji  
#Tekst wyświetlony po funkcji