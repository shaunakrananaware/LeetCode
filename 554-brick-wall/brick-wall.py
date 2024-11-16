class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        creases = [[] for _ in range(len(wall))]

        for idx in range(len(wall)):
            current_row = wall[idx]
            current_brick = 0
            
            for jdx in range(len(current_row)-1):
                creases[idx].append(current_row[jdx]+current_brick)
                current_brick += current_row[jdx]
        
        counter = defaultdict(int)
        for i in creases:
            for j in i:
                counter[j] += 1
        
        if not counter:
            return len(wall)

        max_freq = max(counter, key=lambda x: counter[x])
        res = len(wall) - counter[max_freq]

        return res
