"""
The Way to Home -
https://codeforces.com/problemset/problem/910/A
"""
n,d=[int(ele) for ele in input().split(' ')]
arr = [int(ele) for ele in list(input())]
jump_count = 1
index = d
while index < len(arr) - 1:
    if arr[index] == 0:
        index -= 1
    else:
        print("Jumping the gun with index: %s !!!" % index)
        jump_count += 1
        index = index + d

    if index <= 0:
        break

if index <= 0:
    print(-1)
else:
    print(jump_count)