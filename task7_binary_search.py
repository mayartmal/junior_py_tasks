

value = 31
data = [1, 1, 6, 7, 8, 9, 31, 4, 6, 9, 3] 


def binary_search(value, data):
	data.sort()
	print(data)
	mid = len(data) // 2
	low = 0
	high = len(data) - 1
	while data[mid] != value and low <= high:
	    if value > data[mid]:
	        low = mid + 1
	    else:
	        high = mid - 1
	    mid = (low + high) // 2

	if low > high:
	    print("No value")
	else:
	    print("id =", mid)



binary_search(value, data)
 
#id = len(a) // 2
#low = 0
#high = len(a) - 1
 
#while a[mid] != value and low <= high:
#    if value > a[mid]:
#        low = mid + 1
#    else:
#        high = mid - 1
#    mid = (low + high) // 2
 
#if low > high:
#    print("No value")
#else:
#    print("ID =", mid)