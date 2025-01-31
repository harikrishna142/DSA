class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        mi=prices[0]
        ma=0
        for i in range(len(prices)):
            if prices[i]<mi:
                mi=prices[i]
            else:
                ma=max(ma,prices[i]-mi)
        return ma
            

        


        