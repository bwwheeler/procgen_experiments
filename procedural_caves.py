#/usr/bin/env python

import random, time

mapHeight = 30
mapWidth = 30
fillPercent = 45

def generateNoise():
	caveMap = []
	column = 1
	row = 1
	
	while column <= mapWidth:
		while row <= mapHeight:
			if (column == 1) or (column == mapWidth) or (row == 1) or (row == mapHeight):
				caveMap.append([column, row, 1])
			else:
				if random.randrange(1,100) <= fillPercent:
					caveMap.append([column, row, 1])
				else:
					caveMap.append([column,row,0])
			row += 1
		column += 1
		row = 1
		
	printCaveMap(caveMap)		
	return caveMap
	
# def findIndex(caveMap, column, row):
	# coords = "[" + str(column) + "," + str(row) + ",*]"
	# i = caveMap.index(coords)
	# print(i)

def isOutOfBounds(column, row):

		if column < 1 or row < 1:
			#print(column, ", " , row, " out of min bounds")
			return True
		elif column > mapWidth or row > mapHeight:
			#print(column, ", " , row, " out of max bounds")
			return True
		else:
			#print(column, ", " , row, " in bounds")
			return False

def isWall(caveMap, column, row):
	for cell in caveMap:
		if cell[0] == column and cell[1] == row and cell[2] == 1:
			return True
			#print(cell, " is wall")
		elif cell[0] == column and cell[1] == row and cell[2] == 0:
			return False
			#print(cell, "is not wall")
		else:
			continue
	
def findNeighbors(caveMap, column, row):

	neighbors = 0

	if isOutOfBounds(column -1, row -1):
		neighbors += 1
	elif isWall(caveMap, column -1, row -1):
		#print("checking upper left")
		neighbors += 1
		#print(neighbors,"\n")
		
	if isOutOfBounds(column, row -1):
		neighbors += 1
	elif isWall(caveMap, column, row -1):
		#print("checking above")
		neighbors += 1
	#	print(neighbors,"\n")
		
		
	if isOutOfBounds(column +1, row -1):
		neighbors += 1
	elif isWall(caveMap, column +1, row -1):
		#print("checking upper right")
		neighbors += 1
		#print(neighbors,"\n")
		
		
	if isOutOfBounds(column -1, row):
		neighbors += 1
	elif isWall(caveMap, column -1, row):
		#print("checking left")
		neighbors += 1
		#print(neighbors,"\n")
		
	if isOutOfBounds(column +1, row):
		neighbors += 1
	elif isWall(caveMap, column +1, row):
		#print("checking right")
		neighbors += 1
		#print(neighbors,"\n")
		
	if isOutOfBounds(column -1, row +1):
		neighbors += 1
	elif isWall(caveMap, column -1, row +1):
		#print("checking lower left")
		neighbors += 1
		#print(neighbors,"\n")
		
	if isOutOfBounds(column, row +1):
		neighbors += 1
	elif isWall(caveMap, column, row +1):
		#print("checking below")
		neighbors += 1
		#print(neighbors,"\n")
		
	if isOutOfBounds(column +1, row +1):
		neighbors += 1
	elif isWall(caveMap, column +1, row +1):
		#print("checking lower right")
		neighbors += 1
		#print(neighbors,"\n")
		
	# print("Cell ", cell, " complete")
	#input("")

	return neighbors
	
def runGeneration (caveMap, generations):
	i =0 
	
	for i in range(0, generations):
		start_time = time.time()
		for cell in caveMap:
			if findNeighbors(caveMap,cell[0],cell[1]) < 3:
				cell[2] = 0
			elif findNeighbors(caveMap, cell[0], cell[1]) > 5:
				cell[2] = 1
		printCaveMap(caveMap)
		end_time = time.time()
		print(end_time - start_time, " seconds")
	
	return caveMap

	
def printCaveMap(caveMap):
	i = 1
	for item in caveMap:
		if i == mapWidth + 1:
			print('\r')
			i = 1
		if item[2] == 1:
			print(" # ", end="")
		else:
			print("   ", end="")
		i += 1
	
	print("\n", "\n")
	
def main():
		
	caveMap = generateNoise()
	# findIndex(caveMap, 2,2)
	#print("\n", findNeighbors(caveMap, 2,2))
	#print("\n", findNeighbors(caveMap, 3,3))
	#input("waiting...")
	runGeneration(caveMap, 2)
		
if __name__ == "__main__":
	main()