class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        f={}
        k=""
        for i in strs:
            k="".join(sorted(i))
            if k not in f:
                f[k]=[i]
            else:
                f[k].append(i)
            
        return list(f.values())

        