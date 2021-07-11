"""
Make Product Equal One -
https://codeforces.com/problemset/problem/1206/B
"""
n = int(input())
arr = map(int, input().split(' '))
sign = 1
cost = 0
for each_ele in arr:
    if each_ele > 0:
        cost += each_ele - 1
        sign *= 1
    elif each_ele < 0:
        cost += abs(each_ele) - 1
        sign *= -1
    else:
        cost += 1
        if sign == -1:
            sign = 1

if sign == -1:p;'m'
print(cost)
    