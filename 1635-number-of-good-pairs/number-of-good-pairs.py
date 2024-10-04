class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_freq = defaultdict(int)
        count = 0

        for i in nums:
            count += nums_freq[i]
            nums_freq[i] += 1

        return count