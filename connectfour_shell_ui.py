import connectfour, connectfour_shared_ui

if __name__ == '__main__':
    columns = connectfour_shared_ui.get_num_cols()
    rows = connectfour_shared_ui.get_num_rows()
    game = connectfour.new_game(columns, rows)
    #game = connectfour.GameState(board=[[0, 0, 0, 0, 1, 2],[0, 0, 0, 2, 2, 1],[0, 0, 0, 0, 1, 1],[0, 0, 0, 1, 2, 2],[0, 0, 0, 0, 1, 2],[0, 0, 2, 1, 1, 2],[0, 0, 0, 0, 0, 1]],turn=1)
    #print(game)
    connectfour_shared_ui.print_board(game)
    while connectfour.winner(game) == connectfour.EMPTY:
        game = connectfour_shared_ui.prompt_for_move(game)
        connectfour_shared_ui.print_board(game)
    connectfour_shared_ui.declare_winner(game)
