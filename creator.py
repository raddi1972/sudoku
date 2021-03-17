import solver
import random
import functools as fun


class Sudoku:
    def __init__(self, tries=21):
        self.grid = [[0 for j in range(0, 9)] for i in range(0, 9)]
        self.tries = tries
        self.createGrid()

    def createGrid(self):
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        val = random.randint(1, 9)
        self.grid[i][j] = val
        l = [0]
        self.solution = solver.solve_sudoku(self.grid)
        self.grid = removeElements(self.solution, self.tries)

    def __str__(self):
        s = str(fun.reduce(lambda x, y: x + str(fun.reduce(lambda x,
                                                           y: x + " " + str(y), y, "")) + '\n', self.grid, ""))
        return s


def removeElements(sud, tries):
    l = [x[:] for x in sud]
    index = [(i, j) for i in range(0, 9) for j in range(0, 9) if l[i][j] != 0]
    while len(index):
        rand = random.randint(0, len(index) - 1)
        (i, j) = index[rand]
        temp = l[i][j]
        l[i][j] = 0
        sol = [0]
        solver.pcheck_sudoku(l, sol)
        index.pop(rand)
        if sol[0] == 2:
            tries -= 1
            l[i][j] = temp
            index.append((i, j))
        if tries == 0:
            return l


if __name__ == "__main__":
    sud = Sudoku()
    l = [0]
    solver.pcheck_sudoku(sud.grid, l)
    print(l)
    print(sud)
