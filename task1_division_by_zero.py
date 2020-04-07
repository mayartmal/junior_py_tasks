a = 1

def crazy_devisor(a) :
	b = a/0
	return b
try:
	result = crazy_devisor(a)
except:
	result = "sorry, your divirsor is too crazy"

print(result)

