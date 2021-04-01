from collections import deque

class TreeNode:
    def __init__(self, value = None, depth = 1):
        self.value = value or 1
        self.left = None
        self.right = None
        self.has_not_children = True
        self.depth = depth

    def __str__(self):
        return str(self.value)

    def addChildren(self, left, right, node):
        queue = deque([node])
        while queue:
            node = queue.popleft()
            if node.has_not_children:
                depth = node.depth + 1
                node.left = TreeNode(value=left, depth=depth) if left != -1 else None
                node.right = TreeNode(value=right, depth=depth) if right != -1 else None
                node.has_not_children = False
                return
            else:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

    def get_all_nodes_in_order(self):
        output = []
        current = self
        stack = []
        
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                output.append(current.value)
                current = current.right
            else:
                break
        return output

    def swap(self, k):
        node = self
        queue = deque([node])
        while queue:
            node = queue.popleft()
            is_multiple = node.depth % k == 0
            if is_multiple:
                self.__handle_swap(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def __handle_swap(self, node):
        if node.left is not None or node.right is not None:
            aux = node.left
            node.left = node.right
            node.right = aux
        
def swapNodes(indexes, queries):
    root = TreeNode()
    output = []
    for left, right in indexes:
        root.addChildren(left, right, root)
    for query in queries:
        root.swap(query)
        swaped = root.get_all_nodes_in_order()
        output.append(swaped)
    return output
