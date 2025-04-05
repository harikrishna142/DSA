class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        k=0
        l=[]
        m=len(board)
        n=len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                k=0
                if i<(m-1) and j<(n-1) and board[i+1][j+1]==1:
                    k=k+1
                if j<(n-1) and board[i][j+1]==1:
                    k=k+1
                if i<(m-1) and board[i+1][j]==1:
                    k=k+1
                if j<(n-1) and i>0 and board[i-1][j+1]==1:
                    k=k+1
                if i<(m-1) and j>0 and board[i+1][j-1]==1:
                    k=k+1
                if i>0 and board[i-1][j]==1:
                    k=k+1
                if j>0 and board[i][j-1]==1:
                    k=k+1
                if i>0 and j>0 and board[i-1][j-1]==1:
                    k=k+1
                if k==3:
                    if board[i][j]!=1:
                        l.append([i,j])
                elif k==2:
                    continue
                else:
                    if board[i][j]==1:
                        l.append([i,j])
        for i in l:
            board[i[0]][i[1]]=abs(board[i[0]][i[1]]-1)
                

                

                

        """
        Do not return anything, modify board in-place instead.
        """
        