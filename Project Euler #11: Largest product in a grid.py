#!/bin/python
import sys

grid = []
for grid_i in xrange(20):
    grid_temp = map(int,raw_input().strip().split(' '))
    grid.append(grid_temp)
r=[]
for item in grid:
    for i in range(17):
        r.append(reduce(lambda a,b:a*b , item[i:i+4]))
r=[max(r)]
for i in range(17):
    r=[max(r)]
    for j in range(17):
        r.append(grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j])
        r.append(grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3])
r=[max(r)]
for i in range(3,20):
    for j in range(17):
        r.append(grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3])
print max(r)
