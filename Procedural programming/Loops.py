#https://roadmap.sh/python
#https://realpython.com/python-for-loop/#the-guts-of-the-python-for-loop
#https://realpython.com/python-while-loop/

#For
print('Cykl: For')
print()

# for element in iterable:
#   body

colors = ['Red', 'Blue', 'Yellow', 'White', 'Black', 'Brown', 'Green']

for color in colors:
    print(color)

#Red
#Blue 
#Yellow
#White
#Black
#Brown
#Green

print()

points = [(1,4), (3,6), (7,3)]

for x,y in points:
    print(f"{x = } and {y = }")

# x = 1 and y = 4
# x = 3 and y = 6
# x = 7 and y = 3


print()

for index in range(5):
    print(index)

#0
#1
#2
#3
#4

print()
print('len()') #Compare to lenght in C#
print()

str = 'Hello World'
print(len(str)) #11

list = [0, 1, 2, 3, 4, 5]
print(len(list)) #6 



print()
print('Cykl: While')
print()

# while condition:
#   body

number = 5

while number > 0:
    print(number)
    number -= 1
#5
#4
#3
#2
#1


print()

number_1 = 1

while number_1 <= 5:
    print(number_1)
    number_1 += 1
#1
#2
#3
#4
#5


print()

number_2 = 5

while number_2 != 0:
    print(number_2)
    number_2 -= 1
    
#5
#4
#3
#2
#1

