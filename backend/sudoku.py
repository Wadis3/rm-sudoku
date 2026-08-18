import random

def check(row, col, digit, board):
	for i in range(9):
		if col != i and board[row][i] == digit:
			return False
		if row != i and board[i][col] == digit:
			return False
	
	for i in range(3 * (row // 3), 3 * ((row + 3) // 3)):
		for j in range(3 * (col // 3), 3 * ((col + 3) // 3)):
			if not(row == i and col == j) and board[i][j] == digit:
				return False
	
	return True

def valid_at(row, col, board):
	available = []
	for digit in range(1, 10):
		if check(row, col, digit, board):
			available.append(digit)
	return available

def gen_from(row, col, board):
	if (col == 9):
		col = 0
		row += 1
		if row == 9:
			return True
	
	choices = valid_at(row, col, board)
	random.shuffle(choices)
	
	for digit in choices:
		board[row][col] = digit
		
		if gen_from(row, col + 1, board):
			return True
		
		board[row][col] = 0
	
	return False

def gen_board():
	board = [[0 for _ in range(9)] for _ in range(9)]
	gen_from(0, 0, board)
	return board

if __name__ == "__main__":
	sudoku = gen_board()
	for row in sudoku:
		print(row)
