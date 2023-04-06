def insert(root, val):
    if not root:
        return TreeNode(val)
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

