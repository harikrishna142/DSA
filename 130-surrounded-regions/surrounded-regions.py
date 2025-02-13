class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        def dfs(i,j):
            if i<0 or j<0 or i>m-1 or j>n-1 or board[i][j]!="O":
                return
            board[i][j]="-1"
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i+1,j)

        for i in range(m):
            for j in range(n):
                if i in [0,m-1] or j in [0,n-1]:
                    if board[i][j]=="O":
                        dfs(i,j)
        for i in range(m):
            for j in range(n):
                
                if board[i][j]=="-1":
                    board[i][j]="O"
                else:
                    board[i][j]="X"
        
            

            

        """
        Do not return anything, modify board in-place instead.
        """
        