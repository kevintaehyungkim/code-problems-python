
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

        def dp(i,j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                if i > 0 : dp(i-1,j)
                if i < M-1 : dp(i+1,j)
                if j > 0 : dp(i,j-1)
                if j < N-1 : dp(i,j+1)
        
        cnt = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    dp(i,j)
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
        """
        :type grid: List[List[int]]
        :rtype: int
        """
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