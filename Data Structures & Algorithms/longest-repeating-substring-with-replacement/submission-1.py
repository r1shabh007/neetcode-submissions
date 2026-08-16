class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        seen = defaultdict(int)
        max_letter = 0
        res = 0

        res = 0
        for r in range(len(s)):
            seen[s[r]] += 1 # add current letter to seen
            max_letter = max(max_letter, seen[s[r]])
            while r - l + 1 - max_letter > k: #progress left counter if too many replacements
                seen[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1) # update result if current length is bigger
        return res