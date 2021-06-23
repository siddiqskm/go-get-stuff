"""
Kefa and First Steps -
https://codeforces.com/problemset/problem/580/A
"""
n = int(input())
arr = [int(ele) for ele in input().split()]
dp_arr = [1] * n
index = 1
while index < n:
    if arr[index] >= arr[index - 1]:
        dp_arr[index] = dp_arr[index - 1] + 1
    
    index += 1

print(max(dp_arr))