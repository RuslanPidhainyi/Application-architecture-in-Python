#Metoda send() jest używana w kontekście komunikacji dwukierunkowej między kodem wywołującym a generatorem. Pozwala ona na przekazanie wartości do generatora w dowolnym momencie jego działania i umożliwia generatorowi na przetworzenie tej wartości i ewentualne zwrócenie wyniku

def dodawania():
    result = 0
    while True:
        value = yield result
        result += value

calc = dodawania() #tworzymy generator  
next(calc) #przechodzimy do pierwszego yield

print(calc.send(5)) # 0 + 5 = 5 
#wynik to 5
print(calc.send(3))# 5 + 3 = 8
#wynik to 8
print(calc.send(10))# 8 + 10 = 18
#wynik to 18 