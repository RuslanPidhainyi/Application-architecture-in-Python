# *args - це є параметр у декораторі дає змогу приймати довільну кількість позиційних аргументів в функції а потім викликає оригінальну функцію.

# **kwargs - це є параметр у декораторі дає змогу приймати довільну кількість іменованих аргументів в функції а потім викликає оригінальну функцію.

################################################################################################################

# *args використовується для передачі позиційних аргументів, наприклад:
# sum_numbers(1, 2, 3, 4) — тут аргументи передаються за позицією, і їх порядок має значення.

# **kwargs використовується для передачі іменованих аргументів, наприклад:
# sum_numbers(a=1, b=2, c=3, d=4) — тут аргументи передаються як ключі та значення, тому порядок не є критичним, але імена параметрів повинні збігатися з очікуваними в функції.

# Таким чином, різниця полягає саме в способі передачі аргументів: позиційно через *args і іменовано через **kwargs.

def initial_decor_with_args_kwards(func):
    def wrapper(*args, **kwargs):
        print("Argumenty przekazywane do func: ", args, kwargs)
        result = func(*args, **kwargs)
        print("Wynik func: ", result)
        return result
    return wrapper

@initial_decor_with_args_kwards
def sum_numbers(a, b, c):
    return a + b + c

#takoz mozemy zapisywac argumenty w kwargs w nastepujácy sposb nadająć stan - zerowy
@initial_decor_with_args_kwards
def ruznica_numbers(a, b, c=0):
    return - a - b - c

################################################################################################################
print("arg | arg | kwargs")
print(sum_numbers(1, 2, c=3))
#Argumenty przekazywane do func:  (1, 2) {'c': 3}
#Wynik func:  6
# 6

print()

print(ruznica_numbers(1, 2, c=3))
#Argumenty przekazywane do func:  (1, 2) {'c': 3}
#Wynik func:  -6
# -6