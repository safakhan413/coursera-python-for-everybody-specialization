# x = {}

x = [[1,2,3],
     [4,5,6],
     [7,8,9],
     [3,-4,-6]]



def calcSumDiag(x):
    '''
    Algo:
    Output: sum of diagonals of matrix
    input: matrix

    Steps:
    1. Start with size of the matrix x
    2. track another var y initially -1
    3. For each iteration on size of x, get the value y+1
    4. use variable sum to store and add
    '''
    width = len(x)
    # print(width)
    length = len(x[0])

    if width != length:
        return -1
    y = -1
    sum = 0
    for i in x:
        # print(i, '\n')
        y = y+1
        # print(i[y])
        sum = sum + i[y]

    return sum



b = calcSumDiag(x)
print(b)

