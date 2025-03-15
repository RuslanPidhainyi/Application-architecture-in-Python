import time
import functools
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def timer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        logging.info(f"Function execution time: {end_time - start_time}")
        return result
    return inner

@timer
def baseFunc_iteration(n):
    for i in range(n):
        pass


#Stworz dekorator, ktory bédzie odpowiedzalny za wyswietlanie liczby elementów listy, jesli jakakolwiek lista pojawi sié w parametrach funktion dekorowanej. Protip: uzyj isinstancje do sprawdzenia czy parametr jest listą.

logging.basicConfig(level=logging.INFO)

def list_counter(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        for arg in args:
            if isinstance(arg, list):
                logging.info(f"List detected with {len(arg)} elements")
        for key, value in kwargs.items():
            if isinstance(value, list):
                logging.info(f"List detected in parameter '{key}' with {len(value)} elements")
        return func(*args, **kwargs)
    return inner

def timer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        logging.info(f"Function execution time: {end_time - start_time}")
        return result
    return inner

@timer
@list_counter
def funcLista_iteration(n, some_list=None):
    for i in range(n):
        pass


#Stworz dekorator, który będzie zapisywał w pliku *.log nazwę funkcji dekorowanej, datę oraz długość wykonania. Nazwa pliku będzie podana jako argument dekoratora. Protip: uzyj ibiblioteke datetime. Pamietaj o tym, zeby dekoratory przyjeły metadane funkcji dekorowanej.

logging.basicConfig(level=logging.INFO)

def log_to_file(filename):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            
            log_message = f"{datetime.now()} - Function: {func.__name__} - Execution time: {execution_time} seconds\n"
            with open(filename, "a") as log_file:
                log_file.write(log_message)
            
            return result
        return inner
    return decorator

def timer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        logging.info(f"Function execution time: {end_time - start_time}")
        return result
    return inner

@timer
@log_to_file(r"E:\My documents\source\repos\Architektura aplikacji w Pythonie\Lab1-Dekorator\execution.log")
def funcSavePlick_iteration(n):
    for i in range(n):
        pass

#************************************************#

#baseFunc_iteration(int(1e7))

#funcLista_iteration(int(1e7), some_list=[1, 2, 3, 4, 5])

#funcSavePlick_iteration(int(1e7)) 