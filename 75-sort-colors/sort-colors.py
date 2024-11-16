class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0]*3
        for i in nums: bucket[i] += 1

        i = 0
        for jdx in range(len(bucket)):
            for k in range(bucket[jdx]):
                nums[i] =  jdx
                i += 1
