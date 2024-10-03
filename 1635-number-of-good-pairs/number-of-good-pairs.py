class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0

        for idx in range(len(nums)):
            for jdx in range(idx+1, len(nums)):
                if nums[jdx] == nums[idx]:
                    count += 1

        return count 
