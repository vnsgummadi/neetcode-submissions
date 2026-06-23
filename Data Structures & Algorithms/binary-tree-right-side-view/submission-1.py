# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            size = len(queue)
            last = []
            for i in range(size):
                node = queue.popleft()
                last.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                

            res.append(last[len(last)-1])
        return res

        


        