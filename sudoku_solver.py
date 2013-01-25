#!/usr/bin/python
from fltk import *
import time

def getColumn(column):
	temp = []
	for x in range(1, 7):
		if sudoku[column][x].value() != '':
			temp.append(sudoku[column][x].value())
	return set(temp)

def getRow(row):
	temp = []
	for x in range(1, 7):
		if sudoku[x][row].value() != '':
			temp.append(sudoku[x][row].value())
	return set(temp)

def getBox(box):
	temp = []
	for column in sudoku:
		for row in sudoku[column]:
			if getBoxNumber(column, row) == box and sudoku[column][row].value() != '':
				temp.append(sudoku[column][row].value())
	return set(temp)

def getBoxNumber(column, row):
	if column == 1 or column == 2 or column == 3:
		if row == 1 or row == 2:
			return 1
		elif row == 3 or row == 4:
			return 3
		elif row == 5 or row == 6:
			return 5

	elif column == 4 or column == 5 or column == 6:
		if row == 1 or row == 2:
			return 2
		elif row == 3 or row == 4:
			return 4
		elif row == 5 or row == 6:
			return 6

def solve(w_id):
	changed = True
	while changed == True:
		changed = False
		for column in sudoku:
			for row in sudoku[column]:
				if sudoku[column][row].value() == '':
					answer = set(['1', '2', '3', '4', '5', '6']) - getColumn(column) - getRow(row) - getBox(getBoxNumber(column, row))
					if len(answer) == 1:
						sudoku[column][row].value(list(answer)[0])
						sudoku[column][row].color(FL_GREEN)
						changed = True
		

window = Fl_Window(0, 0, 315, 350, 'Sudoku Solver')
window.begin()

sudoku = {}
x, y = 5, 5

for column in range(1, 7):
	sudoku[column] = {}
	for row in range(1, 7):
		sudoku[column][row] = Fl_Input(x, y, 50, 50)
		sudoku[column][row].textsize(32)
		if row == 2 or row == 4:
			y += 55
		else:
			y += 50
	y = 5
	if column == 3:
		x += 55
	else:
		x += 50

button_solve = Fl_Button(5, 320, 305, 25, 'Solve')
	
window.end()

button_solve.callback(solve)

window.show()
Fl.run()
