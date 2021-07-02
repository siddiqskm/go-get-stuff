"""
Pretty Permutations -
https://codeforces.com/contest/1541/problem/A
"""
for _ in range(int(input())):
    n = int(input())
    a = [ele for ele in range(2, n + 1)]
    a.append(1)
    print(' '.join([str(e) for e in a]))