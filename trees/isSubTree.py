"""
Sep 1, 2023

Time complexity: O(n) where n is number of nodes in tree because worst case traverse all nodes in an unbalanced tree. 
Space complexity: O(h) where h is height of tree because stack would store height of tree. 

Explanation: 
    1. Depth First Search
    2. Use isSameTree() function 
    3. Returning values in recursion 
"""

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:\

        def isSameTree(p, q):
            if not p and not q:
                return True 
            elif not p or not q:
                return False 
            elif p.val != q.val:
                return False
            else:
                return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right)) 
        
        if not subRoot:
            return True
        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))



