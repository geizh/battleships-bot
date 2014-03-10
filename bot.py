import sys
import json
import random

if __name__ == "__main__":
	report = json.loads(sys.argv[1])
	output = {}
	
	if report.cmd == "init":
		orientation = random.choice("horizontal", "vertical")
		for i in range(2, 6):
			x = None
			y = None
			if orientation == "horizontal":
				x = random.randint(0, 2)
				y = i
			else:
				x = i
				y = random.randint(0, 2)
			
			point = "%d%d" % (x, y)
			output[i] = {"point" : point, "orientation" : orientation}
			
	elif report.cmd == "move":
		x = None
		y = None
		
		while True:
			x = random.randint(0, 7)
			y = random.randint(0, 7)
			if move not in report.hit and move not in report.missed:
				break;
		
		output = {"move" : "%d%d" % (x, y)}
	
	print json.dumps(output)
	