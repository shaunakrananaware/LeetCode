class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = list()
        product = 1
        for i in nums:
            res.append(product)
            product *= i
        
        product = 1
        for idx in range(len(res)-1, -1, -1):
            res[idx] *= product
            product *= nums[idx]
        
        return res