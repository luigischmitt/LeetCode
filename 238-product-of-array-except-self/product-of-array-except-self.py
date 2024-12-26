class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        resposta = [1] * n

        # Calculate prefix products
        prefix = 1
        for i in range(n):
            resposta[i] = prefix
            prefix *= nums[i]

        # Calculate suffix products and multiply with prefix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            resposta[i] *= suffix
            suffix *= nums[i]

        return resposta
        