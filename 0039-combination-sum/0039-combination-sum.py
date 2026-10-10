class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def f(i,res,sub,n):

            if sum(sub) == target:
                res.append(sub.copy())
                return
            
            if i == n:
                return 
            if sum(sub) > target:
                return
            
            
            sub.append(candidates[i])
            f(i,res,sub,n)
            sub.pop()
            f(i+1,res,sub,n)
        res = []
        n = len(candidates)
        f(0,res,[],n)
        return res
        

