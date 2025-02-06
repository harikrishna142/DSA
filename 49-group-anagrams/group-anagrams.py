class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        f=collections.defaultdict(list)
        k=""
        for i in strs:
            k="".join(sorted(i))
            f[k].append(i)
            
        return list(f.values())

        