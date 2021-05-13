import connectfour

def get_num_cols() -> int:
    '''Prompt the user for the number of columns the game will be played with and
    return it.
    '''
    while True:
        user_input = input('Number of columns (from 4 to {}): '.format(connectfour.MAX_COLUMNS))
        if not user_input.isdigit():
            print('Invalid input')
        else:
            num_cols = int(user_input)
            if num_cols < 4 or num_cols > connectfour.MAX_COLUMNS:
                print('Invalid number of columns')
            else:
                return num_cols

def get_num_rows() -> int:
    '''Prompt the user for the number of rows the game will be played with and
    return it.
    '''
    while True:
        user_input = input('Number of rows (from 4 to {}): '.format(connectfour.MAX_ROWS))
        if not user_input.isdigit():
            print('Invalid input')
        else:
            num_rows = int(user_input)
            if num_rows < 4 or num_rows > connectfour.MAX_ROWS:
                print('Invalid number of rows')
            else:
                return num_rows

def print_board(game_state: connectfour.GameState) -> None:
    '''Print the board given the game_state.
    '''
    print()
    for i in range(1, connectfour.columns(game_state) + 1):
        if i < 9:
            print(i, end = '  ')
        else:
            print(i, end = ' ')
    print()
    for row in range(connectfour.rows(game_state)):
        for column in range(connectfour.columns(game_state)):
            if game_state.board[column][row] == connectfour.EMPTY:
                print('.', end = '  ')
            elif game_state.board[column][row] == connectfour.RED:
                print('R', end = '  ')
            elif game_state.board[column][row] == connectfour.YELLOW:
                print('Y', end = '  ')
            if column == connectfour.columns(game_state) - 1:
                print()

def prompt_for_move(game_state: connectfour.GameState) -> connectfour.GameState:
    while True:
        try:
            if game_state.turn == connectfour.RED:
                move = input('\nRed player\'s turn. Enter move (e.g. "drop 4" or "pop 1"): ')
            elif game_state.turn == connectfour.YELLOW:
                move = input('\nYellow player\'s turn. Enter move (e.g. "drop 4" or "pop 1"): ')
            if valid_move_format(move):
                return execute_move(game_state, move)
            else:
                print('Invalid format. Try again.')
        except connectfour.InvalidMoveError:
            print('Invalid move. Try again.')
        except ValueError:
            print('Invalid column number. Try again.')

def valid_move_format(move: str) -> bool:
    '''Return True if the move is in the correct format. Otherwise, return False.
    '''
    if len(move) < 5 or len(move) > 6:
        return False
    if move[:-2].lower() != 'drop' and move[:-2].lower() != 'pop':
        return False
    if not move[-1].isdigit():
        return False
    return True

def execute_move(game_state: connectfour.GameState, move: str) -> connectfour.GameState:
    '''Execute the user's move given the current game_state and return the resulting
    game state.
    '''
    if move[:-2].lower() == 'drop':
        return connectfour.drop(game_state, int(move[-1]) - 1)
    elif move[:-2].lower() == 'pop':
        return connectfour.pop(game_state, int(move[-1]) - 1)

def declare_winner(game_state: connectfour.GameState) -> None:
    '''Print who won once the game is over.
    '''
    if connectfour.winner(game_state) == connectfour.RED:
        print('\nGame over. Red player wins!')
    elif connectfour.winner(game_state) == connectfour.YELLOW:
        print('\nGame over. Yellow player wins!')
