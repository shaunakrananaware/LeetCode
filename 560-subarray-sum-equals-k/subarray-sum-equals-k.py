class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] += 1
        current_sum = 0
        res = 0
        
        for i in nums:
            current_sum += i
            if current_sum-k in prefix_sum:
                res += prefix_sum[current_sum-k]
            prefix_sum[current_sum] += 1
            
        return res