#list comprehension
# List comprehension — створює повноцінний список у пам'яті
lista = [x**2 for x in range(10)]
print(type(lista))  # <class 'list'> 

print(lista) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#wyrazenie generatorowe
# Generator expression — створює генератор, який обчислює значення "на льоту"
generator = (x**2 for x in range(10))
print(type(generator)) # <class 'generator'>

print(generator)  # <generator object <genexpr> at 0x7f8c3c2b4d60>

# Щоб побачити елементи генератора, можна пройтися по ньому в циклі for або перетворити його на список:
print(list(generator)) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

for value in generator:
    print(value, end=" ") # 0 1 4 9 16 25 36 49 64 81

#Dobra praktyka: Zawsze przekazuj wyrażenie generatorowe, zamiast wyrażenia listowego, do funkcji, które oczekują obiektów iterowalnych, takich jak min(), max() i sum()

#uzycie w funkcjach wbudowanych

#✅ x**2 for x in range(10) generates:
#0, 1, 4, 9, 16, 25, 36, 49, 64, 81

min(x**2 for x in range(10)) # 0
max(x**2 for x in range(10)) # 81 
sum(x**2 for x in range(10)) # 285 