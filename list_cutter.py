import sys

total = int(sys.stdin.next())
sticks = [int(stick) for stick in sys.stdin.next().split()]

sticks.sort()
while sticks:
    sticks = filter(lambda a: a > 0,[i - sticks[0] for i in sticks])
    print sticks