import sqlite3
import json
from sudoku import gen_game
from flask import Flask, request, jsonify, render_template

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
	conn.commit()
	conn.close()

@app.route('/new_board', methods=['GET'])
def new_sudoku():
	difficulty = request.args.get('difficulty', 'medium')
	
	game = gen_game(difficulty)
	
	conn = sqlite3.connect(DB_FILE)
	cursor = conn.cursor()
	
	cursor.execute('INSERT INTO sudokus (difficulty, puzzle, solution) VALUES (?, ?, ?)', (difficulty, json.dumps(game['puzzle']), json.dumps(game['board'])))
	id = cursor.lastrowid
	conn.commit()

	conn.close()
	
	return jsonify({
		'id': id,
		'difficulty': difficulty,
		'puzzle': game['puzzle'],
		'board': game['board']
	})

@app.route('/get/<int:id>', methods=['GET'])
def get(id):
	conn = sqlite3.connect(DB_FILE)
	cursor = conn.cursor()
	
	cursor.execute('SELECT id, difficulty, puzzle, solution FROM sudokus WHERE id = ?', (id,))
	row = cursor.fetchone()
	conn.close()

	if row is None:
		return jsonify({'error': 'Hittade inte pusslet'}), 404
	
	return jsonify({
		'id': row[0],
		'difficulty': row[1],
		'puzzle': json.loads(row[2]),
		'board': json.loads(row[3])
	})

@app.route('/render/<int:id>', methods=['GET'])
def render(id):
	conn = sqlite3.connect(DB_FILE)
	cursor = conn.cursor()

	cursor.execute('SELECT id, difficulty, puzzle, solution FROM sudokus WHERE id = ?', (id,))
	row = cursor.fetchone()
	conn.close()

	if row is None:
		return 'Hittade inte pusslet', 404

	difficulty = row[1]
	puzzle = json.loads(row[2])

	return render_template(
		'sudoku.html',
		puzzle_id=id,
		difficulty=difficulty,
		puzzle=puzzle
	)

if __name__ == '__main__':
	init_db()
	app.run(host='0.0.0.0', port=5000)
