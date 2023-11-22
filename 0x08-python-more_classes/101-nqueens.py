#!/usr/bin/python3

"""

This is module for giving selution to following problem
Placing N non-attacking queens on an N×N chessboard

"""


class Chessboard():
    """
    chassBoard is chessboard of size N x N
    args:
        N: Is the size of N
        N: must be a number, Or ValueError will be raised
    """
    
    def __init__(self, N:int):
        """Constructor"""
        self.N = N
        self.board = [[0 for i in range(0, self.N)] for j in range(0, self.N)]
        self.queens = 0

    @property
    def N(self):
        """The N property."""
        return self.__N
    
    @N.setter
    def N(self, value):
        """set the N"""
        self.__N = value
    
    def put_queen(self, x, y):
        if (x > self.__N or y > self.__N):
            raise ValueError("Out of board range")

        if not self.could_fit(x, y):
            raise ValueError("Position occupied")

        for a,b in self.queen_attacks(x, y):
            self.board[a][b] = "x"
        self.board[x][y] = "Q" or "🔅"

    def could_fit(self, x, y):
        """Checks if queen could fit in position wihtout
        attack/getting attacked from another"""

        if self.board[x][y] in ("x", "Q"):
            return False

        for a, b in self.queen_attacks(x, y):
            if self.board[a][b] == "Q":
                return False

        return True
    
    def queen_attacks(self, x, y):
        if (x > self.__N or y > self.__N):
            raise ValueError("Out of board range")

        queen_attacks = []

        for i in range(0, self.__N):
            if (self.board[i][x] != "1"):
                queen_attacks.append((x, i))
            if (self.board[y][i] != "1"):
                queen_attacks.append((i, y))

        for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
            # self.board[i][j] = "x"
            queen_attacks.append((i, j))
            
        for i, j in zip(range(y, self.__N, 1), range(x, -1, -1)):
            # self.board[i][j] = "x"
            queen_attacks.append((i, j))

        for i, j in zip(range(x, self.__N), range(y, self.__N)):
            # self.board[i][j] = "x"
            queen_attacks.append((i, j))

        for i, j in zip(range(x, self.__N), range(y, -1, -1)):
            # self.board[j][i] = "x"
            queen_attacks.append((j, i))
        

        return queen_attacks

    
    def get_queen(self, x, y):
        if (x > self.__N or y > self.__N):
            raise ValueError("Out of board range")
        
        pos = self.queen_attacks(x, y)
        self.board[x][y] = 0
        for a, b in pos:
            self.board[a][b] = 0

        self.queens -= 1


    def print_board(self):
        """print_board"""
        for i, sub_lis in enumerate(self.board):
            print("-"*self.__N*self.__N)
            for j, _ in enumerate(sub_lis):
                print("|",self.board[i][j], "|", end="")
            print()
        print("_"*self.__N*self.__N)

judit = Chessboard(4)

judit.put_queen(0, 1)
judit.put_queen(1, 3)
judit.get_queen(1, 3)

# judit.put_queen(3, 2)
print(2, 2)
judit.print_board()

# def could_fit(cb, row, solutions, result):
#     
#     if len(solutions) == 4:
#         result.append(solutions)
#         print("here?")
#         solutions = []
#
#     if row > 3 and row < 0:
#         row = 0
#
#     for col in range(0, cb.N):
#         if cb.could_fit(row, col):
#             print(row, col)
#             cb.put_queen(row, col)
#             solutions.append((row, col))
#             could_fit(cb, row + 1, solutions, result)
#             print(solutions)
#             cb.print_board()
#
#     # if len(solutions) > 0:
#     #     cb.get_queen(*solutions[-1])
#     #     solutions.pop()
#
#
#
# judit.print_board()
# print(could_fit(judit, 0, [], []))


