# Pool w module multiprocessing umożliwia równoczesne wykonywanie wielu zadań w puli procesów. Ma identyczne działanie jak ThreadPoolExecutor z modułu concurrent.future.

from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == '__main__':

    #Створюємо пул із 4 процесів.
    #Це значить, що до 4 процесів можуть працювати паралельно.
    
    with Pool(processes = 4) as pool:
        results = pool.map(square, range(10))
        #map() — застосовує функцію square до кожного елемента в діапазоні від 0 до 9.
        #pool.map працює як звичайний map, але паралельно!
        #Він бере кожен елемент з range(10) (0, 1, 2, ..., 9) і запускає square(n) у одному з процесів.
        #Результати збираються у список results.

        print("Kwadraty liczb od 0 do 9:", results)
# #WYNIK: Kwadraty liczb od 0 do 9: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]