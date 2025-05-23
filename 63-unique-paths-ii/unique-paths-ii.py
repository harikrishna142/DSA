class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for i in range(m)]
        print(dp)
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                    continue
                if i==0 and j==0:
                    dp[i][j]=1
                else:
                    if i==0:
                        dp[i][j]=dp[i][j-1]
                    elif j==0:
                        dp[i][j]=dp[i-1][j]
                    else:
                        
                        dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

        
        