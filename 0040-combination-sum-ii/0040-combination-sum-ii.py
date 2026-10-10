class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def f(i,res,sub,n):

            if sum(sub) == target:
                res.append(sub.copy())
                return

            if i == n:
                return

            if sum(sub) > target:
                return
            
            sub.append(candidates[i])
            f(i+1,res,sub,n)
            sub.pop()
            
            j = i + 1
            while j < n and candidates[i] == candidates[j]:
                j+=1
            f(j,res,sub,n)
        res = []
        candidates.sort()
        n = len(candidates)
        f(0,res,[],n)
        return res
            
            

            