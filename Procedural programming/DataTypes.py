#https://roadmap.sh/python
#https://www.tutorialspoint.com/python/python_data_types.htm
'''
                    Data Types in Python
                            |
  Number    String   Boolean   Sequence     Set       Dictionary
    |                             |          
Integer,                        List,      
Float,                          Tuple,    
Complex,                        Range,


- Primitive Types:

Примітивні типи даних – це фундаментальні типи даних, які використовуються для створення складних типів даних (іноді їх називають складними структурами даних). Існує 4 основних примітивні типи даних

1) Integers
2) Floats
3) Strings
4) Booleans


- Non-primitive Types:

Непримітивні типи даних зберігають значення або колекції значень. Існує 4 основні типи непримітивних типів

1) List
2) Tuple
3) Set
4) Dictionary
'''




print('Numeric Data Types (Number)')
var1 = 10          # Integer
print(var1)        # 10
print(type(var1))  # <class 'int'>

var2 = 3.14        # Float
print(var2)        # 3.14
print(type(var2))  # <class 'float'>

#Complex - ... .
var3 = 2 + 3j      # Complex
print(var3)        # (2+3j)
print(type(var3))  # <class 'complex'>



print()



print('String Data Type')
str1 = "Hello World!"   # String
print(str1)             # Hello World!
print(type(str1))       # <class 'str'>

notChar = str1[0]       # String indexing
print(notChar)          # H
print(type(notChar))    # <class 'str'>

print(str1[1:3])                # el
print(str1[1:])                 # ello World!
print(str1 * 2)                 # Hello World!Hello World!
print(str1 + " Hello Gelaxy!")  # Hello World! Hello Gelaxy!
#print(str1 + 2)  # TypeError: can only concatenate str (not "int") to str



print()



print('Boolean Data Types')
bool1 = True        # Boolean
print(bool1)        # True  
print(type(bool1))  # <class 'bool'>

bool2 = False       # Boolean
print(bool1)        # False  
print(type(bool1))  # <class 'bool'>



print()



print('Sequence Data Types')
print()
print('   - List')
'''
Sequence/Послідовність – це тип даних колекції. Це впорядкована колекція елементів. Елементи в послідовності мають позиційний індекс, що починається з 0. Концептуально вона схожа на масив у C або C++. 
У Python визначено наступні три типи даних послідовності.

    List - це змінний тип даних, який дозволяє зберігати колекцію елементів. Елементи в списку можуть бути різних типів, і їх можна змінювати.

    Tuple - це незмінний тип даних, який також дозволяє зберігати колекцію елементів. Елементи в кортежі можуть бути різних типів, але їх не можна змінювати після створення.

    Range - це послідовність чисел, яка використовується для створення діапазонів чисел. Вона часто використовується в циклах для ітерації по числовим значенням.
'''

# list = ['a', "abc", 123, 0.1]

isTrue = True
isStr = 'xuy'
isInt = 123
isFloat = 12.12

list1 = ["Hi", "Hello"]

list = [isTrue, 'a', 'abc', isStr, 1, 0.1, isInt, isFloat, 2-3j] # List
print(list)         # [True, 'a', 'abc', 'xuy', 1, 0.1, 123, 12.12, (2-3j)]
print(type(list))   # <class 'list'>

print(list[0])      # True
print(list[1:3])    # ['a', 'abc']
print(list[1:])     # ['a', 'abc', 'xuy', 1, 0.1, 123, 12.12, (2-3j)]
print(list * 2)     # [True, 'a', 'abc', 'xuy', 1, 0.1, 123, 12.12, (2-3j), True, 'a', 'abc', 'xuy', 1, 0.1, 123, 12.12, (2-3j)]
print(list + list1) # [True, 'a', 'abc', 'xuy', 1, 0.1, 123, 12.12, (2-3j), 'Hi', 'Hello']


print()
print('   - Tuple/Кортеж')
'''
Tuple/Кортеж -  це ще один тип даних послідовності, схожий на список. Кортеж Python складається з певної кількості значень, розділених комами. Однак, на відміну від списків, кортежі укладаються в дужки (...)

Кортеж також є послідовністю, отже, кожен елемент у кортежі має індекс, що вказує на його позицію в колекції. Індекс починається з 0.
'''

# tuple = ('a', "abc", 123, 0.1)

isTrue1 = True
isStr1 = 'xyz'
isInt1 = 123
isFloat1 = 12.12

tuple1 = ("Bay", "Good bay")

tuple = ( isTrue1, 'a', 'abc', isStr1, 1, 0.1, isInt1, isFloat1, 2-3j )
print(tuple)        # (True, 'a', 'abc', 'xyz', 1, 0.1, 123, 12.12, (2-3j))
print(type(tuple))  # <class 'tuple'>

print(tuple[0])         # True
print(tuple[1:3])       # ('a', 'abc')
print(tuple[1:])        # ('a', 'abc', 'xyz', 1, 0.1, 123, 12.12, (2-3j))
print(tuple * 2)        # (True, 'a', 'abc', 'xyz', 1, 0.1, 123, 12.12, (2-3j), True, 'a', 'abc', 'xyz', 1, 0.1, 123, 12.12, (2-3j))
print(tuple + tuple1)   # (True, 'a', 'abc', 'xyz', 1, 0.1, 123, 12.12, (2-3j), 'Bay', 'Good bay')

print()
print('     - different between LIST and TUPLE')
'''
Основні відмінності між списками та кортежами полягають у наступному: 
1.) List укладені в  [], а Tuple укладені в ()
2.) В List можна замінювати елементи в середені колекції
3.) В Tuple не можна замінювати елементи в середені колекції ( Tuple є тільки для читання елементів)
'''

