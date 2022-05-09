class Cell:

    def __init__(self, sym='-'):
        self.symbol = True
        self.sym = sym


class Board:

    def __init__(self):
        self.cells = [[Cell('-') for i in range(3)] for j in range(3)]

    def info(self):
        for i in range(3):
            for j in range(3):
                print(self.cells[j][i].sym, end='')
            print()


class Player:

    def __init__(self, name, sym, board):
        self.name = name
        self.sym = sym
        self.board = board
        self.x = 0
        self.y = 0

    def player_turn(self):
        print('На какую клетку ходим?')
        while True:
            self.x = int(input('Введите координату x (1/2/3): ')) - 1
            self.y = int(input('Введите координату y (1/2/3): ')) - 1
            if self.board.cells[self.x][self.y].sym == '-':
                self.board.cells[self.x][self.y].sym = self.sym
                break
            else:
                print('Клетка занята, попробуйте другую!')

    def filling(self):
        for num in range(3):
            if self.board.cells[num][0].sym == self.board.cells[num][1].sym == self.board.cells[num][2].sym == self.sym:
                return True
            elif self.board.cells[0][num].sym == self.board.cells[1][num].sym \
                    == self.board.cells[2][num].sym == self.sym:
                return True
            elif self.board.cells[0][0].sym == self.board.cells[1][1].sym == self.board.cells[2][2].sym == self.sym:
                return True
            elif self.board.cells[0][2].sym == self.board.cells[1][1].sym == self.board.cells[2][0].sym == self.sym:
                return True
        else:
            return False


board = Board()
player_1 = Player('Ваня', '0', board)
player_2 = Player('Петя', 'X', board)
while True:
    print('Ходит первый игрок!')
    player_1.player_turn()
    win_1 = player_1.filling()
    if win_1 == True:
        print('Победил первый игрок!')
        break
    player_1.board.info()
    print('Ходит второй игрок!')
    player_2.player_turn()
    win_2 = player_2.filling()
    if win_2 == True:
        print('Победил второй игрок!')
        break
    player_1.board.info()
