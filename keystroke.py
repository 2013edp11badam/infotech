from subprocess import Popen, PIPE
import time

def keypress(sequence):
	p = Popen(['xte'], stdin=PIPE)
	p.communicate(input=sequence)

print 'sleep for 5'
time.sleep(5)

ctrl_a_sequence = '''keydown Control_L
key A
keyup Control_L
'''

keypress(ctrl_a_sequence)
