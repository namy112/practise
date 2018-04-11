class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)< 1:
            return -1
        elif len(s)==1:
                return 0
        else:
            word_dict={}
            for char in s:
                if char in word_dict:
                    word_dict[char] +=1
                else:
                    word_dict[char] =1
        

        for index, char in enumerate(s):
            if word_dict[char] < 2:
                return index
            
        return -1


s1='leetcode'
s2='loveleetcode'
s3='cc'
s4=''
test1=Solution()
print(test1.firstUniqChar(s1))
print(test1.firstUniqChar(s2))
print(test1.firstUniqChar(s3))
print(test1.firstUniqChar(s4))


# More Pythonic way
class Solution(object):

    def firstUniqCharPython(self, s):
            """
            :type s: str
            :rtype: int
            """
            
           
            index=[s.index(l) for l in s if s.count(l) == 1]
            return min(index) if len(index) > 0 else -1
            #print(index)
s1='leetcode'
s2='loveleetcode'
s3='cc'
s4=''
test1=Solution()
print(test1.firstUniqCharPython(s1))
print(test1.firstUniqCharPython(s2))
print(test1.firstUniqCharPython(s3))
print(test1.firstUniqCharPython(s4))  
    