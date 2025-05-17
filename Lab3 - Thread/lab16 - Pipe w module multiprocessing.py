#Potoki (Pipes) w module multiprocessing są używane do komunikacji między procesami poprzez przesyłanie strumieni danych. Każdy potok zapewnia dwukierunkową komunikację między dwoma procesami, gdzie jeden proces może pisać do potoku, a drugi proces może czytać z niego

from multiprocessing import Process, Pipe

def f(conn):
    conn.send("Hello")# Надсилає повідомлення через pipe
    conn.close()# Закриває сторону з'єднання

if __name__ == '__main__':
    parent_conn, child_conn = Pipe() # Tworzenie potoku w 2 zmiennach & Обидві сторони можуть надсилати (send()) і отримувати (recv()) повідомлення.
    p = Process(target=f, args=(child_conn,)) #Створюється новий процес p, який буде виконувати функцію f(child_conn).
    
    p.start() # запускає дочірній процес.

    print(parent_conn.recv())   #Батьківський процес викликає recv() на своїй стороні каналу.
                                # Чекає на повідомлення і виводить отримане повідомлення "Hello" на екран.
    
    p.join() #змушує головний процес чекати, доки дочірній завершить роботу.

    # WYNIK: Hello