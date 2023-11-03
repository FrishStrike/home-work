import random

def draw_board(cells):
    print("\n" + "-------" + "\n")
    print(cells[0], '|', cells[1], "|", cells[2])
    print(cells[3], '|', cells[4], "|", cells[5])
    print(cells[6], '|', cells[7], "|", cells[8])
    print("\n" + "-------" + "\n")


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
    while True:
        move = random.randrange(0, 9)
        if cells[move] != "X" and cells[move] != "O":
            cells[move] = symbol
            return
        


def check_win(cells, symbol):
    win_cells = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
        ]
    win_count = 0
    
    for win_cell in win_cells:
        for cell in win_cell: # 0 1 2
            if cells[cell] == symbol: 
                win_count += 1
        # конец игры
        if win_count == 3:
            return True
        win_count = 0
        
    return False   


def cells_is_not_fill(cells):
    count = 0
    for i in cells:
        if i == "X" or i == "O":
            count +=1
    if count == 8:
        print("Ничья!")
        return False
    return True


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
        
    while game:
        draw_board(cells)
        if symbol_player == "X":
            get_player_move(cells, symbol_player)
            draw_board(cells)
            win = check_win(cells, symbol_player)
            if win:
                print("Вы победили!")
                break
            get_computer_move(cells, symbol_computer)
            win = check_win(cells, symbol_computer)
            if win:
                print("Вы проиграли!")
                break
        else:
            get_computer_move(cells, symbol_computer)
            draw_board(cells)
            win = check_win(cells, symbol_computer)
            if win:
                print("Вы проиграли!")
                break
            get_player_move(cells, symbol_player)
            win = check_win(cells, symbol_player)
            if win:
                print("Вы победили!")
                break
        draw_board(cells)
        game = cells_is_not_fill(cells)


main()