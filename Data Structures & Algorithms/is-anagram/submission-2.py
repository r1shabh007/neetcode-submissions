class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            #if same length create a hashmap
            letters = {}
            for i in range(len(s)):
                letters[s[i]] = letters.get(s[i], 0) + 1 
                letters[t[i]] = letters.get(t[i], 0) - 1
            if set(letters.values()) == {0}:
                return True
            else:
                return False
        else: 
            return False
        