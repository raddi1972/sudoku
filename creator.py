import solver
import random


def removeElements(sud, tries):
    l = [x[:] for x in sud]
    indexes = solver.indexGrid(l, False)
    if (len(indexes) == 20 or tries[0] == 0) and len(indexes) <= 31:
        return l
    while len(indexes):
        rand = random.randint(0, len(indexes) - 1)
        (i, j) = indexes[rand]
        temp = l[i][j]
        l[i][j] = 0
        sols = [0]
        solver.solve_sudoku(l, sols, 2)
        if sols[0] == 2:
            tries[0] -= 1
            l[i][j] = temp
            indexes.pop(rand)
            continue
        sol = removeElements(l, tries)
        if len(sol) == 0:
            indexes.pop(rand)
            continue
        return sol
    return []


def createGrid():
    lst = []
    for i in range(0, 9):
        lst.append([])
        for j in range(0, 9):
            lst[i].append(0)

    i = random.randint(0, 8)
    j = random.randint(0, 8)
    val = random.randint(1, 9)
    lst[i][j] = val
    # solver.printGrid(lst)
    l = [0]
    solver.solve_sudoku(lst, l)
    print(l[0])
    solver.printGrid(l[1])
    n = [3]
    sudoku = removeElements(l[1], n)
    f = [0]
    solver.solve_sudoku(sudoku, f, 2)
    solver.printGrid(sudoku)


if __name__ == "__main__":
    createGrid()
