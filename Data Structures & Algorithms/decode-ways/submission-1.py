class Solution:
    def numDecodings(self, s: str) -> int:
        n1, n2 = (0, 1), (0, 1) #num, max
        for i in s:
            combined = int(str(n2[0]) + str(i))
            print(combined)
            maxnums = 0
            if combined >= 10 and combined <= 26:
                maxnums += n1[1]
            if i != '0':
                maxnums += n2[1]
            if i == '0' and (combined < 10 or combined > 26):
                return 0
            n1 = n2
            n2 = (i, maxnums) 
        return n2[1]