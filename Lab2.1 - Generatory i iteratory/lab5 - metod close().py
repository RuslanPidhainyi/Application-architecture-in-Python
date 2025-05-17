##W momencie wywoływania metody close() generator kończy swoje działanie, a jego iteracja zostanie zatrzymana.

generator = (x**2 for x in range(10))
for i in generator:
    if i == 9:
        generator.close()
    print(i)  # Wydrukuje liczby kwadratowe od 0 do 9, ale zatrzyma się po 9

#Wynik:
#0
#1
#4
#9