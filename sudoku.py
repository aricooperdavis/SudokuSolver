import numpy as np
#just because its arrays are so nice

grid = np.array([
    (6, 0, 0, 0, 0, 0, 0, 5, 1),
    (0, 0, 0, 3, 0, 0, 9, 0, 0),
    (0, 0, 8, 0, 0, 0, 0, 0, 0),
    (0, 4, 0, 7, 0, 0, 5, 0, 0),
    (0, 0, 0, 0, 9, 0, 8, 0, 0),
    (0, 0, 1, 8, 5, 0, 0, 3, 7),
    (5, 0, 2, 6, 0 ,0, 0, 0, 4),
    (3, 0, 0, 0, 0, 7, 0, 2, 9),
    (0, 0, 4, 0, 0, 0, 0, 0, 0)
    ])
#this is the original sudoku grid

grid_original = np.array(grid, copy=True)
#make a copy of the grid so that we don't edit the original

def grid_ref(number):
    """function converts linear 0-81 item reference to (y,x) item reference"""
    grid_ref = (number//9, number%9)
    #to get the row we divide by nine and ignore the remainder
    #to get the column we divide by nine and only look at the remainder
    return grid_ref

def value(grid, number):
    """function gets value of given linear item"""
    g_r = grid_ref(number)
    value = grid[g_r]
    #just check a given grid for a given grid reference
    return value

def cell(grid, number):
    """function returns array describing the cell that a linear item is in"""
    g_r = grid_ref(number)
    cell_ref = (g_r[0]//3, g_r[1]//3)
    cell = grid[((cell_ref[0])*3):((cell_ref[0])*3)+3, ((cell_ref[1])*3):((cell_ref[1])*3)+3]
    #cells are 3 wide and high
    return cell

def row(grid, number):
    """function returns array describing the row that a linear item is in"""
    g_r = grid_ref(number)
    row_ref = g_r[0]
    row = grid[(row_ref):(row_ref+1), 0:9]
    return row

def column(grid, number):
    """function returns array describing the column that a linear item is in"""
    g_r = grid_ref(number)
    column_ref = g_r[1]
    column = grid[0:9, (column_ref):(column_ref+1)]
    return column

print(grid)
#print the initial sudoku grid

forwards = True
i = 0

while i <9*9:
    print("Checking original grid cell "+str(grid_ref(i))+"...")

    if value(grid_original, i) == 0 and forwards:
        print("Cell is empty in original grid, can place here.")
        for a in range(1, 10):
            print("Checking rows, columns, and cells for "+str(a)+"s ...")
            if a not in cell(grid, i) and a not in row(grid, i) and a not in column(grid, i):
                print("Placing "+str(a)+" at "+str(grid_ref(i))+".")
                grid[grid_ref(i)] = a
                i += 1
                print(grid)
                break
            else:
                print("Can't place "+str(a)+" here.")
                if a == 9:
                    print("We can't place anything here!")
                    forwards = False
                    i -= 1 #goes back a cell
                    break
    elif value(grid_original, i) != 0 and forwards:
        print("Cell is filled in original grid, can't place here.")
        i += 1

    elif value(grid_original, i) == 0 and not forwards:
        print("Cell is empty in original grid, can edit this one.")
        if grid[grid_ref(i)] == 9:
            print("Cell can't be any other value; we can't place anything here!")
            grid[grid_ref(i)] = 0
            print("Resetting "+str(grid_ref(i))+" to zero.")
            print(grid)
            i -= 1
        else:
            for a in range(grid[grid_ref(i)]+1, 10):
                print("Checking rows, columns, and cells for "+str(a)+"s...")
                if a not in cell(grid, i) and a not in row(grid, i) and a not in column(grid, i):
                    print("Placing "+str(a)+" at "+str(grid_ref(i))+".")
                    grid[grid_ref(i)] = a
                    print(grid)
                    forwards = True
                    i += 1
                    break
                else:
                    print("Can't place "+str(a)+" here.")
                    if a == 9:
                        print("We can't place anything here!")
                        grid[grid_ref(i)] = 0
                        print(grid)
                        i -= 1
                        break

    elif value(grid_original, i) != 0 and not forwards:
        print("Cell is filled in orignial grid, can't place here.")
        i -= 1

print(grid)
