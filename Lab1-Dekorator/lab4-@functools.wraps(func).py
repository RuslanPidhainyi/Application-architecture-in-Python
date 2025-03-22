import functools

# @wraps || @functools.wraps - nadaje nazwe i docstring oryginalnej funkcji oryginalnej funkcji


#without @wraps || @functools.wraps, czyli bez zachowania oryginalnej nazwy funkcji i jej dokumentacji 
# Prostymi slowami - zwykly dekorator z args i kwargs

def init_simple_decorator(func):
    def wrapper(*args, **kwargs):
        """Docstring від wrapper (декоратора)."""
        print(f'[simple_decorator] Przed wylowaniem oryg func.')
        result = func(*args, **kwargs)
        print(f'[simple_decorator] Po wywolaniu oryg func.')
        return result
    return wrapper


#with @wraps || @functools.wraps, czyli z zachowania oryginalnej nazwy funkcji i jej dokumentacji 
# Prostymi slowami - WRAPS dekorator z uzyciem args i kwargs

def init_wrapper_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):    
        """Docstring від wrapper (декоратора)."""
        print(f'[wrapper_decorator] Przed wylowaniem oryg func.')
        result = func(*args, **kwargs)
        print(f'[wrapper_decorator] Po wywolaniu oryg func.')
        return result
    return wrapper




##################################################################
#uzycie dekoratorów


@init_simple_decorator
def greet(name: str):
    """Docstring від greet (оригінальна функція)."""
    print(f'Hello, {name}!')


@init_wrapper_decorator
def greet2(name: str):
    """Docstring від greet2 (оригінальна функція)."""
    print(f'Hello, {name}!')


#########################
#test

#without @wraps || @functools.wraps
print("Name of function: ", greet.__name__) #nazwa dekoratora - wrapper
print("Docstring of function: ", greet.__doc__) #docstring dekoratora - Docstring від wrapper (декоратора)

print()

#with @wraps || @functools.wraps
print("Name of function: ", greet2.__name__)  #nazwa dekoratora - greet2
print("Docstring of function: ", greet2.__doc__) #docstring dekoratora - Docstring від greet2 (оригінальна функція)