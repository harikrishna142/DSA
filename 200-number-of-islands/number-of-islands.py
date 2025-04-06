class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1:
                return
            if grid[i][j]=="1":
                grid[i][j]="-1"
                dfs(i,j+1)
                dfs(i,j-1)
                dfs(i+1,j)
                dfs(i-1,j)
            else:
                return
            
        c=0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":

                    c+=1
                    dfs(i,j)
        return c


    
        