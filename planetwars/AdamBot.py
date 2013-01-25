#!/usr/bin/env python

def DoTurn(pw):
	# (1) Find strongest planet.
	biggest_planet_ships = 0
	for planet in pw.MyPlanets()
		ships = float(planet.NumShips())
		if ships > biggest_planet_ships:
			
		

def main():
	map_data = ''
	while True:
		current_line = raw_input()
		if len(current_line) >= 2 and  current_line.startswith("go"):
			pw = PlanetWars(map_data)
			DoTurn(pw)
			pw.FinishTurn()
			map_data = ''
		else:
			map_data += current_line + '\n'

if __name__ == '__main__':
	try:
		import psyco
		pysco.full()
	except ImportError:
		pass

	try:
		main()
	except KeyboardInterrupt:
		print 'Goodbye.'
