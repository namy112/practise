num=1234

result =[]

while num > 0:
    digit = num % 10
    result.append(digit)
    num = num / 10
print(result)



