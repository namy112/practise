# ---------- PROBLEM ----------
# Create a function that receives a list and a function
# The function passed will return True or False if a list
# value is odd.
# The surrounding function will return a list of odd
# numbers



def check_if_odd(num):
    
    if num % 2 == 0:
        return False
    else:
        return True
    

def calucate(list, check_if_odd):
    oddlist =[]  
    for i in list:
        if check_if_odd(i):
            oddlist.append(i)
            
    return oddlist       
alist = range (1,20)

print calucate(alist, check_if_odd)