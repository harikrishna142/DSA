class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=False
        col=False
        for i in matrix[0]:
            if i==0:
                row=True
                break
        for j in range(len(matrix)):
            if matrix[j][0]==0:
                col=True
                break
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        for i in range(1,len(matrix)):
            if matrix[i][0]==0:
                for j in range(1,len(matrix[0])):
                    matrix[i][j]=0
        for j in range(1,len(matrix[0])):
            if matrix[0][j]==0:
                for i in range(1,len(matrix)):
                    matrix[i][j]=0
        if row==True:
            for j in range(len(matrix[0])):
                matrix[0][j]=0
        if col==True:
            for i in range(len(matrix)):
                matrix[i][0]=0

            
        
        
                    
        

        """
        Do not return anything, modify matrix in-place instead.
        """
        