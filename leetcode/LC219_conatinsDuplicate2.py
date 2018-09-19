"""Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array 
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true""
"""

class Solution(object):
    
    def isTrue(self, indexes,k):
        
        for i in range(len(indexes)):
            for j in range(i+1,len(indexes)):
                absDiff= abs(indexes[i]-indexes[j])
                if absDiff <= k:
                    return True
        return False
        
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 8: 06
        if not nums:
            return False

        tempDict = {} #1:0, 0:1 , 1 :2, 1:3
        absDiff=0
        for i in range(len(nums)): #4
            if nums[i] not in tempDict:
                tempDict[nums[i]]=[i] 
            else:
                tempDict[nums[i]].append(i)
                if self.isTrue(tempDict[nums[i]],k): #[0,2,3], 3
                     return True
        return False
    # 9: 12
    
"""NotesToME:

use enumerate() 
 dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
"""