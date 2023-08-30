"""
Aug 30, 2023

Time complexity: O(n), where n is number of nodes in tree because we have to go through each node
Space complexity: O(h), with h is height of tree because stack stores height of tree

Explanation: 
    1. Depth First Search 
    2. Binary Tree is made up of Binary Trees
    3. Recursive pattern is to swap leaves of root
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if not root: 
            return None

        # Pythonic method to swap two variables  
        root.left, root.right = root.right, root.left

        # Recursive call
        self.invertTree(root.left)
        self.invertTree(root.right)

