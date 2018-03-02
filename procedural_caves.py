#/usr/bin/env python
#v0.2
import random, time

mapHeight = 30
mapWidth = 30
fillPercent = 45

def generateNoise():
	#generate a grid of cells with height = mapHeight and width = mapWidth with each cell either "walls" (true) or "floors" (false)
	#border is guaranteed to be walls and all other spaces have a fillPercent chance of being walls
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

def isOutOfBounds(column, row):
	#find if a cell is out of bounds based on map size
	
	if column < 1 or row < 1:
		return True
	elif column > mapWidth or row > mapHeight:
		return True
	else:
		return False

def isWall(caveMap, column, row):
	#determine if a cell is a wall or not
	#very inefficient - might have to loop through entire list

	for cell in caveMap:
		if cell[0] == column and cell[1] == row and cell[2] == 1:
			return True
		elif cell[0] == column and cell[1] == row and cell[2] == 0:
			return False
		else:
			continue
	
def findNeighbors(caveMap, column, row):
	#find the number of walls in a 3x3 pattern around a given cell (determined by column and row)
	#there must be a more efficient way to do this, but here we are

	neighbors = 0

	if isOutOfBounds(column -1, row -1):
		neighbors += 1
	elif isWall(caveMap, column -1, row -1):
		neighbors += 1
		
	if isOutOfBounds(column, row -1):
		neighbors += 1
	elif isWall(caveMap, column, row -1):
		neighbors += 1
		
	if isOutOfBounds(column +1, row -1):
		neighbors += 1
	elif isWall(caveMap, column +1, row -1):
		neighbors += 1
		
	if isOutOfBounds(column -1, row):
		neighbors += 1
	elif isWall(caveMap, column -1, row):
		neighbors += 1
		
	if isOutOfBounds(column +1, row):
		neighbors += 1
	elif isWall(caveMap, column +1, row):
		neighbors += 1
		
	if isOutOfBounds(column -1, row +1):
		neighbors += 1
	elif isWall(caveMap, column -1, row +1):
		neighbors += 1
		
	if isOutOfBounds(column, row +1):
		neighbors += 1
	elif isWall(caveMap, column, row +1):
		neighbors += 1
		
	if isOutOfBounds(column +1, row +1):
		neighbors += 1
	elif isWall(caveMap, column +1, row +1):
		neighbors += 1

	return neighbors
	
def runGeneration (caveMap, generations):
	#smooth out random noise using modified 4-5 cellular automata rules
	#the entire process is pretty inefficient - it has to loop through the entire list as many as 
	#(mapWidth * mapHeight * 8) times for potentially millions of comparisons
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
	#print the map by displaying a grid of characters where # = walls and spaces = floors
	#just uses mapWidth to insert returns, very agnostic about the column/row of a cell
	
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
	runGeneration(caveMap, 2)
		
if __name__ == "__main__":
	main()