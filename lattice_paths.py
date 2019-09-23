def main():

    w, h = 22, 22;
    Matrix = [[0 for x in range(w)] for y in range(h)]

    # there has to be a starting value set to 1 that the initial point [1][1] is set to 1 the other are all 0
    Matrix[0][1] = 1
    # the matrix has to be bigger because we look at the edges so we need an extra row (one cell has 4 edges)
    # and an extra row on top and left that there is no need for edge cases
    for x in range(1, 22):
        for y in range(1, 22):
            Matrix[x][y] = Matrix[x - 1][y] + Matrix[x][y-1]
    print(Matrix[21][21])

if __name__ == '__main__':
    main()