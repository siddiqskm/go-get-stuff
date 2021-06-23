"""
Love Song -
https://codeforces.com/problemset/problem/1539/B
import string

n, t = map(int, input().split(' '))
s = input()
char_dict = dict(zip(string.ascii_lowercase, range(1,27)))
for _ in range(t):
    l, r = map(int, input().split(' '))
    val = 0
    for each_char in s[l-1:r]:
        val += char_dict.get(each_char)
    print(val)
"""
n,q=map(int, input().split())
s=input()
arr=[0]
for x in s:
    arr.append(arr[-1]+(ord(x)-ord('a')+1))
print("arr is: %s" % arr)
for x in range(q):
    a,b=map(int, input().split())
    print(arr[b]-arr[a-1])
