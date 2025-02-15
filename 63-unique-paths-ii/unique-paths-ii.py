class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid=obstacleGrid
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            if grid[i][0]==1 or dp[i-1][0]==-1:
                dp[i][0]=-1
            else:
                dp[i][0]=1
        for j in range(n):
            if grid[0][j]==1 or dp[0][j-1]==-1:
                dp[0][j]=-1
            else:
                dp[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j]==1:
                    dp[i][j]=-1
                    continue
                if dp[i-1][j]==-1 and dp[i][j-1]==-1:
                    dp[i][j]=-1
                elif dp[i-1][j]==-1:
                    dp[i][j]=dp[i][j-1]
                elif dp[i][j-1]==-1:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        if dp[-1][-1]==-1:
            return 0
        return dp[-1][-1]

        
        