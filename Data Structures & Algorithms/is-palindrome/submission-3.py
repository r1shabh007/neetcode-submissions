class Solution:
    def isPalindrome(self, s: str) -> bool:
        STRLEN = len(s)
        s = s.lower()
        i = 0
        k = STRLEN - 1
        while i < k: # while the pointers have not crossed each other
        #make sure both pointers are on letters
            while not s[i].isalnum():
                i += 1
                if i > k:
                    return True
            while not s[k].isalnum():
                k -= 1
                if i > k:
                    return True
            if s[i] != s[k]:
                return False
            i += 1
            k -= 1
        return True
        # i moves right, while k moves left
        #check if the letter is the same
