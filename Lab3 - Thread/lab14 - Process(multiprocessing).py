#Obiekty procesu reprezentują aktywność, która jest uruchamiana w osobnym procesie. Klasa Process posiada odpowiedniki wszystkich metod klasy threading.Thread

#Різниця між threading і multiprocessing:

#threading — спільна памʼять, але один процес

#multiprocessing — окремі процеси, ізольована памʼять, але дозволяє справжній паралелізм (особливо для CPU-bound задач)


#os.getppid()
#os.getppid() означає get parent process ID — повертає ідентифікатор (ID) батьківського процесу.

#Це корисно для того, щоб дізнатися, який процес запустив поточний (наприклад, головний процес створив дочірній — і ми можемо перевірити, хто був батьком).



#Process(target=f, args=('WSEI',))
#Це створення нового процесу за допомогою multiprocessing.Process.

    #target=f — означає, що процес буде виконувати функцію f.
    #args=('WSEI',) — означає, що функція f отримає 'WSEI' як аргумент.

    #Важливо: args має бути кортежем, навіть якщо один елемент — тому ставимо кому: ('WSEI',).


from multiprocessing import Process #Process — дозволяє створювати окремі процеси (паралельне виконання)
import os


def info(title):
    print(title)
    print("Nazwa modułu:", __name__)
    print("parent process", os.getppid()) #os.getppid() означає get parent process ID — повертає ідентифікатор (ID) батьківського процесу.
    print("process id", os.getpid()) #os.getpid() означає get process ID — повертає ідентифікатор (ID) процесу.

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target = f, args=('WSEI',)) #Proces Це створення нового процесу за допомогою multiprocessing.Process.
    p.start()
    p.join()

#main line
#Nazwa modułu: __main__
#parent process 1912
#process id 1728
#function f
#Nazwa modułu: __mp_main__
#parent process 1728
#process id 24172
#hello WSEI