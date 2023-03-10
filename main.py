with open('./VstupyMesta.txt') as f:
    size = f.readlines()[0]
    size = size.split()
    row = int(size[0])
    col = int(size[1])

with open('./VstupyMesta.txt') as f:
    stations = f.readlines()[1:]

arr = []
s = []
for i in stations:
    x = i.split()
    x = list(map(list, x))
    arr.append(x[0])


def dist(x1, x2, y1, y2):
    return abs(x2 - y2) + abs(x1 - y1)


def fun():
    for i in range(row):
        for j in range(col):
            if(arr[i][j] == 'S'):
                s.append([i, j])

fun()


def ret():
    for i in range(row):
        for j in range(col):
            min = dist(s[0][0], s[0][1], i, j)
            for k in range(len(s)):
                newmin = dist(s[k][0], s[k][1], i, j)
                if(newmin < min):
                    min = newmin

            arr[i][j] = min

ret()
print(arr)
