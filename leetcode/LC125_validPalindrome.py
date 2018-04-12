import string
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp= re.sub('[^a-zA-Z0-9]+', '',s) 
        rev_temp=temp[::-1]
    
        if (temp.lower()==rev_temp.lower()):
            return True
        else:
            return False
        
#------------------------------------- Test cases-------------------------------------------
s1='A man, a plan, a canal: Panama'
s2='race a car'
s3='a.'
s4=''
test1=Solution()
print(test1.isPalindrome(s1))
print(test1.isPalindrome(s2))
print(test1.isPalindrome(s3))
print(test1.isPalindrome(s4))
        
# re.sub--> it ignores all the mentioned values inside []. Also , ^ sign means exclude everything expect characters or numbers.
#reversed--> One cannot use lower() on a reversed object. Ex: rev_temp=reversed(temp) and rev_temp.lower() wont work.
#           https://stackoverflow.com/questions/28632804/why-strreversed-doesnt-give-me-the-reversed-string