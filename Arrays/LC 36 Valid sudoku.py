class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # single set approach// Multi Pass solution
        '''
        # Row check
        for i in range(0,9):
            unique = set()
            for j in range(0,9):
                if board[i][j] != '.':
                    if board[i][j] in unique:
                        return False
                    else:
                        unique.add(board[i][j])
        print("Row checked")
        #Column check
        for j in range(0,9):
            unique = set()
            for i in range(0,9):
                if board[i][j] != '.':
                    if board[i][j] in unique:
                        return False
                    else:
                        unique.add(board[i][j])
        print("Column checked")

        #Subbox check
        unique = set()
        c,r = 0,0
        while(r<9): #to go through rows 0-2, 3-5 and 6-8
            c= 0
            while(c<9): #to go through columns 0-2, 3-5 and 6-8
                for i in range(0+r,3+r):  
                    for j in range(0+c,3+c):
                        if board[i][j] != '.':
                            if board[i][j] in unique:
                                return False
                            else:
                                unique.add(board[i][j])
                unique = set()
                c+= 3
            r+= 3
        return True
        '''

        #Single Pass solution - better if grid size is much larger
        # 3 sets - one for row, one for column, one for subboxes
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        subbox = collections.defaultdict(set) #Key will be (r//3,c//3)

        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != '.':
                    #no not in ith row or jth column or (i//3,j//3)th box then add else False
                    if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in subbox[(i//3,j//3)]):
                        return False
                    else:
                        #add to set
                        rows[i].add(board[i][j])
                        cols[j].add(board[i][j])
                        subbox[(i//3,j//3)].add(board[i][j])
        return True
            

            
        