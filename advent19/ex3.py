import numpy as np
import csv
import pprint
pp = pprint.PrettyPrinter(indent=4)

def plot_coord(point,n):
	return point[0] + n//2, point[1] + n//2, point[2]

def right(loc,length):
	line = [(loc[0] + i, loc[1], loc[2] + i) for i in range(1,length + 1)]
	return line

def left(loc,length):
	line = [(loc[0] - i, loc[1], loc[2] + i) for i in range(1,length + 1)]
	return line

def up(loc,length):
	line = [(loc[0], loc[1] + i, loc[2] + i) for i in range(1,length + 1)]
	return line

def down(loc,length): 
	line = [(loc[0], loc[1] - i, loc[2] + i) for i in range(1,length + 1)]
	return line

def move_line(line,n):
	return [plot_coord(p,n) for p in line]

def plot_line(line,n):
	counts = list(np.zeros([n,n])) #[[ 0 for i in range(n)] for j in range(n)]
	distance = list(np.zeros([n,n]))
	for p in line:
		counts[p[0]][p[1]] += 1
		distance[p[0]][p[1]] += p[2]
	return counts, distance 

def make_line(instructions):
	line = [(0,0,0)]
	for p in instructions:
		direction = p[0]
		length = int(p[1:])
		if direction == 'R':
			line.extend(right(line[-1],length))
		elif direction == 'L':
			line.extend(left(line[-1],length))
		elif direction == 'U':
			line.extend(up(line[-1],length))
		elif direction == 'D':
			line.extend(down(line[-1],length))
	return line

#remove self intersection
def remove_self_intersection(counts):
	counts = list(counts)
	counts_np  = np.array(counts)
	counts_np[counts_np > 0] = 1
#	for i in range(n):
#		for j in range(n):
#			if counts[i][j] > 0:
#				counts[i][j] = 1
	return list(counts_np)
#pp.pprint(counts)


n = 20000 
#grid = [[(i,j) for i in range(n)] for j in range(n)]
#counts = [[ 0 for i in range(n)] for j in range(n)]

with open('ex3.csv','r') as f:
	csv = csv.reader(f)
	data = [row for row in csv]

instruction = data[0]
print("Instructions 1 loaded")
line = make_line(instruction)
print("line 1 made")
transformed_line = move_line(line,n)
print("line 1 moved")
counts, distance = plot_line(transformed_line,n)
print("line 1 plotted")
counts = remove_self_intersection(tuple(counts))
print("self-intersections removed")

instruction2 = data[1]
print("Instruction 2 loaded")
line2 = make_line(instruction2)
print("Line 2 made")
transformed_line2 = move_line(line2,n)
print("line 2 moved")
counts2, distance2 = plot_line(transformed_line2,n)
print("line 2 plotted")
counts2 = remove_self_intersection(counts2)
print("self-intersections removed")

total = np.array(counts) + np.array(counts2)

cross = np.where(total > 1)

man_dist = np.abs(cross[0]-n//2) + np.abs(cross[1]-n//2)
man_dist = man_dist[man_dist > 0]
min_dist = min(man_dist)

print((man_dist,min_dist))
total_distances = []
for cross_x, cross_y in zip(cross[0],cross[1]):
	total_distance = distance[cross_x][cross_y] + distance2[cross_x][cross_y]
	total_distances.append(total_distance)
total_distances = np.array(total_distances, dtype=int)
total_distances = total_distances[total_distances > 0]
print((total_distances,min(total_distances)))
