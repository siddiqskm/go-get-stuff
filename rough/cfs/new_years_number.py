"""
New Year's Number
https://codeforces.com/problemset/problem/1475/B
"""
for _ in range(int(input())):
    num = int(input())
    div, rem = divmod(num, 2020)
    if rem <= div:
        print("YES")
    else:
        print("NO")