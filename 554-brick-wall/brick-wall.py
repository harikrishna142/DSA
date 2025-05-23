class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        m=len(wall)
        s=set()
        for i in wall:
            s.add(i[0])
            for j in range(1,len(i)):
                i[j]+=i[j-1]
                s.add(i[j])
        s=list(s)
        s.sort()
        
        for i in s[:-1]:
            c=0
            for j in wall:
                if i not in j:
                    c+=1
            m=min(c,m)
        return m



        