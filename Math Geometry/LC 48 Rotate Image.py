class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        done = []
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                c = 0
                #Find new location for (i,j)
                if (i,j) in done: 
                    continue
                #start_i,start_j = i,j
                while True:
                    i_new,j_new = j,abs((len(matrix)-1)-i)
                    new_pos = (i_new,j_new)

                    if new_pos in done:
                        break

                    #swap grid cells
                    if c==0:
                        temp1 = matrix[i][j]
                    temp2 = temp1
                    temp1 = matrix[i_new][j_new]
                    matrix[i_new][j_new] = temp2
                    
                    #put in done so that we dont swap this cell again in future
                    done.append((i_new,j_new))
                    i,j = i_new,j_new

                    c+= 1
                

                
        