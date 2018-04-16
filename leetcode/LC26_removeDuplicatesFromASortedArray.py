class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count=1
        last_index_pos=1
        
        
        if len(nums)<0:
            return 0
        
        if len(nums)==1:
            return 1
        
        if len(nums)>1:
            for i in range(len(nums)-1):
                if nums[i]!=nums[i+1]:
                    count +=1
                    nums[last_index_pos]= nums[i+1] # Here you swap the last_index posotion with the unique value you recieved.
                    last_index_pos +=1
                
        
        
            return count
            
            
#Given nums = [0,0,1,1,1,2,2,3,3,4],

#Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

#It doesn't matter what values are set beyond the returned length.
        