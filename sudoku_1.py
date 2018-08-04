
import numpy as np

grid = np.array([
    (0, 0, 5, 8, 7, 1, 4, 0, 0),
    (0, 1, 7, 0, 0, 0, 8, 9, 5),
    (4, 0, 0, 0, 0, 0, 0, 1, 7),
    (7, 3, 0, 2, 5, 4, 0, 8, 6),
    (5, 4, 0, 1, 6, 8, 0, 7, 0),
    (8, 6, 0, 9, 3, 7, 0, 5, 4),
    (2, 5, 0, 0, 0 ,0, 7, 4, 9),
    (0, 7, 0, 0, 0, 0, 0, 2, 0),
    (0, 0, 4, 7, 0, 2, 5, 0, 0)
    ])

grid_original = np.array(grid, copy=True)

def grid_ref(number):
    grid_ref = (number//9, number%9)
    return grid_ref

def value(grid, number):
    g_r = grid_ref(number)
    value = grid[g_r]
    return value

def cell(grid, number):
    g_r = grid_ref(number)
    cell_ref = (g_r[0]//3, g_r[1]//3)
    cell = grid[((cell_ref[0])*3):((cell_ref[0])*3)+3, ((cell_ref[1])*3):((cell_ref[1])*3)+3]
    return cell

def row(grid, number):
    g_r = grid_ref(number)
    row_ref = g_r[0]
    row = grid[(row_ref):(row_ref+1), 0:9]
    return row

def column(grid, number):
    g_r = grid_ref(number)
    column_ref = g_r[1]
    column = grid[0:9, (column_ref):(column_ref+1)]
    return column

print(grid)
print("\n Processing... \n")

forwards = True
i = 0

while i <9*9:

    if value(grid_original, i) == 0 and forwards:
        for a in range(1, 10):
            if a not in cell(grid, i) and a not in row(grid, i) and a not in column(grid, i):
                grid[grid_ref(i)] = a
                i += 1
                break
            else:
                if a == 9:
                    forwards = False
                    i -= 1 #goes back a cell
                    break
    elif value(grid_original, i) != 0 and forwards:
        i += 1

    elif value(grid_original, i) == 0 and not forwards:
        if grid[grid_ref(i)] == 9:
            grid[grid_ref(i)] = 0
            i -= 1
        else:
            for a in range(grid[grid_ref(i)]+1, 10):
                if a not in cell(grid, i) and a not in row(grid, i) and a not in column(grid, i):
                    grid[grid_ref(i)] = a
                    forwards = True
                    i += 1
                    break
                else:
                    if a == 9:
                        grid[grid_ref(i)] = 0
                        i -= 1
                        break

    elif value(grid_original, i) != 0 and not forwards:
        i -= 1

print(grid)
