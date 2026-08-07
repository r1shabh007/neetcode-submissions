class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            #check for anagram
            letters = [0] * 26
            for i in s:
                letters[ord(i) - 97] += 1
            for i in t:
                letters[ord(i) - 97] -= 1
                if letters[ord(i) - 97] < 0:
                    return False
            return True
        else:
            return False
        