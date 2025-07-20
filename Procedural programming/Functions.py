#https://roadmap.sh/python

print()
#Python not supported in functions overloading!
print('Python not supported in functions overloading!')
print()
print('Functions')
print()

#func ktora nic nie zwaraca
def main():
    print('Hello world!')

#funk ktora nic nie zwraca, ale przyjmuje argumenty (z jawnym typem)
def greet_1(name: str):
    print(f'Hello {name}')

#funkcja ktora nic nie zwraca, ale przyjmuje dwa argumenty (z nie jawnym typem)
def greet_2(name, surname):
    print(f'Hello {name} {surname}')

#funkcja ktora zwraca wartosc (z jawnym typem)
def getHardcordID() -> int:
    return 42

#funkcja ktora zwraca wartosc (z nie jawnym typem)
def getHardcordFullname():
    fullname = 'Ruslan Pidhainyi'
    return fullname

#funkcja ktora przyjmuje parametry i zwraca wartosc (z jawnym typem)
def addOperation_1(a: int, b: int) -> int:
    return a + b

#funkcja ktora przyjmuje parametry i zwraca wartosc (z nie jawnym typem)
def addOperation_2(a, b, c):
    return a + b + c

main()

greet_1('Ruslan')

greet_2('Ruslan', 'Pidhainyi')

print(getHardcordID())

print(getHardcordFullname())

result = addOperation_1(5, 10)
print(f'Result of addOperation: {result}')  # Output: Result of addOperation: 15

res = addOperation_2(5, 10, 15)
print(f'Result of addOperation: {res}')  # Output: Result of addOperation: 30


print()
print('Lambda functions')
print()

#lambda func ktora nic nie zwaraca
firstProgram = lambda: print('Hello world!')

#lambda funk ktora nic nie zwraca, ale przyjmuje argumenty
goodbye = lambda name: print(f'Goodbye {name}')

#lambda funkcja ktora zwraca wartosc 
getID = lambda: 42

#lambda funkcja ktora przyjmuje parametry i zwraca wartosc
subtractionOperations = lambda a, b: a - b

firstProgram()

goodbye('Ruslan')

print(getID())

result = subtractionOperations(10, 5)
print(f'Result of subtractionOperations: {result}')  # Output: Result of subtractionOperations: 5