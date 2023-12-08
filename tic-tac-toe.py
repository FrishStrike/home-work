import random


def draw_board(cells):
    print("\n" + "-------" + "\n")
    print(cells[0], '|', cells[1], "|", cells[2])
    print(cells[3], '|', cells[4], "|", cells[5])
    print(cells[6], '|', cells[7], "|", cells[8])
    print("\n" + "-------" + "\n")


def check_win(cells, symbol, best_move=False):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    win_moves = {}
    win_move = []
    
    for win_combo in win_combos:
        for combo_cell in win_combo:
            if cells[combo_cell] == symbol: 
                win_move.append(win_move)

        if best_move and len(win_move) == 2:
            dict_key = "".join(str(i) for i in win_move)
            win_move = list(filter(lambda x: x != "X" or x != "O", win_move))
            win_moves[dict_key] = win_move

        if best_move and len(win_move) == 1:
            dict_key = "".join(str(i) for i in win_move)
            win_move = list(filter(lambda x: x != "X" or x != "O", win_move))
            win_moves[dict_key] = win_move
                
        if len(win_move) == 3:
            return True
        
        win_move.clear()
    
    if best_move:
        return win_moves   
    return False   


def cells_is_not_fill(cells):
    count = 0
    for i in cells:
        if i == "X" or i == "O":
            count +=1
    if count == 8:
        draw_board(cells)
        print("Ничья!")
        return False
    return True


def get_player_move(cells, symbol):
    while True:
        move = int(input("Укажите номер клетки: "))-1
        if 0 <= move <= 8:
            if cells[move] != "X" and cells[move] != "O":
                cells[move] = symbol
                return
            else:
                print("Эта клетка уже занята, укажите другую!")
        else:
            print("Нужно указать номер клетки от 1 до 9")


def get_computer_move(cells, symbol):
    win_moves = check_win(cells, symbol, True)
    win_list = []
    print(win_moves)
    if not win_moves:
        while True:
            move = random.randrange(0, 9)
            if cells[move] != "X" and cells[move] != "O":
                cells[move] = symbol
                return
    else:
        for key in win_moves:
            print(win_moves[key])
            if len(win_moves[key]) == 1:
                move = win_moves[key][0]
                break
            for win_move in win_moves[key]:
                win_list.append(win_move)
        if len(win_list):
            move = random.choice(win_list)
        cells[move] = symbol
        


def main():
    cells = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbol_player = random.randrange(0, 2)
    symbol_computer = ""
    if symbol_player == 0:
        symbol_player = "X"
        symbol_computer = "O"
    else:
        symbol_player = "O"
        symbol_computer = "X"

    game = True

    draw_board(cells)
        
    while game:
        if symbol_player == "X":
            get_player_move(cells, symbol_player)
            win = check_win(cells, symbol_player)
            if win:
                draw_board(cells)
                print("Вы победили!")
                break
            get_computer_move(cells, symbol_computer)
            win = check_win(cells, symbol_computer)
            if win:
                draw_board(cells)
                print("Вы проиграли!")
                break
            draw_board(cells)
        else:
            get_computer_move(cells, symbol_computer)
            draw_board(cells)
            win = check_win(cells, symbol_computer)
            if win:
                draw_board(cells)
                print("Вы проиграли!")
                break
            get_player_move(cells, symbol_player)
            win = check_win(cells, symbol_player)
            if win:
                draw_board(cells)
                print("Вы победили!")
                break
        game = cells_is_not_fill(cells)


main()