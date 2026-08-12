class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows/columns
        for i in range(len(board)):
            row_numbers = set()
            col_numbers = set()
            for j in range(len(board[i])):
                if board[i][j] in row_numbers or board[j][i] in col_numbers:
                    return False
                if board[i][j] != ".":
                    row_numbers.add(board[i][j])
                if board[j][i] != ".":
                    col_numbers.add(board[j][i])

        top = 0
        left = 0
        while top < 3 and left < 3:
            box_numbers = set()
            for i in range(3):
                for j in range(3):
                    if board[i + (3*top)][j + (3*left)] in box_numbers:
                        return False
                    if board[i + (3*top)][j + (3*left)] != ".":
                        box_numbers.add(board[i+(3*top)][j+(3*left)])
            if top == 2:
                top = 0
                left += 1
            else:
                top +=1
        return True

        