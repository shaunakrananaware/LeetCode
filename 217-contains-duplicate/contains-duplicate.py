class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        data = {}
        for i in nums:
            if i in data:
                return True
            data[i] = 1

        return False

                
            
        