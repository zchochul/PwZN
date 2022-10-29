class ClassDecorator:
    def __init__(self, func):
        self._func = func
    
    def __call__(self):
        print('Hello Caller')

@ClassDecorator
def my_function():
    s = 'My Function'
    print(s)
    return s

#print(type(my_function))
fc = ClassDecorator()
fc()