def validate_bst(root, low=float('-inf'), high=float('inf')):
    if not root: 
        return True
    elif not low < root.val < high:
        return False
    return (self.isValidBST(root.left, low, root.val) and self.isValidBST(root.right, root.val, high))