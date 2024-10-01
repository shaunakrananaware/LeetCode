class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr) - 1
        currentMax = arr[size]
        prevMax = 0
        arr[size] = -1
        
        for i in range(size-1, -1, -1):
            if currentMax < arr[i]:
                prevMax = currentMax
                currentMax = arr[i]
                arr[i] = prevMax
                continue
                 
            arr[i] = currentMax
        return arr
