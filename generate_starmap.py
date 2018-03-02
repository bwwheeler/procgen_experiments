import matplotlib.pyplot as plt
import random

k = int(input("Number of stars "))

height = 1000
width = 1000
# k = 50

i = 1
starList = []

while i < k:
	point = [random.randrange(5,width-5),random.randrange(5,height-5)]
	starList.append(point)
	i += 1

print(*zip(*starList))
plt.scatter(*zip(*starList))
plt.axis([0,width,0,height])
plt.show()