class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            # create dict of "s" with unique letters set to value of 0
            letters = dict.fromkeys(set(s), 0) 

            for i in s: # iterate through letters and count # of appearances 
                letters[i] += 1

            for i in t:
                if i in letters:
                    letters[i] -= 1
                    if letters[i] < 0:
                        return False
                else:
                    return False

            if set(letters.values()) != {0}:
                return False
                
            return True
            #anagram algorithm
        else:
            return False