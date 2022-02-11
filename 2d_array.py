
#########################
### NUMBER OF ISLANDS ###
#########################
'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

# key is to sink all parts of island if encountered 
# use DFS - if memory is issue use stack instead of recursion
# time: O(MN)
# space: O(MN) worst case when grid map filled with lands
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        M,N = len(grid), len(grid[0])

        def dfs(i,j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                if i > 0 : dfs(i-1,j)
                if i < M-1 : dfs(i+1,j)
                if j > 0 : dfs(i,j-1)
                if j < N-1 : dfs(i,j+1)
        
        cnt = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    dfs(i,j)
                    cnt += 1
        return cnt



#######################
### MAX AREA ISLAND ###
#######################
'''
Given a non-empty 2D array grid of 0's and 1's, 
an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
'''
def maxAreaOfIsland(self, grid):
    max_area = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Reset cur_area to 0
                self.cur_area = 0
                self.dfs(grid, i, j)
                
                max_area = max(max_area, self.cur_area)
                
    return max_area
        
    def dfs(self, grid, i, j):
        self.cur_area += 1
        grid[i][j] = 0
        
        # Check left
        if j - 1 >= 0 and grid[i][j-1] == 1:
            self.dfs(grid, i, j-1)
        
        # Check right
        if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
            self.dfs(grid, i, j+1)
        
        # Check up
        if i - 1 >= 0 and grid[i-1][j] == 1:
            self.dfs(grid, i-1, j)
        
        # Check down
        if i + 1 < len(grid) and grid[i+1][j] == 1:
            self.dfs(grid, i+1, j)


'''
last question was a variation of largest island matrix
except it was like largest land mass that could have water inside it
so basically you have to first take out all the water that touches the edges of matrix border -> mark with #
and then the largest landmass with the land remaining kinda
I did it in some 3 pass janky way where
I filled in the land masses
and then did largest land mass LOL
but the dude liked me and we kinda clicked so I guess it was fine
'''

# first take out all the water that touches the edges of matrix border -> mark with #
# memoization by marking edge waters # so don't repeat
# run largest island but 0s count as 1 too 
[[1,2,3],
 [4,5,6],
 [7,8,9]
]

'''
grid[0][0...]
grid[len(grid[0])-1][0...]

grid[1...][0]
grid[1...][len(grid[0])-1]

-> 
'''

"""
Run DFS on 0's
    Mark # if not surrounded by land
  - you need a an array outside that stores the *coordinates* 0s you visited 
  - check for if it's not in the array, up down right left diagonals should be 1, 
  - if diagonals -> fucked, if udlr =0 then keep going dfs
    - base of DFS if reached border
    - backtrack set 0 -> #
  
For each zeros visited:
    Run DFS on nearby 1 and count land mass


def dfs(row, col):
  
    for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # Check all 4 directions
      new_row, new_col = row + x, col + y
      dfs(new_row, new_col)

    
"""
# pacific atlantic 


##############################
### TRAPPING RAIN WATER II ###
##############################
'''
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, 
return the volume of water it can trap after raining.

Idea: 

Initially the heap contains all cells on the perimeter of the map. 
Because it is ordered in increasing height, the first cell popped is the lowest point on the outer wall.
Check the 4 neighbours, ignoring any already explored (in the heap or have already been popped off the heap) or outside the map.
If a newly discovered neighbour is lower than the current cell then water can be added on top of it. We know the water cannot flow out anywhere because the current cell is the lowest.
Add the water to this neighbouring cell (zero if neighbour is higher than cell) and push neighbour with its new height onto the heap.

We are effectively continually raising the water level, filling in any "holes" as we go.

Every cell is pushed and popped from the heap, which is O(mn log(mn))

'''
def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0
            
        rows, cols = len(heightMap), len(heightMap[0])
        water = 0
        q = []

        for r in range(rows):
            heapq.heappush(q, (heightMap[r][0], r, 0))    
            heapq.heappush(q, (heightMap[r][cols - 1], r, cols - 1))    
        for c in range(1, cols - 1):
            heapq.heappush(q, (heightMap[0][c], 0, c))    
            heapq.heappush(q, (heightMap[rows - 1][c], rows - 1, c))    
    
        visited = {(r, c) for _, r, c in q}

        while q:
            
            h, r, c = heapq.heappop(q)
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r1, c1 = r + dr, c + dc
                if (r1, c1) not in visited and r1 >= 0 and c1 >= 0 and r1 < rows and c1 < cols:
                    visited.add((r1, c1))
                    water += max(0, h - heightMap[r1][c1])
                    heapq.heappush(q, (max(h, heightMap[r1][c1]), r1, c1))
                
        return water

######################
### UNIQUE PATHS I ###
######################

def uniquePaths(self, m, n):
    table = [[1 for x in range(n)] for x in range(m)]
    # for i in range(m):
    #     table[i][0] = 1
    # for i in range(n):
    #     table[0][i] = 1
    for i in range(1,m):
        for j in range(1,n):
            table[i][j] = table[i-1][j] + table[i][j-1]
    return table[m-1][n-1]



#######################
### UNIQUE PATHS II ###
#######################
'''
O(num) where is the num of nodes in the matrix (num of cells)
Each node/cell is visited only once
Or O(N*M) where N and M are the grid's dimensions
Space compleixty

O(1) in=place modification
Code
'''
def unique_path(grid):
    m = obstacleGrid
    if not m or m == [[]] or len(m)==0 or m[0][0] == 1:
        return 0
    
    # start:
    m[0][0] = 1
    
    # top row:
    for i in range(1, len(m[0])):
        if m[0][i] == 1: # obstacle
            m[0][i] = 0
        else:
            m[0][i] = m[0][i-1] # previous cell (cell to the left)
            
    # left most col:
    for i in range(1, len(m)):
        if m[i][0] == 1: # obstacle
            m[i][0] = 0
        else:
            m[i][0] = m[i-1][0] # previous cell (cell to the top)
            
    # rest of the grid:
    for i in range(1, len(m)):
        for j in range(1, len(m[0])):
            if m[i][j] == 1:
                m[i][j] = 0
            else:
                m[i][j] = m[i-1][j] + m[i][j-1]
                
    return m[len(m)-1][len(m[0])-1]