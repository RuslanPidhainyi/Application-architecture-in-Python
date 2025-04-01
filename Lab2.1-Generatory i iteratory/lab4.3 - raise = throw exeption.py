# raise Це ключове слово (оператор), яке використовується для явного викликання exception.
# (python) raise = (C#) throw exeption

def check_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від’ємним!")
    return age

# Викликаємо функцію
try:
    check_age(-5)
except ValueError as e:
    print("Помилка:", e)