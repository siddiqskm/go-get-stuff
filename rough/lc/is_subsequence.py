"""
Is Subsequence -
https://leetcode.com/problems/is-subsequence/
"""
def lcs(s, t, m, n):
    if m == 0 or n == 0:
        return 0

    if s[m-1] == t[n-1]:
        return 1 + lcs(s, t, m-1, n-1)
    else:
        return max(lcs(s, t, m, n-1), lcs(s, t, m-1, n))


s = 'abc'
t = 'ahbgdc'
m = len(s)
n = len(t)
dp = [[-1
       for i in range(n + 1)]
       for j in range(m + 1)]

print("DP array is: %s" % dp)

if lcs(s, t, m, n) == len(s):
    print("Yup subsequence !!!")
else:
    print("Not a subsequence !!!")