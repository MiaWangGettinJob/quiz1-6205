class Problem2:

    def ifsame(root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2 or root1.val != root2.val:
            return False
        else:
            return ifsame(root1.left, root2.left) and ifsame(root1.right, root2.right)