list2 = [1, 22, 333, 4444]
print(list2)        # [1, 22, 333, 4444]
list2[2] = 1_000    # Valid syntax with list
print(list2)        # [1, 22, 1000, 4444]

tuple2 = (1, 22, 333, 4444)
print(tuple2)       # (1, 22, 333, 4444)
#tuple2[2] = 1_000   # Invalid syntax with tuple
#print(tuple2)       # tuple2[2] = 1_000   # Invalid syntax with tuple


print()
print('   - Range/Діапазон')
'''
Range/Діапазон - це незмінна послідовність чисел, яка зазвичай використовується для перебору певної кількості елементів.

Він представлений класом Range. Конструктор цього класу приймає послідовність чисел, починаючи з 0, та збільшує її до 1, доки не досягне заданого числа.
'''

# range(start, stop, step)

'''
start - ціле число для визначення початкової позиції (необов'язково, за замовчуванням: 0)
stop  - Ціле число для визначення кінцевої позиції (обов'язково)
step - Ціле число для визначення приросту (необов'язково, за замовчуванням: 1)
'''

#Нижче поданий приклад як саме можем використовувати range в циклі for:

# stop  - Ціле число для визначення кінцевої позиції (обов'язково)
for i in range(5):
    print(i)

print()
# start - ціле число для визначення початкової позиції (необов'язково, за замовчуванням: 0)
# stop  - Ціле число для визначення кінцевої позиції (обов'язково)
for i in range(2, 5):
    print(i)

print()
# start - ціле число для визначення початкової позиції (необов'язково, за замовчуванням: 0)
# stop  - Ціле число для визначення кінцевої позиції (обов'язково)
# step - Ціле число для визначення приросту (необов'язково, за замовчуванням: 1)
for i in range(1,5,2):
    print(i)

print()

print("Set Data Type")
print()
print('   - Set')
'''
Set - це реалізація набору (set) у Python, як це визначено в математиці. Множина (set) у Python — це колекція, але не індексована чи впорядкована колекція, як рядок, список чи кортеж. Об'єкт не може з'являтися в наборі більше одного разу, тоді як у списку та кортежі один і той самий об'єкт може з'являтися більше одного разу.

Елементи в наборі, розділені комами, поміщаються у фігурні дужки {}. Елементи в колекції наборів можуть мати різні типи даних.

Зверніть увагу, що елементи в колекції множин можуть не слідувати тому ж порядку, в якому вони введені. Позиція елементів оптимізована Python для виконання операцій над множинами, як це визначено в математиці.

Set у Python є об'єктом вбудованого класу set , що можна перевірити за допомогою функції type().

Множина може зберігати лише незмінні об'єкти, такі як число (ціле, число з плаваючою комою, комплексне або логічне), рядок або кортеж. Якщо ви спробуєте помістити список або словник у колекцію множин, Python викличе помилку TypeError . 
'''
# set = { 1, 22, 333, 4444 }

setInt = { 1, 22, 333, 4444, 55555 }
print(setInt)          # {1, 55555, 22, 4444, 333}
print(type(setInt))    # <class 'set'>

print()

setStr = { 'asambler', 'csharp', 'pythone', 'java'}
print(setStr)
print(type(setStr))    # <class 'set'>


print()

print("Dictionary Data Type")
'''
Dictionary - є різновидом хеш-таблиці. Ключ словника може бути майже будь-якого типу Python, але зазвичай це числа або рядки. Значення ж можуть бути будь-яким довільним об'єктом Python.

Словник Python подібний до асоціативних масивів або хешів, що містяться в Perl, і складається з пар ключ:значення . Пари розділяються комами та поміщаються у фігурні дужки {}. Щоб встановити відповідність між ключем і значенням, між ними ставиться символ крапки з комою ':'

Словники обведені фігурними дужками ({ }), а значення можна присвоювати та отримувати до них доступ за допомогою квадратних дужок ([]).
'''

#dict = {'key_0': 'someValue', 'key_1': 'values', 'key_2':'value'}

#OR

#dict = {}
#dict[key_0] = "this is one value"
#dict[key_1] = "this is two value"


dict = {1:"Hello", 2:"Hi", 3:"Good morning"}
print(dict)         # {1: 'Hello', 2: 'Hi', 3: 'Good morning'}
print(type(dict))   # <class 'dict'>

dict1 = {}
dict1['One'] = "Bay"
dict1[2] = "Good bay"
print(dict1)        # {'One': 'Bay', 2: 'Good bay'}
print(type(dict1))  # <class 'dict'>

print(dict[1])          # Hello
print(dict1['One'])     # Bay
print(dict)             # {1: 'Hello', 2: 'Hi', 3: 'Good morning'}
print(dict.keys())      # dict_keys([1, 2, 3])
print(dict1.keys())     # dict_keys(['One', 2])
print(dict.values())    # dict_values(['Hello', 'Hi', 'Good morning'])
print(dict1.values())   # dict_values(['Bay', 'Good bay'])

print()

print("Arrays")

arrString = ['apple', 'banna', 'watermelon']
print(arrString)        # ['apple', 'banna', 'watermelon']
print(type(arrString))  # <class 'list'>

arrInt = [
    [1,2,3,4], 
    [0,1,2,3],
]
print(arrInt)        # [[1, 2, 3, 4], [0, 1, 2, 3]]
print(type(arrInt))  # <class 'list'>