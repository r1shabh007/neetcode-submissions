class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.word = True

    def search(self, word: str) -> bool:
        
        def dfs(word, root):
            curr = root
            for i in range(len(word)):
                l = word[i]
                while l == ".":
                    for roots in curr.children.values():
                        if dfs(word[i + 1:], roots):
                            return True
                    return False
                
                if l not in curr.children:
                    return False
                curr = curr.children[l]
            return curr.word
        return dfs(word, self.root)
