



def fib (num):
	
	if num == 0:
		return 0
	elif num == 1:
		return 1
	 
	else:
		result = fib(num-1) + fib(num-2)
		return result
	
	


print(fib(4))