class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        if n == 0 or n == 1:
            return 1
        dp[0] = 1
        dp[1] = 1
        for j in range(2,n+1):
            dp[j] = dp[j-1] + dp[j-2]
        return dp[n]

            
            