class Solution:
    def reverseDegree(self, s: str) -> int:
        sume = 0
        for i in range(len(s)):
            r = 26 - (ord(s[i]) - ord('a'))
            sume += r * (i+1)

        return sume



