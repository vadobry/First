class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode):
        if root is None:
            return
        queue = []
        averages = []
        counts = 0
        summa = 0
        queue.append(root)
        queue.append(None)
        while len(queue) > 0:
            node = queue.pop(0)
            if node is None:
                averages.append(summa / counts)
                summa = 0
                counts = 0
                queue.append(None)

                if queue[0] is None:
                    break
                else:
                    continue

            summa += node.val
            counts += 1
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return averages

