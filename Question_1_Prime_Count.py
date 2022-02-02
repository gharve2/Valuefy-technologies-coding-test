a = [1]*100001
count = [0]*100001
a[0] = a[1] = 0
for i in range(2, 100001):
    if a[i]:
        count[i] += 1
        for j in range(i*2,  100001, i):
            a[j] = 0
            count[j] += 1
d = [[0, 0] for _ in range(6)]
for i in range(1, 6):
    for j in range(2, 100001):
        d[i].append(d[i][-1] + (count[j] == i))

for _ in range(int(input())):
    aa, bb, kk = map(int, input().split())
    print(d[kk][bb] - d[kk][aa-1])