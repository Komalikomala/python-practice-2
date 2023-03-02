Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #PYTHON LISTS (LIST):
>>> # (LIST IS COLLECTION OF ELEMENTS OR COLLECTION OF VARIABLES):
>>> products = ['bat' , 'ball']
>>> print(products)
['bat', 'ball']
>>> print(type(products))
<class 'list'>
>>> 
>>> #EX 02:
>>> products = ['bat' , 'ball']
>>> price = [6000 , 500]
>>> print(price)
[6000, 500]
>>> print(type(price))
<class 'list'>
>>> 
>>> #EX 03:
>>> # in this program step 2 or 3 boolean datatypes ex 03:
>>> products = ['bat' , 'ball']
>>> price = [6000 , 500]
>>> isAvailable = [True , flase]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    isAvailable = [True , flase]
NameError: name 'flase' is not defined
>>> isAvailable = [True , False]
>>> mixed = [1 , 'virat' , True , 56.799 , [ 12, 54, 777, 98]]
>>> print(mixed)
[1, 'virat', True, 56.799, [12, 54, 777, 98]]
>>> print(type(mixed))
<class 'list'>
>>> 
>>> #EX 04
>>> mixed = [1 , 'virat' , True , 54.799 , [12, 54, 777, 98]]
>>> print(len(mixed))
5
>>> print(mixed[0])
1
>>> print(mixed[-1])
[12, 54, 777, 98]
>>> print(mixed[4][5])
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(mixed[4][5])
IndexError: list index out of range
>>> print(mixed[4][1])
54
>>> 
>>> #EX 05
>>> 
>>> names = list(('komali' , 'komala'))
>>> print(names)
['komali', 'komala']
>>> print(type(names))
<class 'list'>
>>> 
>>> 
>>> #EX 06:
>>> print(mixed)
[1, 'virat', True, 54.799, [12, 54, 777, 98]]
>>> mixed [0] = 18
>>> print(mixed)
[18, 'virat', True, 54.799, [12, 54, 777, 98]]
>>> # WE R REPLACE THE EX 06 STEP IS FIRST NUMBER '1' WE R REPLACE 18 :
>>> 