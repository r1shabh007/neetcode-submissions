class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            #check for anagram
            letters = [0] * 26
            for i in s:
                index_i = ord(i) - 97
                letters[index_i] += 1
            for i in t:
                index_i = ord(i) - 97
                letters[index_i] -= 1
                if letters[index_i] < 0:
                    return False
            return True
        else:
            return False
        