
#sum(1 for i in bin(20)[2:] if i == '1')
a = 2
print (bin(a))

def counter_for_1(raw_data):
	work_data = bin(raw_data)[2:]
	counter_result = 0;
	for symbol in work_data:
		if symbol == "1":
			counter_result = counter_result + 1
	print(counter_result)		

counter_for_1(a)

