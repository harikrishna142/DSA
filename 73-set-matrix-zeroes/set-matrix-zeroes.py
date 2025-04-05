class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=[]
        col=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    if i not in row:
                        row.append(i)
                    if j not in col:
                        col.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in col:
                    matrix[i][j]=0
        
        
                    
        

        """
        Do not return anything, modify matrix in-place instead.
        """
        