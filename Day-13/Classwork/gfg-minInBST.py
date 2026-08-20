"""
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""


            
class Solution:
    def minValue(self, root):
        if not root:
            return -1
        while root.left:
            root = root.left
        return root.data
