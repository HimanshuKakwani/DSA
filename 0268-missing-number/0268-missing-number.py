class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res1 = len(nums)
        
        for i in range(len(nums)):
            res1 += (i - nums[i])            
        return(res1)