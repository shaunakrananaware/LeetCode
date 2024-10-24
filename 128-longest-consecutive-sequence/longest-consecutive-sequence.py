class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0

        for i in nums:
            if i-1 in nums_set: continue
            length = 0
            while i+length in nums_set: length += 1
            longest_seq = max(longest_seq, length)

        return longest_seq

        