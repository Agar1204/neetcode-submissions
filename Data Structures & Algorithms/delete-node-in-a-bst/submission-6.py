# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr



    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        while True:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
                return root
            elif key > root.val:
                root.right = self.deleteNode(root.right, key)
                return root
            else:
                if not root.right:
                    return root.left
                elif not root.left:
                    return root.right
                else:
                    minNode = self.minNode(root.right)
                    temp = root.val
                    root.val = minNode.val
                    minNode.val = temp
                    root.right = self.deleteNode(root.right, key)
                    return root
        return root
        