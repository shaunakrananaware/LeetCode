class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = nums[0] < nums[len(nums)-1]
        if not increasing:
            nums = nums[::-1]
        
        for idx in range(len(nums)-1):
            if nums[idx] > nums[idx+1]:
                return False
            
        return True