from StdSuites.AppleScript_Suite import lists
from paramiko.common import one_byte


# 1,5,3
# 1,3,5
# 
# 8,9,2,4
# 2,4,8,9
# 
# 
# [1,2,3,4,5,8,9]

# 1) create a new list with size of both the lists combined
# 2) create a starting pointer for both the lists
# 3) loop through lists
# 4) compare both the list and insert elem into the new lists one by one_byte
# 5) As soon as you place an item in a list update the pointer for that list 



inputList1 = [0,0,0,1,2,3,4]
inputList2 = [3,5,8]

newList = []
list1Pointer = 0
list2Pointer = 0
len1 = len(inputList1)
len2 = len(inputList2)

while len(newList) != len1 +  len2: 
    if list1Pointer< len1 and list2Pointer < len2 and inputList1[list1Pointer] <= inputList2[list2Pointer]:
        newList.append(inputList1[list1Pointer])
        list1Pointer += 1
        
    elif list1Pointer < len1 and list2Pointer < len2 and inputList2[list2Pointer] < inputList1[list1Pointer]:
        newList.append(inputList2[list2Pointer])
        list2Pointer += 1
    
    elif list1Pointer == len1:
        for i in range(list2Pointer, len2):    
         newList.append(inputList2[i])
         
    elif list2Pointer == len2:
        for i in range(list1Pointer, len1):
            newList.append(inputList1[i])
    else:
         print("Please enter non empty lists")


print(newList)
