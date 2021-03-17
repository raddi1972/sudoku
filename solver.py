import random
import functools as fun
# Test Sudoku to be solved using this algorithm.
# sudoku = [
#     [3, 0, 6, 5, 0, 8, 4, 0, 0],
#     [5, 2, 0, 0, 0, 0, 0, 0, 0],
#     [0, 8, 7, 0, 0, 0, 0, 3, 1],
#     [0, 0, 3, 0, 1, 0, 0, 8, 0],
#     [9, 0, 0, 8, 6, 3, 0, 0, 5],
#     [0, 5, 0, 0, 9, 0, 6, 0, 0],
#     [1, 3, 0, 0, 0, 0, 2, 5, 0],
#     [0, 0, 0, 0, 0, 0, 0, 7, 4],
#     [0, 0, 5, 2, 0, 6, 3, 0, 0]
# ]

cache = []


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
    elements = {i for i in range(1, 10)}

    # Checking row for elemets in sudoku
    for x in sud[i]:
        if not x == 0:
            try:
                elements.remove(x)
            except:
                pass

    # Checking column for elements in sudoku
    for x in sud:
        if not x[j] == 0:
            try:
                elements.remove(x[j])
            except:
                pass

    # Checking block for elements in sudoku
    for x in range((3 * (block // 3)), (3 * (block // 3)) + 3):
        for y in range(3 * (block % 3), (3 * (block % 3)) + 3):
            if not sud[x][y] == 0:
                try:
                    elements.remove(sud[x][y])
                except:
                    pass
    return elements


def isCompleted(sud):
    for i in range(0, 9):
        for j in range(0, 9):
            if sud[i][j] == 0:
                return False
    return True


def pcheck_sudoku(sud):
    cache = [x[:] for x in sud]
    counter = [0]
    check_sudoku(sud, counter)
    return counter


def solve_sudoku(sud):
    indexes = [(i, j) for i in range(0, 9)
               for j in range(0, 9) if sud[i][j] == 0]
    if len(indexes) == 0:
        return sud
    for x in indexes:
        (i, j) = x
        s = list(getElements(sud, i, j))
        while len(s):
            rand = random.randint(0, len(s)-1)
            sud[i][j] = s[rand]
            if solve_sudoku(sud) != []:
                return sud
            s.pop(rand)
        sud[i][j] = 0
        return []


def check_sudoku(sud, counter):
    indexes = [(i, j) for i in range(0, 9)
               for j in range(0, 9) if sud[i][j] == 0]
    for i in sud:
        for j in i:
            if sud[i][j] == cache[i][j]:
                temp = sud[i][j]
                if temp == 0:
                    indexes.remove((i, j))
            else:
                break
    if len(indexes) == 0:
        counter[0] += 1
        counter.append([x[:] for x in sud])
        return counter
    for x in indexes:
        (i, j) = x
        elements = getElements(sud, i, j)
        if len(elements) == 0:
            return
        elements = list(elements)
        for s in elements:
            sud[i][j] = s
            check_sudoku(sud, counter)
            if counter[0] == 2:
                return counter
        sud[i][j] = 0
        return


if __name__ == "__main__":
    lst = [0]
    # pcheck_sudoku(sudoku, lst, 1)
    print(lst)
    # for i in range(0, 9):
    #     for j in range(0, 9):
    #         if sudoku[i][j] == 0:
    #             print(i, j, getElements(sudoku, i, j))
