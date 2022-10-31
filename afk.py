import pydirectinput
import random

while True:
	x = random.randint(1000, 1500)
	y = random.randint(500, 1000)
	pydirectinput.moveTo(x, y, 0.1)
