"""
Aug 31, 2023

Time complexity: O(n) where n is number of nodes in tree because worst case traverse all nodes in an unbalanced tree. 
Space complexity: O(h) where h is height of tree because stack would store height of tree. 

Explanation: 
    1. Depth First Search
    2. Binary Tree is made up of Binary Trees
    3. Keep count of left and right depth
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case 
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left) + 1
        right_depth = self.maxDepth(root.right) + 1
        
        return max(left_depth, right_depth)
