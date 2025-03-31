#Funkcja next() jest używana do pobierania kolejnych wartości z generatora. Gdy generator 
#jest wywoływany za pomocą funkcji next(), wykonuje on kolejny krok i zwraca kolejną 
#wartość z sekwencji, którą generuje.

def generartor_numbers(n):
    for i in range(n):
        yield i

gen = generartor_numbers(5)
print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 2
#print(next(gen)) # 3
#print(next(gen)) # 4
#print(next(gen, "wartosc domyslna")) # po 4 pietli, wynikem biedzie: wartosc domyslna




#Gdy generator wyczerpie swoje wartości, a próbujemy pobrać kolejną za pomocą next(), 
#zostanie wygenerowany wyjątek StopIteration. W pętli for jest on automatycznie 
#obsługiwany, dlatego zazwyczaj używamy pętli for do iterowania po generatorach.
 
#Możemy dostarczyć tej funkcji wartość domyślną w jej
#drugim parametrze.