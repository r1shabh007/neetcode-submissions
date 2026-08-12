class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res += [str(len(word)), "#", word]
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0

        while i < len(s):
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res

                
            

                
