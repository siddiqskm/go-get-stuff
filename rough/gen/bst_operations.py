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

    print("The input list is: %s" % arr)

    mid = len(arr) // 2

    print("The root element is: %s" % arr[mid])
    root = TreeNode(arr[mid])

    # Left Subtree of root has all values < arr[mid]
    root.left = convert_list_to_tree(arr[:mid])

    # Right Subtree of root has all values > arr[mid]
    root.right = convert_list_to_tree(arr[mid+1:])
    
    # Return the root Element
    return root   


# A utility function to print the preorder 
# traversal of the BST
def pre_order(root):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right) 


# A utility function to print the postorder 
# traversal of the BST
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)


# A utility function to print the inorder 
# traversal of the BST
def in_order(root):
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)


def insert_node(root, key):
    if not root:
        return TreeNode(key)

    if key == root.val:
        return root
    elif key > root.val:
        root.right = insert_node(root.right, key)
    else:
        root.left = insert_node(root.left, key)
    
    return root


sample_list = [2, 4, 67, 9, 12, 56, 78, 90]

# Convert a list to binary tree to start with
sample_list.sort()
print("sample list is: %s" % sample_list)
root = convert_list_to_tree(sample_list)
print("Pre Order NLR -")
pre_order(root)
print("Post Order LRN -")
post_order(root)
print("In Order LNR -")
in_order(root)
print("Insertion starts now !!!")
root = insert_node(root, 30)
root = insert_node(root, 1000)
root = insert_node(root, -1000)
root = insert_node(root, 20)
root = insert_node(root, 210)
root = insert_node(root, 310)
root = insert_node(root, 310)
print("In Order LNR -")
in_order(root)