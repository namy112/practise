# we define a decorator
# def log(original_function):
#     def new_function(*args, **kwargs):
#         with open("log.txt", "w") as logfile:
#             logfile.write("Function '%s' called with positional arguments %s and keyword arguments %s.\n" % (original_function.__name__, args, kwargs))
# 
#         return original_function(*args, **kwargs)
# 
#     return new_function
# 
# # here is a function to decorate
# def my_function(message):
#     print(message)
# 
# # and here is how we decorate it
# my_functionCall = log(my_function)
# my_functionCall("Hello2")



# with open("mydata.txt", mode="w") as myFile:
#  
#     # You can write to the file with write
#     # It doesn't add a newline
#     myFile.write("Some random text\nMore random text\nAnd some more")
#     
# with open("mydata.txt") as myFile:   
#     print(myFile.read())
#     


oneTo10 = range(1, 11)
 
# The function to pass into map
def dbl_num(num):
    return num * 2
 
# Pass in the function and the list to generate a new list
print(type(map(dbl_num, oneTo10)))
 
# You could do the same thing with a lambda