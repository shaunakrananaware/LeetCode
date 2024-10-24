class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        res = list()

        for i in range(k):
            most_freq = max(num_count, key=lambda x: num_count[x])
            res.append(most_freq)
            del num_count[most_freq]
        
        return res