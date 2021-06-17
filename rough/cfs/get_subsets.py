"""
Given an integer array nums of unique elements,
return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order.
"""
def subsets(nums):
    def backtrack(first = 0, curr = []):
        print("Input attributes are: k - %s, first - %s and curr - %s"
              % (k, first, curr))
        # if the combination is done
        if len(curr) == k:
            # Uncomment the below line to remove duplicates
            # if curr not in output: output.append(curr[:])
            output.append(curr[:])
            return

        for i in range(first, n):
            # add nums[i] into the current combination
            curr.append(nums[i])
            # use next integers to complete the combination
            backtrack(i + 1, curr)
            # backtrack
            curr.pop()
    
    output = []
    # Uncomment the below line to remove duplicates
    # nums.sort()
    n = len(nums)
    for k in range(n + 1):
        print("k value is: %s" % k)
        backtrack()
    return output


arr = [1, 2, 2]
print("Subsets are: %s" % subsets(arr))