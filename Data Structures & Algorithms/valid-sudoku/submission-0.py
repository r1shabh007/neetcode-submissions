class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {name: set() for name in range(9)}
        cols = {name: set() for name in range(9)}
        boxes = {name: set() for name in range(9)}

        print(rows, cols, boxes)

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                box = (row // 3) * 3 + (col // 3) # boxes numbered 0 - 9
                if num.isdigit():
                    if num in rows[row] or num in cols[col] or num in boxes[box]:
                        return False
                rows[row].add(num)
                cols[col].add(num)
                boxes[box].add(num)
        return True
                
        
