#!/usr/bin/python
# and flooded_cells[neighbour] not in flooded_cells:
import random, time
from fltk import *

def go(w_id):

	print str(len(flooded_cells))

	for cell in flooded_cells:
		index = flooded_cells.index(cell)
		neighbours = [index + 14, index - 14, index + 1, index - 1]
		for neighbour in neighbours:
			print 'INDEX COLOR: ' + str(floodit[index].color())
			print 'NEIGHBOUR COLOR: ' + str(floodit[neighbour].color())
			try:
				if floodit[index].color() == floodit[neighbour].color():
					if floodit[neighbour] not in flooded_cells:
						flooded_cells.append(neighbour)
						print 'SAME AND ADDED'
			except IndexError:
				pass

	for x in flooded_cells:
		floodit[x].color(w_id.color())
		floodit[x].redraw()

#floodit[cell].color(button_color)
#floodit[neighbour].color(floodit[cell].color())
#floodit[neighbour].redraw()

# create window
window = Fl_Window(335, 290, 'Floodit')
window.begin()

# create buttons
button_red = Fl_Button(5, 5, 40, 40)
button_yellow = Fl_Button(5, 45, 40, 40)
button_green = Fl_Button(5, 85, 40, 40)
button_blue = Fl_Button(5, 125, 40, 40)
button_magenta = Fl_Button(5, 165, 40, 40)
button_cyan = Fl_Button(5, 205, 40, 40)

# set button colors
button_red.color(FL_RED)
button_yellow.color(FL_YELLOW)
button_green.color(FL_GREEN)
button_blue.color(FL_BLUE)
button_magenta.color(FL_MAGENTA)
button_cyan.color(FL_CYAN)

turns_output = Fl_Output(5, 260, 40, 25)
turns_output.value('25')

# set variables for grid
floodit = []
flooded_cells = [0]
colors = [FL_RED, FL_YELLOW, FL_GREEN, FL_BLUE, FL_MAGENTA, FL_CYAN]
x, y = 50, 5

for column in range(1, 15):
	for row in range(1, 15):
		floodit.append(Fl_Box(x, y, 20, 20))
		floodit[-1].box(FL_FLAT_BOX)
		floodit[-1].color(random.choice(colors))
		y += 20
	y = 5
	x += 20

print floodit[0].color()

window.end()

button_red.callback(go)
button_yellow.callback(go)
button_green.callback(go)
button_blue.callback(go)
button_magenta.callback(go)
button_cyan.callback(go)

window.show()
Fl.run()
