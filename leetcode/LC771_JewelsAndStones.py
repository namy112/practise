class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        count=0
        for elemJ in J:
            for elemS in S:
                if elemJ==elemS:
                    count=count+1
        return count
    
    
    
J="aA"
S="aAAbbbb"

test1=Solution()
print(test1.numJewelsInStones(J, S))