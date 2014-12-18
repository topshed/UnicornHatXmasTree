import unicornhat as UH
import  sys, time
import random

UH.clear()
while True:

# create each row of the tree
	for y in range(0,8):
		for x in range(6,8):
			UH.set_pixel(x,y, 0,255,0)
	for y in range(1,7):
		for x in range(4,6):
			UH.set_pixel(x,y, 0,255,0)
	for y in range(2,6):
		for x in range(2,4):
			UH.set_pixel(x,y, 0,255,0)
	for y in range(3,5):
		for x in range(0,2):
			UH.set_pixel(x,y, 0,255,0)
	UH.show()
#now generate the baubles at random
	balbs = random.randint(1,5)
	i = 1
	while i <= balbs:
		b1_y = random.randint(1,6)
		b1_x = random.randint(4,5)
		randr = random.randint(50,255)
		randg = random.randint(50,255)
		randb = random.randint(50,255)
		i+=1
		UH.set_pixel(b1_x,b1_y,randr, randg, randb)
	balbs = random.randint(1,4)
	i = 1
	while i <= balbs:
		b1_y = random.randint(0,7)
		b1_x = random.randint(6,7)
		randr = random.randint(50,255)
		randg = random.randint(50,255)
		randb = random.randint(50,255)
		i+=1
		UH.set_pixel(b1_x,b1_y,randr, randg, randb)
	balbs = random.randint(1,3)
	i = 1
	while i <= balbs:
		b1_y = random.randint(2,5)
		b1_x = random.randint(2,3)
		randr = random.randint(50,255)
		randg = random.randint(50,255)
		randb = random.randint(50,255)
		i+=1
		UH.set_pixel(b1_x,b1_y,randr, randg, randb)
	UH.show()
	time.sleep(0.4)
