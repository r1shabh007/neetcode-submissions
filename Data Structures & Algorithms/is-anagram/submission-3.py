class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            #anagram code
            letters = {}
            for i in s:
                letters[i] = letters.get(i, 0) + 1
            for i in t:
                if i in letters:
                    letters[i] -= 1
                    if letters[i] < 0:
                        return False
                else:
                    return False
            return True 
        else:
            return False