class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        data = {}
        for idx in nums:
            if idx in data:
                return True
            data[idx] = 1

        return False

                
            
        