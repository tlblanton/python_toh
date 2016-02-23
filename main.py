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
        end.stack.append(start.stack.pop())
        moves += 1
        print("{0} -> {1}").format(start.name, end.name)
        display(A.stack, B.stack, C.stack)
    else:
        hanoi(ringNum-1, start, end, aux)
        end.stack.append(start.stack.pop())
        print("{0} -> {1}").format(start.name, end.name)
        moves += 1
        display(A.stack, B.stack, C.stack)
        hanoi(ringNum-1, aux, start, end)


class customStack:
    def __init__(self, nName):
        self.name = nName
        self.stack = []

A = customStack("A")
B = customStack("B")
C = customStack("C")

rings = int(raw_input("How many rings are on tower A?\n"))
n = rings

while n:
    A.stack.append(n)
    n -= 1

display(A.stack, B.stack, C.stack)
hanoi(rings, A, B, C)
print "Number of moves: {0}".format(moves)