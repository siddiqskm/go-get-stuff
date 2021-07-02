"""
Subset Sum Problem -
https://leetcode.com/problems/partition-equal-subset-sum/
https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

def is_subset_sum(arr, n, sum):
    if sum == 0:
        return True

    if n == 0:
        return False

    if arr[n-1] > sum:
        return is_subset_sum(arr, n-1, sum)
    
    return is_subset_sum(arr, n-1, sum) or \
        is_subset_sum(arr, n-1, sum-arr[n-1])

print("The output is: %s" % is_subset_sum([3, 34, 4, 12, 5, 2], 6, 9))

Partition Sum -
        def can_partition(nums, n, input_sum):
            if n == 0 and input_sum != 0:
                return False
            
            if input_sum == 0:
                return True
            
            if nums[n-1] > input_sum:
                return can_partition(nums, n-1, input_sum)
            
            return can_partition(nums, n-1, input_sum) or can_partition(nums, n-1, input_sum-nums[n-1])
        
        num_sum = sum(nums)
        if num_sum % 2 != 0:
            return False
        
        return can_partition(nums, len(nums), num_sum // 2)

DP Solution
arr, n, sum
"""
def is_subset_sum(arr, n, sum):
    table = [[False
              for x in range(sum+1)]
              for y in range(n+1)]

    # If sum is 0, then answer is true
    for i in range(n + 1):
        table[i][0] = True
         
    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, sum + 1):
         table[0][i]= False

    print("The DP table is: %s" % table)

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if j < arr[i-1]:
                table[i][j] = table[i-1][j]
            
            if j >= arr[i-1]:
                table[i][j] = (
                    table[i-1][j] or
                    table[i-1][j-arr[i-1]]
                )

    print("Final DP table is: %s" % table)
    return table[n][sum]

print("Subset sum status is: %s" % is_subset_sum([3, 34, 4, 12, 5, 2], 6, 13))
