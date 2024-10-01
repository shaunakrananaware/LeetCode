class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCount = {}
        
        for i in nums:
            if i not in numCount:
                numCount[i] = 1
                continue
            
            numCount[i] += 1

        return max(numCount, key=lambda x: numCount[x])

