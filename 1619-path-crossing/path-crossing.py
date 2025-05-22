class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited=set()
        i=j=0
        visited.add((i,j))
        for k in range(len(path)):
            if path[k]=="N":
                j-=1

            elif path[k]=="E":
                i+=1

            elif path[k]=="S":
                j+=1

            else:
                i-=1
            if (i,j) in visited:
                return True
            else:
                visited.add((i,j))
        return False


        