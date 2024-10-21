class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        output = []
        i,j = 0,0
        visited =  [[-1 for j in range(0,n+1)] for i in range(0,m+1)]
        #-1 denotes unvisited-> We make them 0 when visiting them
        sum = -(m*n)

        #while all nodes are not visited
        while(sum!=0):
            #Move right
            while(j<n and visited[i][j]== -1):
                output.append(matrix[i][j])
                #make it visited
                visited[i][j] = 0
                #increase sum by 1
                sum += 1
                j+= 1
            # j out of bounds reset it to one cell before
            j -= 1
            i += 1 #since we dont want double counting
            #Move down
            while(i<m and visited[i][j]== -1):
                output.append(matrix[i][j])
                visited[i][j] = 0
                sum += 1
                i += 1
            i -= 1 #reset i
            j-= 1
            while(j>=0 and visited[i][j]== -1):
                output.append(matrix[i][j])
                visited[i][j] = 0
                sum += 1
                j -= 1
            j += 1 #reset j
            i-= 1
            #Move up till a visited node comes
            while(i>=0 and visited[i][j]== -1):
                output.append(matrix[i][j])
                visited[i][j] = 0
                sum += 1
                i-= 1
            i+= 1 # reset
            j+= 1
        return output



