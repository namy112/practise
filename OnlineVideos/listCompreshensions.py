
# ---------- PROBLEM ----------
# Generate a list of 50 random values between 1 and 1000
# and return those that are multiples of 9
# You'll have to use a list comprehension in a list comprehension
# This is a hard one!


import random

print([x for x in [random.randint(1,1001) for i in range(50)] if x %9 ==0]) 


