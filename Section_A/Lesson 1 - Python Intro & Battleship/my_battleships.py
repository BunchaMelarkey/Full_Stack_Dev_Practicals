import random

board = []
board_size = 5
ship_locations = []
directions = ["north", "south", "east", "west"]
ship_column = 0
ship_row = 0
ship_size = 0

# Return a random board position
def random_pos():
    return random.randint(0, board_size - 1)

# Return a size of either 1, 2 or 3 spaces
def random_size():
    sizes = [1, 2, 3]
    ship_size = random.choice(sizes)
    return ship_size

# Return a direction - Only applicable for medium or large ships
def random_direction():
    ship_direction = random.choice(directions)
    return ship_direction

def generate_ship(direction, ship_row, ship_column, ship_size):
    if (direction == 'north'):
        ship_locations.append([ship_row - 1], [ship_column])
        if (ship_size == 3):
            ship_locations.append([ship_row - 2], [ship_column])
        else:
            pass
    elif (direction == 'south'):
        ship_locations.append([ship_row + 1], [ship_column])

        if (ship_size == 3):
            ship_locations.append([ship_row + 2], [ship_column])

    elif (direction == 'east'):
        ship_locations.append([ship_row], [ship_column + 1])

        if (ship_size == 3):
            ship_locations.append([ship_row], [ship_column + 2])

    elif (direction == 'west'):
        ship_locations.append([ship_row],[ship_column - 1])

        if (ship_size == 3):
            ship_locations.append([ship_row], [ship_column - 2])


# Print out the playing board neatly
def print_board(board):
    for row in board:
        print(" ".join(row))

# Create ship and input co-ordinates into ship_location List
def create_ship():
    ship_column = random_pos()
    ship_row = random_pos()
    ship_size = random_size()

    # Check for existence of ship in said location
    while (([ship_row, ship_column] in ship_locations)):
        ship_column = random_pos()
        ship_row = random_pos()

    ship_locations.append([ship_row, ship_column])

    # CHeck for ships of greater than size 1 
    if (ship_size > 1):
        print("x")
    # Take the 2 spaces in one of the cardinal directions depending 
    # Return a list of the ship's board spaces


# Need a list of locations and then if they have been hit as well


def start_match(board):
    for x in range(0, board_size):
        board.append(["O"] * board_size)

    print("Lets play Battleships!")
    print_board(board)

ship_row_1 = random_pos()
ship_column_1 = random_pos()

print("Battleship at {}, {}".format(ship_row_1, ship_column_1))

# Logic for user guessing the ship position
for turn in range(1, 13):
    guess_row = int(input("Guess Row: "))
    guess_column = int(input("Guess Column: "))

    if (guess_row < 0 or guess_row >= board_size or \
        guess_column < 0 or guess_column <= board_size):
            print("Oops, that's not in the ocean.")    

    elif (guess_row == ship_row_1 and guess_column == ship_column_1):
        print("Congratulations! You hit one my Battleships!")
        break
    elif (board[guess_row][guess_column] == "X"):
        print("You already guessed that one!")
    else:
        print("You missed my battleship")
        board[guess_row][guess_column] = "X"
        if turn == 12:
            print("Game over!")

print("That was turn" + str(turn))
print_board(board)