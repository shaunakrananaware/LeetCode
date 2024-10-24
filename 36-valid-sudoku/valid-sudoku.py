class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for idx in range(9):
            for jdx in range(9):
                current = board[jdx][idx]
                if current == '.': continue
                if (
                    current in row[jdx] or
                    current in col[idx] or
                    current in square[(jdx // 3, idx // 3)] 
                ):
                    return False
                row[jdx].add(current)
                col[idx].add(current)
                square[(jdx // 3, idx // 3)].add(current)

        return True