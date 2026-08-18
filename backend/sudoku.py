import random

def check(row, col, digit, board):
	for i in range(9):
		if col != i && board[row][i] == digit:
			return false
		if row != i && board[i][col] == digit:
			return false
	
	for i in range(3 * (row / 3), 3 * ((row + 3) / 3)):
		for j in range(3 * (col / 3), 3 * ((col + 3) / 3)):
			if !(row == i && col == j) && board[i][j] == digit:
				return false
	
	return true

def valid_at(row, col):
	available = []
	for digit in range(1, 10):
		if check(row, col, digit):
			available.add(digit)
	return available

def gen_from(row, col, board):
	if (col == 9):
		col == 0
		row = row + 1
		if (row == 9):
			return board
	
	random.choice(valid_at(row, col))
	return gen_from(row + 1, col, board)

def gen_board():
	board = [[0 for _ in range(9)] for _ in range(9)]
	
	return gen_from(0, 0, board)
