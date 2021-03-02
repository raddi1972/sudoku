# Test Sudoku to be solved using this algorithm.
sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def reverse(s):
    sout = {0}
    for i in range(1, 10):
        if not i in s:
            sout.add(i)
    return sout


def getBlock(sud, i, j):
    block = 0
    for c in range(0, 3):
        if i > 3 * c + 2:
            block += 3
        if j > 3 * c + 2:
            block += 1
    return block


def getElements(sud, i, j):
    block = getBlock(sud, i, j)
    elements = {0}

    # Checking row for elemets in sudoku
    for x in sud[i]:
        if not x == 0:
            elements.add(x)

    # Checking column for elements in sudoku
    for x in sud:
        if not x[j] == 0:
            elements.add(x[j])

    # Checking block for elements in sudoku
    for x in range((3 * (block // 3)), (3 * (block // 3)) + 3):
        for y in range(3 * (block % 3), (3 * (block % 3)) + 3):
            if not sud[x][y] == 0:
                elements.add(sud[x][y])

    # Reversing the elements so we get elements that can be filled in position
    rev = reverse(elements)
    rev.remove(0)
    return rev


def isCompleted(sud):
    for i in range(0, 9):
        for j in range(0, 9):
            if sud[i][j] == 0:
                return False
    return True


def printGrid(sud):
    for i in sud:
        for j in i:
            print(j, end=" ")
        print()


def indexGrid(sud):
    l = []
    for i in range(0, 9):
        for j in range(0, 9):
            if sud[i][j] == 0:
                l.append((i, j))
    return l


def solve_sudoku(sud):
    l = [x[:] for x in sud]
    if isCompleted(l):
        return l
    indexes = indexGrid(l)
    for x in indexes:
        (i, j) = x
        if l[i][j] == 0:
            s = getElements(l, i, j)
            if len(s) == 0:
                return []
            print('Position :', i, j, 'Set :', s, 'Grid : ')
            printGrid(l)
            for element in s:
                print('checking', element, 'of', s)
                l[i][j] = element
                sol = solve_sudoku(l)
                if len(sol):
                    return sol
            return []


if __name__ == "__main__":
    printGrid(solve_sudoku(sudoku))
    # for i in range(0, 9):
    #     for j in range(0, 9):
    #         if sudoku[i][j] == 0:
    #             print(i, j, getElements(sudoku, i, j))
