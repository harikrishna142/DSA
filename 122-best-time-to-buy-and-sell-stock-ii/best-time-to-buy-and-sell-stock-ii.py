class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi=prices[0]
        m=0
        for i in range(len(prices)):
            mi=min(mi,prices[i])
            if prices[i]>mi:
                m=m+(prices[i]-mi)
                mi=prices[i]
        return m

        