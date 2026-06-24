# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count =1
               
        def helper(root: TreeNode, max):
            nonlocal count
            if root is None:
                return None
            
            if root.val>=max:
                count +=1
                max = root.val

            helper(root.left, max)
            helper(root.right, max)
        helper(root.left, root.val)
        helper(root.right, root.val)
        return count

        