import solver
import random


def removeElements(sud, tries):
    l = [x[:] for x in sud]
    index = solver.indexGrid(l, False)
    while len(index):
        index = solver.indexGrid(l, False)
        rand = random.randint(0, len(index) - 1)
        (i, j) = index[rand]
        temp = l[i][j]
        l[i][j] = 0
        sol = [0]
        solver.solve_sudoku(l, sol, 2)
        if sol[0] == 2:
            tries -= 1
            l[i][j] = temp
        if tries == 0:
            return l


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
    n = 5
    sudoku = removeElements(l[1], n)
    f = [0]
    solver.solve_sudoku(sudoku, f, 2)
    solver.printGrid(sudoku)


if __name__ == "__main__":
    createGrid()
