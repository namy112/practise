#Create an array of customer dictionaries
# Output should look like this
'''
Enter Customer (Yes/No) : y
Enter Customer Name : Derek Banas
Enter Customer (Yes/No) : y
Enter Customer Name : Sally Smith
Enter Customer (Yes/No) : n
Derek Banas
Sally Smith
'''


# Does the user wish to enter a customer t


customerdict= []

while True:
    enterCustiomer =raw_input("Enter customer(Y/N) " )
    enterCustiomer = enterCustiomer.lower()
   
    if enterCustiomer == 'y':
        
        
        enterName= raw_input("Enter customer name ")
        flname, lname= enterName.split()
        
        # saving the entered customer inndictiornary
        customerdict.append({'flname': flname, 'lname': lname})
    else:
        break


#printing the entereted customers
for cust in customerdict:
    print (cust['flname'], cust['lname'])
    