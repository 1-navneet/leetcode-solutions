class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def f(n,i,res,sub):
            if i == n:
                res.append(sub.copy())
                return
            
            sub.append(nums[i])
            f(n,i+1,res,sub)
            sub.pop()
            f(n,i+1,res,sub)
        res = []
        f(len(nums),0,res,[])
        return res