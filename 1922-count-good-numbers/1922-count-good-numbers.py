class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10**9) + 7
        even_cnt = (n+1)//2
        odd_cnt = n//2
        a = pow(5,even_cnt,MOD)
        b = pow(4,odd_cnt,MOD)
        result = (a * b) % MOD
        return result        

        