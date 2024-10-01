class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted_count = 0

        for idx in range(len(flowerbed)):
            if flowerbed[idx] != 0:
                continue

            empty_left = (idx == 0) or not flowerbed[idx-1]
            empty_right = (idx == len(flowerbed)-1) or not flowerbed[idx+1]

            if empty_left and empty_right:
                flowerbed[idx] = 1
                planted_count += 1
            
            if planted_count >= n:
                return True
        
        return planted_count >= n
