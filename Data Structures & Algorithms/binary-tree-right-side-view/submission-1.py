# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = []
        queue = deque()
        queue.append(root)
        while queue:
            currLevel = []
            lenQueue = len(queue)
            for _ in range(lenQueue):
                node = queue.popleft()
                currLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(currLevel[-1])
        return output

        