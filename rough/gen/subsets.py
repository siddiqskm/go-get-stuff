"""
Subsets
https://leetcode.com/problems/subsets/
"""
def subsets(nums):
    """
    Base Condition ->
        i == n
    Attributes ->
        nums
        i
        n
        curr_list
    """
    def generate_subsets(start=0, curr=[]):
        print("Input arguments: %s, %s and %s" % (nums, start, curr))
        if len(curr) == k:
            output_list.append(curr[:])
            return

        for i in range(start, n):
            curr.append(nums[i])
            generate_subsets(i+1, curr)
            curr.pop()


    output_list = []
    n = len(nums)
    for k in range(n + 1):
        generate_subsets()
    print("Output list is: %s" % output_list)


subsets([1, 2, 3])