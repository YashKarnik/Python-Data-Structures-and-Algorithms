# Given a grid of m rows and n columns return number of ways on can traverse the grid
# if starting point in top-left and endpoint in bottom right
# Legal moves are down and right
#  ------------------
# |S    |     |     |
# -------------------
# |     |     |     |
# -------------------
# |     |     |     |
# -------------------
# Legal ways =6


def grid_traveller(m, n):
    ways = [[1 for i in range(n)] for i in range(m)]
    # print(*ways,sep='\n')
    for i in range(1, m):
        for j in range(1, n):
            ways[i][j] = ways[i][j-1]+ways[i-1][j]
    # print(*ways,sep='\n')
    return ways[m-1][n-1]


if __name__ == '__main__':
    print(grid_traveller(3, 3))
    print(grid_traveller(6, 6))
    print(grid_traveller(18, 18))
