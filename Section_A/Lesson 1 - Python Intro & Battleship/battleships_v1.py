import random

def print_board(board):
  for row in board:
    print(" ".join(row))

def random_pos():
  return random.randint(0,board_size-1)

board = []
board_size=5

for x in range(0,board_size):
  board.append(["O"] * board_size)

print("Let's play Battleships!")
print_board(board)

ship_row = random_pos()
ship_col = random_pos()
print("Battleship at {},{}".format(ship_row,ship_col))