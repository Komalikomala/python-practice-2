Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Accesessing  Elements in python
>>> name = 'komalivenkatesh'
>>> age = 22
>>> text = my name is komala and my
SyntaxError: invalid syntax
>>> text = ''' my name is komala
... my father name is venkatesh
... my mother name is amaravathi'''
>>> print(name[2])
m
>>> print(text[13])
o
>>> name = 'koamlivenkatesh'
>>> age = '22'
>>> text = '''my name is komala
...                 my father name is venkatesh
...                             my mother name is amara'''
>>> print('''text''')
text
>>> print(text)
my name is komala
                my father name is venkatesh
                            my mother name is amara
>>> name = 'komali'
>>> age = '22'
>>> text = '''komali
... vrnkatesh
... amaravathi'''
>>> print(text[0:1:2:3:4:])
SyntaxError: invalid syntax
>>> print(name[0:5])
komal
>>> print(name[0:4])
koma
>>> print(name[0])
k
>>> print(name[0:6])
komali
