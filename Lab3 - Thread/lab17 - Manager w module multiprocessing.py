#Manager w module multiprocessing jest używany do współdzielenia zasobów między procesami. Umożliwia tworzenie zarządców, które są obiektami serwerowymi, zapewniającymi dostęp do współdzielonych obiektów. Dzięki temu obiekty te mogą być używane przez różne procesy, a zmiany dokonane przez jeden proces są widoczne dla pozostałych

from multiprocessing import Process, Manager #Manager — створює спільні об'єкти для обміну даними між процесами.

def modify_list(shared_list, index, value):
    shared_list[index] = value

if __name__ == '__main__':
    with Manager() as manager:
        shared_list = manager.list(range(5))
        #Викликаємо Manager, який створює сервер для обміну даними.
        #Створюємо спільний список shared_list з елементами [0, 1, 2, 3, 4].
        #Цей список тепер може змінюватися одночасно з різних процесів.

        processes = []

        #перебераєм елементи да кожен елемнт списку shared_list множим на 10, поччинаючі із 0 до 4
        for i in range(5):
            p = Process(target=modify_list, args=(shared_list, i, i*10))
            processes.append(p)
            p.start()
        
        #Чекаємо завершення всіх процесів
        for p in processes:
            p.join() #join() — означає "почекай, поки цей процес завершиться". Без join() програма могла б продовжити виконання, не чекаючи всіх змін.

        print("Modyfikowana lista:", shared_list)

#WYNIK: Modyfikowana lista: [0, 10, 20, 30, 40]