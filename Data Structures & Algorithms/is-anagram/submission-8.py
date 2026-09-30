class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = {}
        for i in range(len(s)):
            letters[s[i]] = letters.get(s[i], 0) + 1
            letters[t[i]] = letters.get(t[i], 0) - 1
        return True if set(letters.values()) == {0} else False
