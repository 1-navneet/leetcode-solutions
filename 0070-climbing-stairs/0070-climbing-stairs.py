class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        prev0 = 1
        prev1 = 1
        curr = 0
        for i in range(2,n+1):
            curr = prev0 + prev1
            prev0 = prev1
            prev1 = curr
        return prev1


            
            