class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n=numCourses
        pre=prerequisites
        taken=set()
        p=defaultdict(list)
        for i in pre:
            p[i[0]].append(i[1])
        def dfs(c):
            if not p[c]:
                return True
            if c in taken:
                return False
            taken.add(c)
            for j in p[c]:
                if not dfs(j):
                    return False
            p[c]=[]
            return True

        for i in range(n):
            if not dfs(i):
                return False
        return True

        

       
             

        