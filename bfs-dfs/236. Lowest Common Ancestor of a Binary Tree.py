# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        queue = [root]
        
        parent = {root: None}
        
        while q not in parent or p not in parent:
            
            node = queue.pop(0)
            
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            ancestors.add(q)
            q = parent[q]
            
        return q
        
