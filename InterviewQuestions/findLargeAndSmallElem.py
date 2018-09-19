


def findMinAndMax(inputList):

    min=inputList[0]
    max=inputList[0]
    
    for  elem in inputList:
        if elem < min:
            min = elem
        if elem > max:
            mac= elem
    print(min,max)
    
    


a =[9,3,6,8,2,8]

findMinAndMax(a)