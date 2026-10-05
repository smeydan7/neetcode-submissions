class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = set([])
        for i in board:
            for j in i:
                if j == '.':
                    continue
                if j in hashmap:
                    return False
                hashmap.add(j)
            hashmap = set([])

        for i in range(9):
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in hashmap:
                    return False
                hashmap.add(board[j][i])
            hashmap = set([])

        for k in range(9):  
            if k == 0:
                l = 0
                r = 0
            if k == 1:
                l = 3
                r = 0
            if k == 2:
                l = 6
                r = 0
            if k == 3:
                l = 0
                r = 3
            if k == 4:
                l = 3
                r = 3
            if k == 5:
                l = 6
                r = 3
            if k == 6:
                l = 0
                r = 6
            if k == 7:
                l = 3
                r = 6
            if k == 8:
                l = 6
                r = 6

            for i in range(3):
                for j in range(3):
                    if board[l + i][r + j] == '.':
                        continue
                    if board[l + i][r + j] in hashmap:
                        return False
                    hashmap.add(board[l + i][r + j])
            print("reset")
            hashmap = set([])
        
        return True
