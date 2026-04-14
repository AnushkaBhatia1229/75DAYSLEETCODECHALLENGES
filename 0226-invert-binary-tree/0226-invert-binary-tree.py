# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        st = [root]

        while len(st) > 0:
            node = st.pop()

            if node is None:
                continue

            # swap left and right
            hold = node.left
            node.left = node.right
            node.right = hold

            st.append(node.left)
            st.append(node.right)

        return root