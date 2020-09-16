import sys
import os
sys.path.append("..")
from TreeNode import TreeNode

def is_balanced(tree):
    def get_height_if_balanced(tree):
        if not tree:
            return 0
        left = get_height_if_balanced(tree.left)
        right = get_height_if_balanced(tree.right)

        if left == -1 or right == -1:
            return -1
        
        height = -1
        if abs(left-right) <= 1:
            height = 1 + max(left, right)

        return height
    
    return get_height_if_balanced(tree) != -1
