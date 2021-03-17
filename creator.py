import solver
import random
import functools as fun


class Sudoku:
    def __init__(self):
        self.grid = [[0 for j in range(0, 9)] for i in range(0, 9)]
        self.createGrid()

    def createGrid(self):
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        val = random.randint(1, 9)
        self.grid[i][j] = val
        l = [0]
        self.solution = solver.solve_sudoku(self.grid)
        print(self.solution)
        self.removeElements()

    def removeElements(self):
        l = [x[:] for x in self.grid]
        index = [(i, j) for i in range(0, 9)
                 for j in range(0, 9) if l[i][j] != 0]
        while len(index):
            rand = random.randint(0, len(index) - 1)
            (i, j) = index[rand]
            temp = l[i][j]
            l[i][j] = 0
            sol = solver.pcheck_sudoku(l)
            print(sol)
            index.pop(rand)
            if sol[0] == 2:
                l[i][j] = temp
        self.grid = l

    def __str__(self):
        s = str(fun.reduce(lambda x, y: x + str(fun.reduce(lambda x,
                                                           y: x + " " + str(y), y, "")) + '\n', self.grid, ""))
        return s


if __name__ == "__main__":
    sud = Sudoku()
    n = 0
    for i in sud.grid:
        for j in i:
            if j != 0:
                n += 1
    print(solver.pcheck_sudoku(sud.grid))
    print(sud, n)
