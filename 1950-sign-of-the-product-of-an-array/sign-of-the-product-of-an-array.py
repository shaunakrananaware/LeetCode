class Solution:
    def arraySign(self, nums: List[int]) -> int:
        isNeg = False
        
        for num in nums:
            if not num: return 0
            if num < 0:
                isNeg = not isNeg
        
        return -1 if isNeg else 1
