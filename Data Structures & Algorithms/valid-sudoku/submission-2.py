class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Given 9x9 grid

        # 9 sets for cols
        # 1 set for current row
        # 3 sets for 3x3 block
        # Enumerate and iterate.

        cols: list[set[int]] = [set() for _ in range(9)]

        for i in range(9):
            row = set()
            if (i % 3) == 0:
                blocks = [set() for _ in range(3)]
            for j, x in enumerate(board[i]):
                col = cols[j]
                block = blocks[j//3]
                if x == '.':
                    continue
                elif x in col or x in block or x in row:
                    return False
                elif x != '.':
                    col.add(x)
                    row.add(x)
                    block.add(x)
        return True
        