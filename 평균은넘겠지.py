def over_rate():
    ls = list(map(int, input().split()))
    average = sum(ls[1:]) / len(ls[1:])
    cnt = 0
    for i in range(1, len(ls)):
        if ls[i] > average: cnt += 1
    return cnt / (len(ls) - 1) * 100


n = int(input())
rst = []
for i in range(n):
    rst.append(over_rate())

for i in range(n):
    print(f"{rst[i]:.3f}%")
