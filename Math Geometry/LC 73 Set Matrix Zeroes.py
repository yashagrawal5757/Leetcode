class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_zero,col_zero = 0,0 #change them to 1 if 0th row or 0th col contains natural zeros

        for i in range(0,m):
            if matrix[i][0] == 0:
                col_zero = 1
        for j in range(0,n):
            if matrix[0][j] == 0:
                row_zero = 1
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  #same row, 0th column set to zero
                    matrix[0][j] = 0 #same column, 0th row set to zero
        
        #Zero out now
        #Go over all rows from 1st (you dont want to disturb 0th row as its marker)
        for i in range(1,m):
            if matrix[i][0] == 0:
                #zero out ith row
                for col in range(0,n):
                    matrix[i][col] = 0
        #Go over all cols
        for j in range(1,n): #(you dont want to disturb 0th column as its marker)
            if matrix[0][j] == 0:
                #zero out jth col
                for row in range(0,m):
                    matrix[row][j] = 0
            
        #Check row_zero & col_zero value
        if row_zero == 1:
            #zero out 0th row
            for col in range(0,n):
                matrix[0][col] = 0
        if col_zero == 1:
            #zero out 0th column
            for row in range(0,m):
                matrix[row][0] = 0

        return matrix