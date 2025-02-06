class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        f={}
   
        l=list(s.split(" "))
        print(l)
        if len(pattern)!=len(l):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in f:
                if l[i] in f.values():
                    return False
                f[pattern[i]]=l[i]
            else:
                if f[pattern[i]]!=l[i]:
                    return False

        return True

        