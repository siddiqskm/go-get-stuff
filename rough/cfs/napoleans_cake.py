"""
Napoleon Cake -
https://codeforces.com/problemset/problem/1501/B
"""
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))
    print("a is: %s" % a)
    index = n - 1
    while index >= 0:
        print("my index and element is: %s, %s" % (index, a[index]))
        if a[index] > 1:
            a[index - 1] = a[index] - 1
            a[index] = 1
        
        print("array is: %s" % a)

        index -= 1

    print(' '.join([str(ele) for ele in a]))
