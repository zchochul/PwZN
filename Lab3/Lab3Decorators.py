#dodawanie funkcjonalnosci do funkcji
import functools
from textwrap import wrap


#def my_decorator(func):
    #@functools.wraps(func)#wtedy nazwa funkcji bedzie ok
#    def wrapper(*args, **kwargs):
#        print(args, kwargs)
#        print('Executed')
#        return func(*args, **kwargs)
#    
#    return wrapper

def my_decorator(st):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(st)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@my_decorator('Hakuna matata')
def my_function(x, y, z=7):
    s = 'My Function'
    print(s)
    return x+y+z


#gwiazdki
def func(x,y,z):
    print(x, y, z)

a = [1, 2, 3]
#func(*a)

#tak dziala dekorator
#my_function = my_decorator(my_function) i zwraca funkcje

#print(my_function.__name__) #klopoty

print(my_function(1,2))