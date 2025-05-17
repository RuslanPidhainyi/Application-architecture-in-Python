#itertools

# Moduł itertools w Pythonie oferuje zestaw narzędzi do efektywnego przetwarzania i manipulacji iteracji, co może znacząco upraszczać kod, szczególnie w przypadku wielokrotnych iteracji.

# Przykłady metod:
# - itertools.cycle() - pozwala na cykliczne przeglądanie kolekcji.
# - itertools.repeat() - powtarza określoną wartość określoną liczbę razy.
# - itertools.product() - tworzy iloczyn kartezjański dwóch lub więcej zbiorów.
# - itertools.combinations() - generuje kombinacje elementów z kolekcji bez powtórzeń.
# - itertools.permutations() - generuje permutacje elementów z kolekcji.

import itertools




def iterToolCycle(colors):

    cycled = itertools.cycle(colors) # - itertools.cycle() - pozwala na cykliczne przeglądanie kolekcji.

    for i in range(10):
        print(next(cycled))
    print()

#------------------------------------------------------------------------------------------------------------------#

def iterToolRepeat(keywords, count):

    for i in itertools.repeat(keywords, count): # - itertools.repeat() - powtarza określoną wartość określoną liczbę razy.
        print(i) 
    print()

#------------------------------------------------------------------------------------------------------------------#

def iterToolsProduct(TableA, TableB):

    for i in itertools.product(TableA, TableB): # - itertools.product() - tworzy iloczyn kartezjański dwóch lub więcej zbiorów. (Czyli robi kazdy z kazdym)
        print(i)
    print()

#------------------------------------------------------------------------------------------------------------------#

def iterToolsCombinations(data, numb):
    
    comb = list(itertools.combinations(data, numb)) # - itertools.combinations() - generuje kombinacje elementów z kolekcji bez powtórzeń.
    print("Kombinacje 2-elementowe:", comb) 
    print()

#------------------------------------------------------------------------------------------------------------------#


def iterToolsPermutations1(data):
    all_permutations = list(itertools.permutations(data)) # - itertools.permutations() - generuje permutacje elementów z kolekcji.
    print("Wszystkie permutacje:", all_permutations)
    print()

def iterToolsPermutations2(data, numb):
    perm_2 = list(itertools.permutations(data, numb)) # - itertools.permutations() - generuje permutacje elementów z kolekcji.
    print("Permutacje 2-elementowe:", perm_2)
    print()

####################################################################################################################


# - itertools.cycle() - pozwala na cykliczne przeglądanie kolekcji.
colors = ['red', 'green', 'blue']

iterToolCycle(colors) # red green blue red green blue red green blue red green blue




# - itertools.repeat() - powtarza określoną wartość określoną liczbę razy.
keywords = "Hello world!" 
count = 3

iterToolRepeat(keywords, count) # Hello world! Hello world! Hello world!




# - itertools.product() - tworzy iloczyn kartezjański dwóch lub więcej zbiorów. (Czyli robi kazdy z kazdym)
TableA = [1,2]
TableB = ['A','B']   

iterToolsProduct(TableA, TableB) #(1, a) (1, b) (2, a) (2, b) 




# - itertools.combinations() - generuje kombinacje elementów z kolekcji bez powtórzeń.
data = [1,2,3,4] 
numb = 2

iterToolsCombinations(data, numb) # Kombinacje 2-elementowe: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]




# - itertools.permutations() - generuje permutacje elementów z kolekcji.
data1 = [1, 2, 3]
number = 2

iterToolsPermutations1(data1) #Wszystkie permutacje: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

iterToolsPermutations2(data1, number) # Permutacje 2-elementowe: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]