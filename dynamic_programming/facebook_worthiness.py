M = [[]]
m = [[]]
ops = []

def facebook_worthiness(numbers, operations) -> int:
    if len(numbers) <= 0:
        return -1
    if len(numbers) != len(operations) + 1:
        return 1
    global M, m, ops

    ops = operations

    M = [[None] * len(numbers) for _ in range(len(numbers))]
    m = [[None] * len(numbers) for _ in range(len(numbers))]

    for i in range(len(numbers)):
        M[i][i] = numbers[i]
        m[i][i] = numbers[i]
    
    diff = maximum(0, len(numbers)-1) - minimum(0, len(numbers)-1)
    print(M)
    print(m)
    return diff

def maximum(i, j):
    if M[i][j] is not None:
        return M[i][j]
    ma = -1 << 32
    for k in range(i, j):
        front_max = maximum(i, k)
        front_min = minimum(i, k)
        back_min = maximum(k+1, j)
        back_max = minimum(k+1, j)
        options = [front_max + back_max * ops[k], front_max + back_min * ops[k], front_min + back_max * ops[k], front_min + back_min * ops[k]]
        if max(options) > ma:
            ma = max(options)
    M[i][j] = ma 
    return ma

def minimum(i, j):
    if m[i][j] is not None:
        return m[i][j]
    mi = 1 << 32
    for k in range(i, j):
        front_max = maximum(i, k)
        front_min = minimum(i, k)
        back_min = maximum(k+1, j)
        back_max = minimum(k+1, j)
        options = [front_max + back_max * ops[k], front_max + back_min * ops[k], front_min + back_max * ops[k], front_min + back_min * ops[k]]
        if min(options) < mi:
            mi = min(options)
    m[i][j] = mi
    return mi

print(facebook_worthiness([1,2,3,4,5,6,7,8,9,7,5,2,3,6,4,5,4,10],[1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,1,-1,1,-1,1]))