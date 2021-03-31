import io, os, sys
input = sys.stdin.readline
def find(arr, l, r, num):
    i = l
    while (i < r):
        if (arr[i] == num):
            return i
        i += 1
    return i

arr = []
while True:
    inputs = [int(x) for x in input().split()]
    if inputs[0] == 0:
        arr.insert(0, inputs[1])
    elif inputs[0] == 1:
        arr.append(inputs[1])
    elif inputs[0] == 2:
        i = find(arr, 0, len(arr), inputs[1])
        if i < len(arr):
            arr.insert(i + 1, inputs[2])
        else:
            arr.insert(0, inputs[2])
    elif inputs[0] == 3:
        i = find(arr, 0, len(arr), inputs[1])
        if (i < len(arr)):
            arr.remove(inputs[1])
    elif inputs[0] == 4:
        i = 0
        while i < len(arr):
            i = find(arr, i, len(arr), inputs[1])
            if (i < len(arr)):
                arr.remove(inputs[1])
    elif inputs[0] == 5:
        if (len(arr) > 0):
            arr.remove(arr[0])
    else:
        break
    inputs.clear()

if (len(arr) > 0):
    sys.stdout.write(" ".join(map(str, arr)) + "\n")
else:
    print("blank")