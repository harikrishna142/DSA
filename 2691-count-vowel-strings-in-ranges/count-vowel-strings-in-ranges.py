class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        p=[0]*len(words)
        p1=[0]*len(words)
        

        c=0
        for i in range(len(words)):
            p1[i]=c
            if words[i][0] in ['a', 'e', 'i', 'o', 'u'] and words[i][-1] in ['a', 'e', 'i', 'o', 'u']:
                c+=1
            p[i]=c
        s=[]
        for i in queries:
            s.append(p[i[1]]-p1[i[0]])

        
        
        return s


