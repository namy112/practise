
def toLowerCase( str):
    """
    :type str: str
    :rtype: str
    """
    result = ''
    for letter in str:
        print(ord(letter))
        if ord(letter) > 64 and ord(letter) < 91:
            result = result + chr(ord(letter) + 32)
        else:
            
            result = result + letter
          
    return result



print (toLowerCase('HellO'))