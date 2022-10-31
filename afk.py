import pyautogui as p
import random

while True:
	x = random.randint(1000, 1500)
	y = random.randint(500, 1000)
	p.moveTo(x, y, 0.1)
