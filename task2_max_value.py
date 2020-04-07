values = [1, 2, -1, 10, -10]

def max_value_fun(a) :
	max_value = None
	for number in a:
	    if max_value is None:
	        max_value = number
	    if number > max_value:
	        max_value = number
	print("result is ", max_value)


max_value_fun(values)