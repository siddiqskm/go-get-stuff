"""
LC -
108. Convert Sorted Array to Binary Search Tree
109. Convert Sorted List to Binary Search Tree
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convert_list_to_tree(arr):
    if not arr:
        return None

    mid = len(arr) // 2

    print("The root element is: %s" % arr[mid])
    root = TreeNode(arr[mid])

    # Left Subtree of root has all values < arr[mid]
    root.left = convert_list_to_tree(arr[:mid])

    # Right Subtree of root has all values > arr[mid]
    root.right = convert_list_to_tree(arr[mid+1:])
    
    # Return the root Element
    return root   


# A utility function to print the inorder 
# traversal of the BST
def in_order(node):
    if not node:
        return
      
    pre_order(node.left)
    print(node.val)
    pre_order(node.right) 


# A utility function to print the preorder 
# traversal of the BST
def pre_order(node):
    if not node:
        return
      
    print(node.val)
    pre_order(node.left)
    pre_order(node.right) 


# A utility function to print the postorder 
# traversal of the BST
def post_order(node):
    if not node:
        return
      
    pre_order(node.left)
    pre_order(node.right)
    print(node.val)


sample_list = [2, 4, 67, 9, 12, 56, 78, 90]

# Convert a list to binary tree to start with
sample_list.sort()
print("sample list is: %s" % sample_list)
root = convert_list_to_tree(sample_list)
print("In Order LNR -")
in_order(root)
print("Pre Order NLR -")
pre_order(root)
print("Post Order LRN -")
post_order(root)

