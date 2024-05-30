import pygame

#for console

def changecolor(a):
    if a == "r" or a == "red":
        print("\033[31m{}".format(""),end="")
    elif a == "g" or a == "green":
        print("\033[32m{}".format(""),end="")
    elif a == "b" or a == "blue":
        print("\033[32m{}".format(""),end="")
    elif a == "y" or a == "yellow":
        print("\033[33m{}".format(""),end="")
    elif a == "bl" or a == "black":
        print("\033[30m{}".format(""),end="")
    elif a == "v" or a == "violet":
        print("\033[35m{}".format(""),end="")
    elif a == "w" or a == "wite":
        print("\033[37m{}".format(""),end="")
    elif a == "c" or a == "clear":
        print("\033[0m{}".format(""),end="")        
    else:
        print("\033[31m{}".format("NOT_CORRECT_ARGUMENT_FOR_CHANGECOLOR"),"\033[0m{}".format(""))

def changestyle(a):
    if a == "big":
        print("\033[0m{}".format(""),end="")
        print("\033[1m{}".format(""),end="")
    elif a == "little":
        print("\033[0m{}".format(""),end="")
        print("\033[2m{}".format(""),end="")
    elif a == "italic":
        print("\033[0m{}".format(""),end="")
        print("\033[3m{}".format(""),end="")
    elif a == "lined":
        print("\033[0m{}".format(""),end="")
        print("\033[4m{}".format(""),end="")
    elif a == "rt":
        print("\033[0m{}".format(""),end="")
        print("\033[5m{}".format(""),end="")
    elif a == "ft":
        print("\033[0m{}".format(""),end="")
        print("\033[6m{}".format(""),end="")
    elif a == "r":
        print("\033[0m{}".format(""),end="")
        print("\033[7m{}".format(""),end="")
    elif a == "c" or a == "clear":
        print("\033[0m{}".format(""),end="")         
    else:
        print("\033[31m{}".format("NOT_CORRECT_ARGUMENT_FOR_CHANGESTYLE"),"\033[0m{}".format(""))

def HELP():
    changecolor("y")
    print('''
abs(x)

all(iterable)

any(iterable)

ascii(object)

bin(x)

bool(x=False)

class bytearray(source=b'')
class bytearray(source, encoding)
class bytearray(source, encoding, errors)

bytes([source[, encoding[, errors]]])

callable(obj)

chr(i)

classmethod(function)

compile(source, filename, mode, flags=0, dont_inherit=False, optimize=- 1)

complex([real[, imag]])

delattr(object, name)

dir()
dir(object)

dict(**kwargs)
dict(mapping, **kwargs)
dict(iterable, **kwargs)

divmod(a, b)

enumerate(sequence, start=0)

eval(expression, globals=None, locals=None)

exec(object, globals=None, locals=None, /, *, closure=None)

filter(function, iterable)

format(value, format_spec='')

frozenset([iterable])

getattr(object, name)
getattr(object, name, default)

globals()

hasattr(object, name)

hash(object)

hex(x)

id(object)

input()
input(prompt)

int(x=0)
int(x, base=10)

__import__(name, globals=None, locals=None, fromlist=(), level=0)

iter(object)
iter(object, sentinel)

isinstance(object, classinfo)

issubclass(class, classinfo)

len(s)

list
list(iterable)

locals()

map(function, iterable, *iterables)

max(iterable, *, key=None)
max(iterable, *, default, key=None)
max(arg1, arg2, *args, key=None)

memoryview(object)

min(iterable, *, key=None)
min(iterable, *, default, key=None)
min(arg1, arg2, *args, key=None)

next(iterator)
next(iterator, default)

object()

open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

ord(c)

pow(base, exp, mod=None)

print(*objects, sep=' ', end='\n', file=None, flush=False)

property(fget=None, fset=None, fdel=None, doc=None)

range(stop)
range(start, stop, step=1)

repr(object)

reversed(seq)

round(number, ndigits=None)

set
set(iterable)

setattr(object, name, value)

sorted(iterable, *, key=None, reverse=False)

str(object='')
str(object=b'', encoding='utf-8', errors='strict')

vars()
vars(object)

zip(*iterables, strict=False)

          ''')
    changecolor("c")

def stop(a):
    import time
    import sys
    time.sleep(a)
    sys.exit()

#for Pygame
    
class Sprite:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x,y,width,height,)
        self.derection = "none"
        
class Sprite2:
    def __init__(self, x, y, width, height, ip):
        self.rect = pygame.Rect(x,y,width,height)
        self.oimg = pygame.image.load(ip)
        self.img = pygame.transform.scale(self.oimg, (self.rect.width,self.rect.height))
        self.direction = "none"
       
#for Magic 

class User:
    def __init__(self,Username,Password):
        self.Username = Username
        self.Password = Password
        self.Inventory = {"cooper pixake" : 1}
        self.Hp = 250
        self.Mp = 150
        self.mHp = 250
        self.mMp = 150        
        self.NBTs = "noEf"
    def save(self):
        written = self.Username+"  "+self.Password+"  "+str(self.Hp)+"  "+self.NBTs+"  "
        file = open(self.Username+".txt",'x')
        file.write(written)
        file.write(str(self.Inventory))

def RegisterToMagic(Username1,Password1):
    Username1 = User(Username1,Password1)
    User.save(Username1)
def Clear():
    file = open("data.txt",'w')
    file.write("")
            