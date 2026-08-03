class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subs(i,res,sub):
            if i >= len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            subs(i+1,res,sub)
            sub.pop()
            subs(i+1,res,sub)
        res = []
        subs(0,res,[])
        return res
        
    
        
        

        