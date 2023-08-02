class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 0
        for i in range(len(nums)-2,0,-1):
            if(nums[i] == nums[i-1] and nums[i] == nums[i+1]):
                nums.pop(i)
                
        return len(nums)
#         for i in range(len(nums)):
#             if nums[a] != nums[i]:
#                 a += 1
#                 nums[a] = nums[i]
                
            
                    