class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_triangle = [[1]]
        
        for i in range(1, numRows):
            current_row = []
            for j in range(i + 1):
                if j-1 < 0 or j == len(pascals_triangle[i-1]):
                    current_row.append(1)
                    continue
                
                current_row.append(pascals_triangle[i-1][j-1] + pascals_triangle[i-1][j])
            pascals_triangle.append(current_row)
        
        return pascals_triangle

