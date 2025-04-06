class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def back(i,c,t):
            if t==target:
                res.append(c[:])
                return
            for j in range(i,len(candidates)):
                if t>target:
                    return
                c.append(candidates[j])
                back(j,c,t+candidates[j])
                c.pop()
        back(0,[],0)
        return res
        