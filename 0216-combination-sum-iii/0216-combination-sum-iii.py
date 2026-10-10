class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
    
        def f(i,res,sub):

            if len(sub) == k:
                if sum(sub) == n:
                    res.append(sub.copy())
                return
            
            if i >= 10:
                return
  
            
            sub.append(i)
            f(i+1,res,sub)
            sub.pop()
            f(i+1,res,sub)
        res = []
        f(1,res,[])
        return res