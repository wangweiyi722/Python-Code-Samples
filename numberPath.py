#  File: numberPath.py
#  Description: Simulate a maze using a grid of numbers
#  Student's Name: Weiyi Wang
#  Student's UT EID: ww6874
#  Course Name: CS 313E 
#  Unique Number: 87530
#
#  Date Created: 7/25/2016
#  Date Last Modified: 7/29/2016


class Problem(object):

    orig_grid = []
    orig_pathHistory = []
    orig_startRow = 0
    orig_startCol = 0
    orig_targetSum = 0


    def __init__(self,grid,pathHistory,rowDimension,colDimension,startRow,startCol,endRow,endCol):

        self.grid = grid
        self.grid_rows = len(grid)
        self.grid_cols = len(grid[0])
        self.pathHistory = pathHistory
        self.startRow = startRow
        self.startCol = startCol
        self.total = 0
        self.endRow = endRow
        self.endCol = endCol

        # Store the directions for backtracking purposes
        self.dirHistory = []

        # Use this as a flag to tell the recursive procedure to stop
        self.solutionFound = False
        

    def __str__(self):
        
        # First get a neatly organized grid.
        gridStr = 'Grid:' + '\n'
        for row in self.grid:
            for col in row:
                gridStr = gridStr + '{:<7}'.format(str(col))

            gridStr = gridStr + '\n'

        gridStr = gridStr + '\n'
    

        histStr = 'history: ' + str(self.pathHistory)+'\n'

        startStr = 'start point: '+'('+str(self.startRow)+','+str(self.startCol)+') \n'

        totalStr = 'total so far: '+str(self.total)+'\n'

        return gridStr + histStr + startStr + totalStr

# Input a problem and the next proposed space and see if it is valid
def isValid(problem,nextRow,nextCol):

    # In order to be a valid space:
    # 1. Must be within dimensions of grid
    # 2. Cannot be a space already visited, no None value
    
    if 0 <= nextRow <= problem.grid_rows-1 and 0 <= nextCol <= problem.grid_cols-1:
        return problem.grid[nextRow][nextCol] != None
    else:
        return False

