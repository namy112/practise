"""
:type grid: List[List[int]]
:rtype: int
"""
# grid =[[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

grid =[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]
     ]

def test(grid):
    for row in range(len(grid)):
        for col in  range (len(grid[0])):
            print grid[row][col],
        print('')

#Given a grid and a cell index [r][c], get the 4 adjacent neighbors of the cell in the grid
def getAdj(grid, r, c):
    
    minRow=0
    minCol=0
    maxRow= len(grid)
    maxCol = len(grid[0])
        
    left= [grid[r][c-1] for r,c in grid if c>minCol]
#     right = grid[r][c+1]
#     up = grid [r-1][c]
#     down = grid[r+1][c]
    print(left)
    
getAdj(grid, 2, 2)
    


