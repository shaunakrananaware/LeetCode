class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1

        for idx in range(len(arr)-1, -1, -1):
            new_max = max(current_max, arr[idx])
            arr[idx] = current_max
            current_max = new_max

        return arr