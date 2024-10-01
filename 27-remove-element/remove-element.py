class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        MAX_INT = 101
        equal_count = 0

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = MAX_INT
                equal_count += 1
            
        nums.sort()

        return len(nums) - equal_count
            