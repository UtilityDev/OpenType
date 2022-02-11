import sys
from time import sleep

class Typewriter:
	def __init__(self, speed=0.07):
		self.speed = speed # typing speed

	def type(self, txt, line_break=True):
		for char in txt:
			sleep(self.speed)
			sys.stdout.write(char)
			sys.stdout.flush()
		if line_break:
			print('\n')