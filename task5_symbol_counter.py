
test_string = "i'll bring the yeyo myself"

def counter_for_symbols(work_string):
	uniq_symbols_set = set()
	for symbol in work_string:
		uniq_symbols_set.add(symbol)
	
	for uniq_symbol in uniq_symbols_set:
		counter = 0
		for symbol in work_string:
			if uniq_symbol == symbol:
				counter = counter + 1
		print("Symbol: ", uniq_symbol," Couneter: ", counter)
	

counter_for_symbols(test_string)

