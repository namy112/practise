class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        last_non_zero_pos=0
        
        for i in range (len(nums)):
            
            
            if nums[i]!=0:
                
                temp=nums[last_non_zero_pos]
                nums[last_non_zero_pos]= nums[i]
                nums[i]=temp
                last_non_zero_pos +=1
            
        print(nums)
        
s4=[1,0,1]
test1=Solution()
print(test1.moveZeroes(s4))