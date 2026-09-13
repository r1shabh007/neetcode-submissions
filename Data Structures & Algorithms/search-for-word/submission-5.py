class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(board, word, c, i, j, checked):
            if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1 or (i, j) in checked:
                return False
            if board[i][j] != word[c]:
                return False
            if c == len(word) - 1:
                return True
            checked.append((i, j))
            c += 1
            found = (check(board, word, c, i - 1, j, checked) or 
                     check(board, word, c, i + 1, j, checked) or
                     check(board, word, c, i, j + 1, checked) or
                     check(board, word, c, i, j - 1, checked))
            checked.pop()
            return found
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if check(board, word, 0, i , j, []):
                    return True
        return False
                