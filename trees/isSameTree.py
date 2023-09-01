"""
Aug 31, 2023

Time complexity: O(n), where n is number of nodes in tree because we have to go through each node
Space complexity: O(h), with h is height of tree because stack stores height of tree

Explanation: 
    1. Depth First Search 
    2. Binary Tree is made up of Binary Trees
    3. Recursive pattern is to check values and if node is null or not
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False 
        elif p.val != q.val:
            return False
        else:
            return (self.isSameTree(p.left, q.left) and 
                    self.isSameTree(p.right, q.right))

        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right)
        """
