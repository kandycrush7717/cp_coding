'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-02-12
    * Time : 4:12 p.m.
    * Question :(https://leetcode.com/problems/valid-sudoku/)
        Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following
        rules:
        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        Note:
            A Sudoku board (partially filled) could be valid but is not necessarily solvable.
            Only the filled cells need to be validated according to the mentioned rules.
    * Example :
        Input :
            [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
        Output :
            True
'''
def isValidSudoku(board) -> bool:
    u_rows=[set() for x in range(9)]
    u_cols=[set() for x in range(9)]
    u_mini_sqs=[[set(),set(),set()] for x in range(3)]
    for r in range(9):
        for c in range(9):
            if board[r][c]!='.':
                if board[r][c] in u_rows[r] or board[r][c] in u_cols[c] or board[r][c] in u_mini_sqs[r//3][c//3]:
                    return False
                else:
                    u_rows[r].add(board[r][c])
                    u_cols[c].add(board[r][c])
                    u_mini_sqs[r//3][c//3].add(board[r][c])
    return True