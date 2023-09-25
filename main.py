BOARD = """
     |     |     
  1  |  2  |  3  
_____|_____|_____
     |     |     
  4  |  5  |  6  
_____|_____|_____
     |     |     
  7  |  8  |  9  
     |     |     
"""


def evaluate_board(x, o):
    winning_combinations = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["1", "4", "7"], ["2", "5", "8"],
                            ["3", "6", "9"], ["1", "5", "9"], ["3", "5", "7"]]

    for combination in winning_combinations:
        if all(num in x for num in combination):
            print("Game Over, the winner is X!")
            return "X"

        elif all(num in o for num in combination):
            print("Game Over, the winner is O!")
            return "O"

    if len(x) == 5:
        print("Game Over, Tie!")
        return None

    return False


n = 0
x_moves = []
o_moves = []
available_squares = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
is_playing = True

print("Get ready for an intense game of Tic Tac Toe!"
      "\nShow off your skills, dominate the grid, and emerge victorious in this epic battle of X's and O's."
      "\nLet's play!")
print(BOARD)

while is_playing:
    if n % 2 == 0:
        mark = "X"
    else:
        mark = "O"

    user_input = input(f"You're playing with {mark}'s,"
                       f"\nChoose a square to mark it with {mark}:\n")

    if user_input in available_squares:
        BOARD = BOARD.replace(user_input, mark)
        available_squares.remove(user_input)
        if n % 2 == 0:
            x_moves.append(user_input)
        else:
            o_moves.append(user_input)
        n += 1
        print(BOARD)
    else:
        print("The chosen square is unavailable.")

    winner = evaluate_board(x_moves, o_moves)
    if winner is not False:
        is_playing = False
        break
