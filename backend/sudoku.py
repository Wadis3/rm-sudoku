import random
import copy

def check(row, col, digit, board):
	if digit == 0:
		return True
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

def solve_from(row, col, board):
	if col == 9:
		col = 0
		row += 1
		if row == 9:
			return 1
	
	if board[row][col] != 0:
		return solve_from(row, col + 1, board)
	
	solutions = 0
	for digit in valid_at(row, col, board):
		board[row][col] = digit
		
		solutions += solve_from(row, col + 1, board)
		
		board[row][col] = 0
	return solutions

def solve(board):
	return solve_from(0, 0, board)

def gen_puzzle(board, difficulty='medium'):
	targets = {
		'easy': 41,
		'medium': 49,
		'hard': 55
	}
	
	target 	= targets[difficulty]
	removed = 0
	
	positions = [(r, c) for r in range(9) for c in range(9)]
	random.shuffle(positions)
	
	for row, col in positions:
		if removed == target:
			break
		
		temp = board[row][col]
		
		board_copy = copy.deepcopy(board)
		if solve(board_copy) > 1:
			board[row][col] = temp
		else:
			removed += 1

if __name__ == "__main__":
	board = gen_board()
	for row in board:
		print(row)
	print('\n')
	puzzle = copy.deepcopy(board)
	gen_puzzle(puzzle)
	for row in puzzle:
		print(row)
