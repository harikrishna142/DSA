class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        h=[]
        for i in range(1,n+1):
            if n%i==0:
                heapq.heappush(h,-i)
                while len(h)>k:
                    heapq.heappop(h)
        if len(h)<k:
            return -1
        else:
            return -h[0]
        