class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n<=k and m<=k:
            return 0
        if m>k:
            return k*(m-k)
        if n>k:
            return k*(n-k)
        