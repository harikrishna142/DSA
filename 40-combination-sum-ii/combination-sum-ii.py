class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def back(i,c,t):
            if t==target and c not in res:
                res.append(c[:])
                return
            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if t+candidates[j]>target:
                    break
                c.append(candidates[j])
                back(j+1,c,t+candidates[j])
                c.pop()
        back(0,[],0)
        return res
        