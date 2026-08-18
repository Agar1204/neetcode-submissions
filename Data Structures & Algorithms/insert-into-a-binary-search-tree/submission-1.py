# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        current = root
        prev = None
        while current != None:
            prev = current
            if current.val < val:
                current = current.right
            elif current.val > val:
                current = current.left
        if val > prev.val:
            prev.right = TreeNode(val)
        elif val < prev.val:
            prev.left = TreeNode(val)
        return root
            
        