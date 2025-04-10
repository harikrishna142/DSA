class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        s=[capacity]*1001
        for i in range(len(trips)):
            for j in range(trips[i][1],trips[i][2]):
                s[j]=s[j]-trips[i][0]
                if s[j]<0:
                    return False
        return True
        