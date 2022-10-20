#class Student:
#    pass #pusta instrukcja

from selectors import SelectorKey


class Student:
    def __init__(self):
        self.classes = []
        self._private_varia = 2231 #zeby zmusic do nie uzywania
        print("I'm a student")
    
    def print_classes(self, od_czapy):
        print(self.classes, od_czapy)
    
    def __getitem__(self, pp):
        print(pp)
        return 9001
    
    def __len__(self):
        return 231321

s1 = Student()
s2 = Student()

#wszyscy mają to samo
s1.classes.append('PwZN')
s2.classes.append('KMS')
s1.lol = 'beka' #mozna dodawac sobie parametry TEORETYCZNIE
#print(s1.classes, s2.classes, s1.lol)
s1.print_classes('dupa')

s1['xD']
print(len(s1))
#w pythonie nie ma czegos takiego jak zmienna prywatna

class Parent:
    def __init__(self) -> None:
        self._parent_atr = 2
        print('Hello from parent')
    def parent_fun(self):
        print('siemanko')
    def other_fun(self):
        self.parent_fun()
    __parent_function = parent_fun
    def other_exact_fun(self):
        self.__parent_function()

class Child(Parent):
    def __init__(self):
        super().__init__()
        print('Hello from child')
    def parent_fun(self):
        print('siemaneczko')


c = Child()
c.parent_fun()
c.other_fun() #Wszystko to sa funkcje wirtualne, wiec mozna sie naciac
c.other_exact_fun()
