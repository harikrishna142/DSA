class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #g=collections.defaultdict(int)
        g=Counter(magazine)
        #for i in range(len(magazine)):
        #    g[magazine[i]]+=1
        for i in range(len(ransomNote)):
            if ransomNote[i] in g and g[ransomNote[i]]>=1:
                    g[ransomNote[i]]-=1

            else:
                return False
        return True
        