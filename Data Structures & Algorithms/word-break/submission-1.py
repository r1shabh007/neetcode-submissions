class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s): True}
        for i in range(len(s) - 1, -1, -1):
            dp[i] = False
            for word in wordDict:
                if len(word) + i <= len(s) and s[i: i + len(word)] == word:
                    if dp[i + len(word)]:
                        dp[i] = True
        return dp[0]
            
