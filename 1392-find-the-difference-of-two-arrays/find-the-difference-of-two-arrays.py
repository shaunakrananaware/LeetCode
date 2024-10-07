class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        res = [set(), set()]

        for i in nums1:
            if i in counter2: continue
            res[0].add(i)
        
        for i in nums2:
            if i in counter1: continue
            res[1].add(i)

        return res
