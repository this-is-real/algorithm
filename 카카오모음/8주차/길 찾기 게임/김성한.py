import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, head):
        self.head = head
        
    def insert(self, node):
        self.current_node = self.head
        while True:
            if node.x < self.current_node.x:
                if self.current_node.left is not None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = node
                    break
            else:
                if self.current_node.right is not None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = node
                    break

    def get_order_list(self, order_type):
        self.order_list = []
        self.order(self.head, order_type)
        return self.order_list
    
    def order(self, node, order_type):
        if order_type == "pre":
            self.order_list.append(node.value)
        if node.left is not None:
            self.order(node.left, order_type)
        if node.right is not None:
            self.order(node.right, order_type)
        if order_type == "post":
            self.order_list.append(node.value)
                    
def solution(nodeinfo):
    nodeinfo = [[idx+1, x, y] for idx, (x, y) in enumerate(nodeinfo)]
    nodeinfo = sorted(nodeinfo, key=lambda x: -x[2])
    
    head = Node(*nodeinfo.pop(0))
    binary_tree = BinaryTree(head)
    for node in nodeinfo:
        binary_tree.insert(Node(*node))
        
    answer = []
    for order_type in ["pre", "post"]:
        answer.append(binary_tree.get_order_list(order_type))
    return answer