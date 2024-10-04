class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set()
        nums_freq = Counter(nums1)

        for i in nums2:
            if i not in nums_freq:
                continue
            intersection.add(i)
        
        return intersection