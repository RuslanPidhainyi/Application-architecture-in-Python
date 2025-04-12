#throw(ex_type[, ex_value[, ex_traceback]])

#Metoda throw() jest używana w kontekście obsługi wyjątków w generatorach. Gdy metoda throw() zostanie wywołana, wyjątek zostanie wywołany w miejscu, gdzie generator jest obecnie zatrzymany, a następnie generator będzie mógł go obsłużyć za pomocą konstrukcji try-except

def counter():
    try:
        count = 0 #0 
        while True:
            
            #yield dziala jak return ale zatrzymuje na danym indexu i dizie dalej od tego indexu
            yield count # 0 -> 1 -> n
            
            count += 1  #1 -> 2 -> n+1
    except StopIteration:
        print("Generator stopped")

cnt = counter() #tworzymy generator
for i in range(5):
    print(i) #wywolujemy generator i zwracamy nastepny element
    if i >= 2:
        cnt.throw(StopIteration)

#Wynik:
#0
#1
#2
#Generator stopped