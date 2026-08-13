class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        k = len(s) - 1
        while i < k: # while the pointers have not crossed each other
        #make sure both pointers are on letters
            while i < k and not s[i].isalnum():
                i += 1
            while i < k and not s[k].isalnum():
                k -= 1
            if s[i] != s[k]:
                return False
            i += 1
            k -= 1
        return True
        # i moves right, while k moves left
        #check if the letter is the same
