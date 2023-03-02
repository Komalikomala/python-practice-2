Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # COMPARISON AND LAGICAL OPERATERS :
>>> # a = b+c (b+c is a operands and (+) is addition operaters) :
>>> #EX 01
>>> a = 7
>>> b = 16
>>> print(a>b)
False
>>> print(a<b)
True
>>> print(a==b)
False
>>> print(a!=b)
True
>>> print(a>=b)
False
>>> print(a<=b)
True
>>>  print(25>24 and 32==34)
 
SyntaxError: unexpected indent
>>> print(25>24 and 32==34)
False
>>> print(25>24 and 32==32)
True
>>> 
>>> #COMPLIMENT :NOT
>>>  print( not True )
 
SyntaxError: unexpected indent
>>> print(not True)
False
>>> print(not flase)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(not flase)
NameError: name 'flase' is not defined
>>> print(not False)
True
>>> 
>>> #BINARY NUMBERS (0,1)
>>> # 0(False) 1(True)
>>> 