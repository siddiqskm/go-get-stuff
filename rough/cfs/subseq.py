"""
Non-Substring Subsequence -
https://codeforces.com/problemset/problem/1451/B
"""
for _ in range(int(input())):
    n, q = map(int, input().split())
    s = input()
    for i in range(q):
        l, r = map(int, input().split())
        print("%s in %s and %s in %s" %(s[l-1], s[:l-1], s[r-1], s[r:]))
        if s[l-1] in s[:l-1] or s[r-1] in s[r:]:
            print("YES")
        else:
            print("NO")