def get_subarrays(s, index, ret_list):
    print("Function called with: %s and %s" % (s, ret_list))
    if not s:
        return
    else:
        ret_list.append(s)

    return get_subarrays(s[:index], index-1, ret_list)


n = int(input())
arr = [int(each_ele) for each_ele in input().split()]
print("The subarrays are: %s" % get_subarrays(arr, n-1, []))