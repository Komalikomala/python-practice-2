Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #LISTS IN PYTHON (ACCESSES, MAODIFY, REMOVE AND INSERT ELEMENTS):
>>> #LIST : list is a collection of elements (or) collection of variables
>>> products = ["mask", "shield", "covidkit"]
>>> print(products)
['mask', 'shield', 'covidkit']
>>> print(products[1])
shield
>>> print(products[0])
mask
>>> print(products[2])
covidkit
>>> # Now we r change shield into faceshield :
>>> products[1] = "faceshield"
>>> print(products)
['mask', 'faceshield', 'covidkit']
>>> 
>>> #Accesses :
>>> print(products[1:3])
['faceshield', 'covidkit']
>>> print(products[0:3])
['mask', 'faceshield', 'covidkit']
>>> print(products[1:2])
['faceshield']
>>> 
>>> # Now we r Remove elements .pop()//.Remove() and #inser elements-, insert index, "value"
>>> #Example 01
>>> products = ["mask", "shield", "covidkit"]
>>> products.pop(2)
'covidkit'
>>> print(products)
['mask', 'shield']
>>> products.pop(1)
'shield'
>>> print(products)
['mask']
>>> products.pop(3)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    products.pop(3)
IndexError: pop index out of range
>>> 
>>> # Example 02
>>> products = ["mask", "shield", "covidkit"]
>>> products.remove("shield")
>>> print(products)
['mask', 'covidkit']
>>> products.remove("covidkit")
>>> print(products)
['mask']
>>> products.remove("mask")
>>> print(products)
[]
>>> 
>>> # Example 03
>>> products = ["mask", "shield", "covidkit"]
>>> products.insert(1, "spray")
>>> print(products)
['mask', 'spray', 'shield', 'covidkit']
>>> 
>>> # Example 04
>>> products = ["mask", "shield", "covidkit"]
>>> products.insert(len(products), "spray")
>>> print(products)
['mask', 'shield', 'covidkit', 'spray']
>>> 