"""
Given an array find out if a pair exists that match target 
"""
def get_pair(arr, target):
    arr_dict = {}
    for index, each_ele in enumerate(arr):
        print("Array Dict is: %s" % arr_dict)
        if target-each_ele in arr_dict:
            return arr_dict[target-each_ele], index
        else:
            arr_dict[each_ele] = index


def find_element(arr, element):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        print("Mid element is: ", arr[mid])
        if arr[mid] == element:
            return mid
        elif element > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1

arr = [5, 6, 8, 9, 13, 17, 19, 20]
print("The pair returned is: ", get_pair(arr, 15))
print("Element found @ index: ", find_element(arr, 6))