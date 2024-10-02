class Solution:
    
    @staticmethod
    def binarySearch(nums: List[int], key: int) -> bool:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (right+left) // 2
            if key == nums[mid]: return True
            if key < nums[mid]:
                right = mid - 1
                continue
            left = mid+1

        return False

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()

        return [i for i in range(1, len(nums)+1) if not Solution.binarySearch(nums, i)]