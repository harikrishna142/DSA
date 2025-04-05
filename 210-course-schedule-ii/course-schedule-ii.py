from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> list:
        n=numCourses
        pre=prerequisites
        taken=[]
        p=defaultdict(list)
        for i in pre:
            p[i[0]].append(i[1])
        s=[0]*n
        def dfs(c):
            if s[c]==2:
                return True
            elif s[c]==1:
                return False
            s[c]=1
            for j in p[c]:
                if not dfs(j):
                    return False
            s[c]=2
            taken.append(c)
            return True

        for i in range(n):
            if not dfs(i):
                return []


        return taken

        
        
        