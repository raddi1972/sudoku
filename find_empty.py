def find_empty (G):
    
    for i in range (9):
        for j in range (9):
            if G[i][j] == 0:
                return i,j


# calling find_empty
    #empty = find_empty(G)
   # if not empty: #no empty spots are left so the board is solved
    return True
