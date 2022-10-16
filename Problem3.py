from collections import deque

class Problem3(object):

    def leveltra(root):
        if not root:
            return []
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            currentLevel = []
            for i in range(len(queue)):
                node = queue.popleft()
                currentLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(currentLevel)

        return result