"""
Sasha and His Trip -
https://codeforces.com/problemset/problem/1113/A
"""
n, v = map(int, input().split(' '))
cost_arr = [i for i in range(1, n + 1)]
min_cost = 0
d = n - 1
index = 0
while d > 0:
    if d - v >= 0:
        remain = v
    else:
        remain = d

    print("Remain is: %s" % remain)

    min_cost += cost_arr[index] * remain
    d -= remain
    print("Cost and d: %s and %s" % (min_cost, d))
    index += 1

print(min_cost)