Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# python data types
x = "hello world"
print(type(x))
<class 'str'>
 x = 20
 
SyntaxError: unexpected indent

x = 20
print(type(x))
<class 'int'>
x = 2.0
print(type(x))
<class 'float'>
x = 1j
print(type(x))
<class 'complex'>
x = ["appel", "banana", "mango"]
print(type(x))
<class 'list'>
x = {"name", "komali", "age"}
print(type(x))
<class 'set'>
x = ("cherry", "pineappel", "graphes")
print(type(x))
<class 'tuple'>
x = range(7)
print(type(x))
<class 'range'>
x = {"name": "komali"  "age":36}
SyntaxError: invalid syntax

x = {"name": "komali"  "age":36}
SyntaxError: invalid syntax
x = {"name" : "komali"  "age" : 36}
SyntaxError: invalid syntax
x = {"name" : "komali" , "age" : 36}
print(type(x))
<class 'dict'>
x = frozenset({"appel", "banana" , "cherry"})
print(type(x))
<class 'frozenset'>
x = true
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x = true
NameError: name 'true' is not defined. Did you mean: 'True'?


x = true
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    x = true
NameError: name 'true' is not defined. Did you mean: 'True'?

x = True
print(type(x))
<class 'bool'>
x = b"hello"
print(type(x))
<class 'bytes'>
x = byterray(6)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    x = byterray(6)
NameError: name 'byterray' is not defined. Did you mean: 'bytearray'?
x = bytearray(6)
print(type(x))
<class 'bytearray'>
x = memmoryview
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    x = memmoryview
NameError: name 'memmoryview' is not defined. Did you mean: 'memoryview'?
x = memmoryview(bytes(5)
                print(type(x))
                
SyntaxError: '(' was never closed
SyntaxError: '(' was never closed
                
SyntaxError: invalid syntax
x = memmoryview(bytes(5))
                
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    x = memmoryview(bytes(5))
NameError: name 'memmoryview' is not defined. Did you mean: 'memoryview'?
x = memmoryview(bytes(5))
                
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    x = memmoryview(bytes(5))
NameError: name 'memmoryview' is not defined. Did you mean: 'memoryview'?
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

... 
>>> 

>>> 

... 
>>> x = memmoryview(bytes(6))
...                 
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    x = memmoryview(bytes(6))
NameError: name 'memmoryview' is not defined. Did you mean: 'memoryview'?
>>> x = mememoryview(bytes(7))
...                 
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    x = mememoryview(bytes(7))
NameError: name 'mememoryview' is not defined. Did you mean: 'memoryview'?
>>> x = memoryview(bytes(7))
...                 
>>> print(type(x))
...                 
<class 'memoryview'>
>>> x = None
...                 
>>> print(type(x))
...                 
<class 'NoneType'>
