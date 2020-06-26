from src.hello import *

def test_func():
	name = 'Rajesh'
	wish = 'Good Morning'

	assert func() == 'Hello!'
	assert func(name=name) == 'Hello! ' + name
	assert func(wish=wish) == 'Hello! ' + wish
	assert func(name, wish) == 'Hello! ' + name + " " + wish


def test_add():

	assert add(1,2) == 3
	assert add(5,5) == 10
	assert add(5,'a') == 'Invalid arguments'
