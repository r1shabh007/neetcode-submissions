class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.wordEnd = True
            
    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return True if curr.wordEnd else False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return True
        