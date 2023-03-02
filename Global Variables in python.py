Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #	GLOBAL VARIABELS
>>> x = "awesome"
>>> 
>>> def myfunc():
	print("python is " + x)

	
>>> myfunc()
python is awesome
>>> #Example 02
>>> x = "komala"
>>> 
>>> def myfunc():
	print("myname is " + x)

	
>>> myfunc()
myname is komala
>>> 
>>> #Example 03
>>> x = "awesome"
>>> 
>>> def myfunc():
	print("python is " + x)

	
>>> myfunc()def myfunc():
	print("python is " + x)
	
SyntaxError: invalid syntax
>>> 
>>> #Example 03
>>> x = "awesome"
>>> 
>>> def myfunc():
	x = "fantastic"
	print("python is " + x)

	
>>> myfunc()
python is fantastic
>>> 
>>> print("python is " + x)
python is awesome
>>> 
>>> #Example 04
>>> def myfunc():
	global x
	x = "fantastic"

	
>>> myfunc()
>>> 
>>> print("python is
      
SyntaxError: EOL while scanning string literal
>>> print("python is " + x)
python is fantastic
>>> 
>>> #Example 05
>>> x = "fantastic"
>>> 
>>> def myfunc():
	global x
	x = "fantastic"

	
>>> myfunc()
>>> 
>>> print("python is " + x)
python is fantastic
>>> 
>>> print("python is " + x)
python is fantastic
>>> 
>>> 
>>> #Example 05
>>> 
>>> x = "awesome"
>>> 
>>> def myfunc():
	global x
	x = "fantastic"

	
>>> myfunc()
>>> 
>>> print("python is " + x)
python is fantastic
>>> print("python is " + x)
python is fantastic
>>> 