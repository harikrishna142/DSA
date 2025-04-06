class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        com=[]
        candidates.sort()
        def back(i):
            if sum(com)==target and com not in res:
                res.append(com[:])
                return
            for j in range(i,len(candidates)):
                if sum(com)>target:
                    return
                com.append(candidates[j])
                back(j)
                com.pop()
        back(0)
        return res
        