# Feed it a problem
# Recursively solve until get to the end with proper sum
def solve(problem):

    
    
    print('Is this a goal state?')
    print()


    # Base case is when the solution is found
    if problem.startRow == problem.endRow and problem.startCol == problem.endCol and problem.total == Problem.orig_targetSum:

        print('Yes')
        print('Solution found')
        print(problem.pathHistory)
        problem.solutionFound = True
        return(problem.pathHistory)

    # If the total exceeds the target, then this path is no good
    elif problem.total > Problem.orig_targetSum:

        print('Exceeded target sum... backtracking')
        if problem.dirHistory[-1] == 'r':
            problem.grid[problem.startRow][problem.startCol] = problem.pathHistory[-1]
            problem.total -= problem.pathHistory[-1]
            problem.pathHistory.pop()
            problem.dirHistory.pop()
            problem.startCol -= 1
        elif problem.dirHistory[-1] == 'u':
            problem.grid[problem.startRow][problem.startCol] = problem.pathHistory[-1]
            problem.total -= problem.pathHistory[-1]
            problem.pathHistory.pop()
            problem.dirHistory.pop()
            problem.startRow += 1
        elif problem.dirHistory[-1] == 'd':
            problem.grid[problem.startRow][problem.startCol] = problem.pathHistory[-1]
            problem.total -= problem.pathHistory[-1]
            problem.pathHistory.pop()
            problem.dirHistory.pop()
            problem.startRow -= 1
        elif problem.dirHistory[-1] == 'l':
            problem.grid[problem.startRow][problem.startCol] = problem.pathHistory[-1]
            problem.total -= problem.pathHistory[-1]
            problem.pathHistory.pop()
            problem.dirHistory.pop()
            problem.startCol += 1 
        
        return None

    # Otherwise, go try to move around through the maze
    elif not problem.solutionFound:

        if not problem.solutionFound:
            print('No.  Can I move right?')
            print()
            
        # Try to move Right
        if isValid(problem,problem.startRow,problem.startCol + 1) and not problem.solutionFound:

            # Change the problem instance to one where you've moved right
            print('Yes')
            print('Moving right:')
            problem.startCol += 1
            problem.pathHistory.append(problem.grid[problem.startRow][problem.startCol])
            problem.total += problem.grid[problem.startRow][problem.startCol]
            problem.grid[problem.startRow][problem.startCol] = None
            problem.dirHistory.append('r')
            print(problem)

            solve(problem)

        if not problem.solutionFound: 
            print('No.  Can I move up?')
            print()
            
        # Try to move Up
        if isValid(problem,problem.startRow-1,problem.startCol) and not problem.solutionFound:
            print('Yes')
            print('Moving up:')
            problem.startRow -= 1
            problem.pathHistory.append(problem.grid[problem.startRow][problem.startCol])
            problem.total += problem.grid[problem.startRow][problem.startCol]
            problem.grid[problem.startRow][problem.startCol] = None
            problem.dirHistory.append('u')
            print (problem)

            solve(problem)

        if not problem.solutionFound:
            print('No.  Can I move down?')
            print()
            
        # Try to move Down
        if isValid(problem,problem.startRow+1,problem.startCol) and not problem.solutionFound:
            print('Yes')
            print('Moving down:')
            problem.startRow += 1
            problem.pathHistory.append(problem.grid[problem.startRow][problem.startCol])
            problem.total += problem.grid[problem.startRow][problem.startCol]
            problem.grid[problem.startRow][problem.startCol] = None
            problem.dirHistory.append('d')
            print (problem)
            
            solve(problem)

        if not problem.solutionFound:
            print('No.  Can I move left?')
            print()
            
        #Try to move Left
        if isValid(problem,problem.startRow,problem.startCol-1) and not problem.solutionFound:
            print('Yes')
            print('Moving left:')
            problem.startCol -= 1
            problem.pathHistory.append(problem.grid[problem.startRow][problem.startCol])
            problem.total += problem.grid[problem.startRow][problem.startCol]
            problem.grid[problem.startRow][problem.startCol] = None
            problem.dirHistory.append('l')
            print (problem)

            solve(problem)


        # You've made it past all the if statements, meaning you can't move in any direction
        # All options are exhausted, so backtrack one step and return None for the current iteration of solve
        if not problem.solutionFound:
            print('Exhausted all options for path...  Backtracking')
            print()
            
        if problem.dirHistory[-1] == 'r':
            problem.grid[problem.startRow][problem.startCol] = problem.pathHistory[-1]
            problem.total -= problem.pathHistory[-1]
            problem.pathHistory.pop()
            problem.dirHistory.pop()
            problem.startCol -= 1
        elif problem.dirHistory[-1] == 'u':
            problem.grid[problem.startRow][problem.startCol] = problem.pathHistory[-1]
            problem.total -= problem.pathHistory[-1]
            problem.pathHistory.pop()
            problem.dirHistory.pop()
            problem.startRow += 1
        elif problem.dirHistory[-1] == 'd':
            problem.grid[problem.startRow][problem.startCol] = problem.pathHistory[-1]
            problem.total -= problem.pathHistory[-1]
            problem.pathHistory.pop()
            problem.dirHistory.pop()
            problem.startRow -= 1
        elif problem.dirHistory[-1] == 'l':
            problem.grid[problem.startRow][problem.startCol] = problem.pathHistory[-1]
            problem.total -= problem.pathHistory[-1]
            problem.pathHistory.pop()
            problem.dirHistory.pop()
            problem.startCol += 1

        
        
        return None


       
def main():


    in_file = open('pathdata3.txt','r')
    dataLine = in_file.readline().split()
    target = int(dataLine[0])
    grid_rows = int(dataLine[1])
    grid_cols = int(dataLine[2])
    start_row = int(dataLine[3])
    start_col = int(dataLine[4])
    end_row = int(dataLine[5])
    end_col = int(dataLine[6])
    gridList = []
    for line in in_file:

        gridList.append(line.split())


    # Convert all the elements of gridList into integers
    row = 0
    col = 0
    
    while row < len(gridList):
        
        while col < len(gridList[row]):
            
            gridList[row][col] = int(gridList[row][col])
            col += 1

        col = 0
        row += 1


  


    maze = Problem(gridList,[],grid_rows,grid_cols,start_row,start_col,end_row,end_col)
    # Input all this data into a Problem object
    Problem.orig_grid = gridList
    Problem.orig_pathHistory = []
    Problem.orig_startRow = start_row
    Problem.orig_startCol = start_col
    Problem.orig_targetSum = target

    

    
    print('Start State:')
    print(maze)

    

    # Put the starting point in
    print('Entering maze:')
    maze.pathHistory.append(maze.grid[maze.startRow][maze.startCol])
    maze.total += maze.grid[maze.startRow][maze.startCol]
    maze.grid[maze.startRow][maze.startCol] = None
    print(maze)




    solve(maze)

    

main()
