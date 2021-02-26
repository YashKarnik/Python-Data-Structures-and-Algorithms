# return a boolean if a target sum can be achieve from an array of integers
def can_sum(a, target):
    t = [False]*(target+1)
    t[0] = True
    # n = len(a)
    for i in range(target+1):
        for j in a:
            if(i+j < target+1):
                t[i+j] = True
    print(*[i for i in enumerate(t)], sep=',')


if __name__ == '__main__':
    print(can_sum([2, 3, 4, 7], 7))
    print(can_sum([3, 34, 4, 12, 5, 2], 9))
