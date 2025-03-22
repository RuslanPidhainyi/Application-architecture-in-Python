# *args - це є параметр у декораторі дає змогу приймати довільну кількість позиційних аргументів в функції а потім викликає оригінальну функцію.

# *args використовується для передачі позиційних аргументів, наприклад:
# sum_numbers(1, 2, 3, 4) — тут аргументи передаються за позицією, і їх порядок має значення.


def initial_decorator_with_args(func):
    def wrapper(*args):
        print(f"[initial_decorator_with_args] wyłowuje z pozycji argument w funkcji {args}")
        # Викликаємо оригінальну функцію, передаючи їй ці аргументи
        result = func(*args)
        return result
    return wrapper

@initial_decorator_with_args
def sum_numbers(a, b, c, d):
    return a + b + c + d

@initial_decorator_with_args
def set_words(x, y, z):
    print(f"{x}, {y}, {z}")

#############################################################
# *args - mozna uzywać i z liczbami i z stringami
print("Wynik:", sum_numbers(1, 2, 3, 4))
#[initial_decorator_with_args] wyłowuje z pozycji argument w funkcji (1, 2, 3, 4)
#Wynik: 10

print()

print(set_words("jeden", "dwa", "trzy"))
#[initial_decorator_with_args] wyłowuje z pozycji argument w funkcji ('jeden', 'dwa', 'trzy')
#jeden, dwa, trzy


