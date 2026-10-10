class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        arr = [1,2,3,4,5,6,7,8,9]
        def f(i,res,sub,l):
            if len(sub) == k:
                if sum(sub) == n:
                    res.append(sub.copy())
                    return

            if i == l:
                return
            
            sub.append(arr[i])
            f(i+1,res,sub,l)
            sub.pop()
            f(i+1,res,sub,l)
        res = []
        l = len(arr)
        f(0,res,[],l)
        return res