import functools


def init_decor_z_argumentem(argument):
    
    def init_decor(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            print(argument, "Przed wylowaniem oryg func. ", func.__name__)
            result = func(*args, **kwargs)
            print(argument, "Po wylowaniem oryg func. ", func.__name__)

            return result
        
        return wrapper
    
    return init_decor

@init_decor_z_argumentem("INFO:")
def func(a, b):
    return a + b

print(func(1, 2))
# INFO:  Przed wylowaniem oryg func.  func
# INFO:  Po wylowaniem oryg func.  func
# 3
