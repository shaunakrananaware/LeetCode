class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        arr = []

        for idx in range(1, len(nums)+1):
            if idx not in num_set:
                arr.append(idx)

        return arr