class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[] for _ in range(n)]
        dp[0].append(triangle[0][0])
       
        for i in range(1,n):
            for j in range(len(triangle[i])):
                if j==0:
                    dp[i].append(triangle[i][j]+dp[i-1][j])
                   
                elif j==len(triangle[i])-1:
                    dp[i].append(triangle[i][j]+dp[i-1][j-1])
                else:
                    dp[i].append(triangle[i][j]+min(dp[i-1][j],dp[i-1][j-1]))
        return min(dp[-1])

        