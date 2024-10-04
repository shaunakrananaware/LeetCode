class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        natural_nums = {i: 1 for i in range(1, len(nums)+1)}
        error = [0, 0]

        for i in nums:
            natural_nums[i] -= 1
        
        for key, value in natural_nums.items():
            if value == -1: error[0] = key
            if value == 1: error[1] = key
        
        return error

