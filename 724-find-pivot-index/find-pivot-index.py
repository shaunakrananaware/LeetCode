class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        
        sum_left = 0
        sum_right = 0
        for i in nums: sum_right += i

        for idx in range(len(nums)):
            if sum_left == sum_right - nums[idx]: break
            sum_left += nums[idx]
            sum_right -= nums[idx]

        if sum_left != sum_right-nums[idx]:
            return -1
        return idx
