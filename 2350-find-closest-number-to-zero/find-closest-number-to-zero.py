class Solution(object):
    def findClosestNumber(self, nums):
        menor = 100001
        for i in range(len(nums)):
            if menor >= abs(nums[i]):
                menor = abs(nums[i])
        
        if menor*(-1) in nums:
            if menor not in nums:
                return menor*(-1)
        return menor
        