class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        LENGTH = len(nums)
        products = [1] * LENGTH
        #going forwards
        cofactor_fwd = 1
        for i in range(LENGTH - 1):
            cofactor_fwd *= nums[i]
            products[i + 1] *= cofactor_fwd
        #going backwards
        cofactor_bwd = 1
        for i in range(LENGTH - 1, 0, -1):
            cofactor_bwd *= nums[i]
            products[i - 1] *= cofactor_bwd
        return products