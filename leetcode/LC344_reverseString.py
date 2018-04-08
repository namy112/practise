class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        reversedString=s[::-1]
        
        return reversedString
            
        

test1=Solution()

print(test1.reverseString("hello"))