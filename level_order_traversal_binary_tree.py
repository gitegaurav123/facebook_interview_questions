# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        level_order = []
        frontier = [root]
        frontier_value = [root.val]
        while frontier:
            level_order.append(frontier_value)
            next = []
            next_frontier_value = []
            # print frontier
            for element in frontier:
                for next_node in [element.left, element.right]:
                    if next_node != None:
                        next.append(next_node)
                        next_frontier_value.append(next_node.val)
            
            frontier = next
            frontier_value = next_frontier_value
        return level_order