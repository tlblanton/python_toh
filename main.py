import sys

moves = 0


def display(aCopy, bCopy, cCopy):
    print '** Move Number: {0}'.format(moves)
    sys.stdout.write("[")
    for num in range(len(aCopy)):
        sys.stdout.write('%s' % aCopy[num])
        if num != len(aCopy)-1:
            sys.stdout.write(", ")
        else:
            print ']'
    if len(aCopy) == 0:
        print(']')

    sys.stdout.write("[")
    for num in range(len(bCopy)):
        sys.stdout.write('%s' % bCopy[num])
        if num != len(bCopy)-1:
            sys.stdout.write(", ")
        else:
            print(']')
    if len(bCopy) == 0:
        print(']')

    sys.stdout.write("[")
    for num in range(len(cCopy)):
        sys.stdout.write('%s' % cCopy[num])
        if num != len(cCopy)-1:
            sys.stdout.write(", ")
        else:
            print ']'
    if len(cCopy) == 0:
        print(']')
    print('----------------------------------------------------')


def hanoi(ringNum, start, aux, end):
    global moves
    if ringNum == 1:
        end.append(start.pop())
        moves += 1
        display(A, B, C)
    else:
        hanoi(ringNum-1, start, end, aux)
        end.append(start.pop())
        moves += 1
        display(A, B, C)
        hanoi(ringNum-1, aux, start, end)


A = []
B = []
C = []


rings = input("How many rings are on tower A?\n")
n = rings

while n:
    A.append(n)
    n -= 1


display(A, B, C)
hanoi(rings, A, B, C)
print "Number of moves: {0}".format(moves)