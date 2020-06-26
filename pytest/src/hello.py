def func(name = None, wish = None):
	if name and wish:
		return "Hello! " + name + " " + wish
	elif name:
		return "Hello! " + name
	elif wish:
		return "Hello! " + wish
	else:
		return "Hello!"


def add(x, y):
	if isinstance(x, int) and isinstance(y, int):
		return x + y
	else:
		return 'Invalid arguments'