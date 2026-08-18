import sqlite3
import json
from flask import Flask

app = Flask(__name__)
DB_FILE = "/data/sudoku.db"

def init_db():
	conn = sqlite3.connect(DB_FILE)
	cursor = conn.cursor()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS sudokus (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			difficulty TEXT NOT NULL,
			puzzle TEXT NOT NULL,
			solution TEXT NOT NULL
		)
	''')

	cursor.execute('SELECT COUNT(*) FROM sudokus')
	if cursor.fetchone()[0] == 0:
		puzzle_example 	= [[0]]
		puzzle_solution = [[0]]
		cursor.execute('INSTERT INTO sudokus (difficulty, puzzle, solution VALUES (?, ?, ?)', ('easy', json.dumps(puzzle_example), json.dumps(puzzle_solution)))
		conn.commit()
	conn.close()

@app.route('/new_board', methods=['GET'])
def new_sudoku():
	difficulty = request.args.get('difficulty', 'easy')

	conn = sqlite3.connect(DB_FILE)
	cursor = conn.cursor()
    	return board

if __name__ == '__main__':
    	app.run(host='0.0.0.0', port=5000)
