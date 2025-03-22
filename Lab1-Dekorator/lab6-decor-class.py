def init_decorator_class(klas):
    class MyClass:
        def __init__(self, *args, **kwargs):
            self.wrapped = klas(*args, **kwargs)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)
        
        def nowa_metoda(self):
            print("To jest Nowa metoda doadna przez dekorator")
        
    return MyClass


@init_decorator_class
class MainClass:
    def __init__(self, x):
        self.x = x

    def metoda(self):
        print("to jest metoda oryginalej klasy")
    

##########################

obj = MainClass(10)
print(obj.x)
print(obj.metoda())
print(obj.nowa_metoda())