import sys
N = int(sys.stdin.readline())
ropes = []
for i in range(N):
    a= int(sys.stdin.readline())
    ropes.append(a)
ropes.sort()
before = len(ropes)*ropes[0]
while ropes !=[]:
    ropes.remove(ropes[0])
    if ropes !=[]:
        if len(ropes)*ropes[0] > before:
            before = len(ropes)*ropes[0]
print(before)
