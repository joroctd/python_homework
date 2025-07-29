class TictactoeException(Exception):
    def __init__(self, message):
        self.message = f'Error: {message}\n'
        super()

class Board:
    valid_moves = ["upper left", "upper center", "upper right", 
                   "middle left", "center", "middle right", 
                   "lower left", "lower center", "lower right"]
    
    def __init__(self, size=3):
        self.squares = [[' '] * size for _ in range(size)]
        self.turn = "X"
        self.size = 3

    def __str__(self):
        lines=['\n']
        for i in range(len(self.squares)):
            lines.append(f' {' | '.join(self.squares[i])} \n')
            if not i == len(self.squares)-1:
                lines.append('-----------\n')
        return ''.join(lines)

    def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TictactoeException('Invalid move.')
        
        move_index = Board.valid_moves.index(move_string)
        row = move_index // len(self.squares)
        column = move_index % len(self.squares[0])

        if self.squares[row][column] != ' ':
            raise TictactoeException('Spot is taken.')
        
        self.squares[row][column] = self.turn
        self.turn = {'X': 'O', 'O': 'X'}[self.turn]

    def whats_next(self):
        # util/tictactoe-gen-wins.py
        wins = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], 
                [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)], 
                [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
        for play in ['X', 'O']:
            for line in wins:
                if all(self.squares[i][j] == play for i, j in line):
                    return (True, f'{play} wins!')
                
        if all(self.squares[i][j] != ' ' for i in range(self.size) for j in range(self.size)):
            return (True, "Cat's Game.")
        
        return (False, f"{self.turn}'s turn.")

board = Board()
print(board)
print(f'Welcome to Tic Tac Toe! Valid commands are: {Board.valid_moves}.\n')
done = False
while not done:
    try:
        move = input(f'Enter {board.turn}\'s move: ')
    except KeyboardInterrupt as e:
        done = True
        print('')
        continue

    try:
        board.move(move)
        print(board)
        done, message = board.whats_next()
    except TictactoeException as e:
        message = e.message
    print(message)

print('\nThanks for playing!\n')
