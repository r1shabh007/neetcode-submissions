class Node:
    def __init__(self):
        self.children = {}
        self.wordExists = False
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #init trie
        root = Node()
        res = set()
        seen = set()
        row = len(board)
        col = len(board[0])

        for word in words:
            curr = root
            for i in word:
                if not i in curr.children:
                    curr.children[i] = Node()
                curr = curr.children[i]
            curr.wordExists = True
            curr.word = word
        
        def dfs(i, j):
            if i < 0 or i > row - 1 or j < 0 or j > col - 1 or (i, j) in seen:
                return

            nonlocal res
            nonlocal curr
            letter = board[i][j]
            #print(letter, curr.children.keys())
            if letter in curr.children.keys():
                prev = curr
                curr = curr.children[letter]
                seen.add((i, j))
                if curr.wordExists:
                    res.add(curr.word)
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)
                seen.remove((i, j))
                curr = prev

        for i in range(row):
            for j in range(col):
                curr = root
                dfs(i, j)
        
        #print(curr.children["b"].children["a"].children["c"].children["k"].wordExists)
        return list(res)
        

