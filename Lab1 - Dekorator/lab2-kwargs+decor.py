# **kwargs - це є параметр у декораторі дає змогу приймати довільну кількість іменованих аргументів в функції а потім викликає оригінальну функцію.

# **kwargs використовується для передачі іменованих аргументів, наприклад:
# sum_numbers(a=1, b=2, c=3, d=4) — тут аргументи передаються як ключі та значення, тому порядок не є критичним, але імена параметрів повинні збігатися з очікуваними в функції.

def initial_decorator_with_kwars(func):
    def wrapper(**kwargs):
        print(f"[initial_decorator_with_kwars] wyłowuje z pozycji argument w funkcji {kwargs}")
        # Викликаємо оригінальну функцію, передаючи їй ці аргументи
        result = func(**kwargs)
        return result
    return wrapper

@initial_decorator_with_kwars
def sum_number(a, b, c, d):
    return a + b + c + d

@initial_decorator_with_kwars
def show_info(name, age):
    print(f"Imię: {name}, Wiek: {age}")


#############################################################
# **kwargs - mozna uzywać i z liczbami i z stringami

numbers = sum_number(a=1, b=2, c=3, d=4)
print("wynik ", numbers)

print()

info = show_info(name="Ruslan", age=21)
print(info)


