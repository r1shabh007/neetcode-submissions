class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen = {letter: 0 for letter in t} # setting up blank + target dicts
        target = {}
        for i in t:
            target[i] = target.get(i, 0) + 1 

        conditions_met = 0
        TLEN = len(target)
        res = (0, len(s) - 1)
        l = 0
        for r in range(len(s)):
            if s[r] in seen:
                seen[s[r]] += 1
                if seen[s[r]] == target[s[r]]:
                    conditions_met += 1
            while conditions_met == TLEN:
                if res[1]-res[0] > r - l:
                    res = (l, r)
                if s[l] in seen:
                    seen[s[l]] -= 1
                    if seen[s[l]] < target[s[l]]:
                        conditions_met -= 1
                l += 1
            # print("l: ", l, "r: ", r)
            # print("conditions_met: ", conditions_met, "tlen", TLEN)
        
        return s[res[0]:res[1]+1] if l > 0 else ""