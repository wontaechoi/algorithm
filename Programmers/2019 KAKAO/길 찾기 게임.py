import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, x=None, y=None, index=None):
        self.x = x
        self.y = y
        self.index = index


class Tree:
    def __init__(self, node, index):
        self.node = Node(node[0], node[1], index)
        self.left = None
        self.right = None

    def insert(self, new, index):
        new_x, new_y = new[0], new[1]
        current_tree = self
        while True:
            current = current_tree.node
            flag = False
            if current.x > new_x:
                if current_tree.left == None:
                    current_tree.left = Tree(new, index)
                    flag = True
                current_tree = current_tree.left
            else:
                if current_tree.right == None:
                    current_tree.right = Tree(new, index)
                    flag = True
                current_tree = current_tree.right
            if flag:
                break
            current = current_tree.node

    def postorder(self):
        if self.left == None and self.right == None:
            return [self.node.index]
        elif self.left == None:
            return [self.node.index] + self.right.postorder()
        elif self.right == None:
            return [self.node.index] + self.left.postorder()
        else:
            return [self.node.index] + self.left.postorder() + self.right.postorder()

    def preorder(self):
        if self.left == None and self.right == None:
            return [self.node.index]
        elif self.left == None:
            return self.right.preorder() + [self.node.index]
        elif self.right == None:
            return self.left.preorder() + [self.node.index]
        else:
            return self.left.preorder() + self.right.preorder() + [self.node.index]


def solution(nodeinfo):
    nodes = []
    for i in range(len(nodeinfo)):
        nodes.append((nodeinfo[i][0], nodeinfo[i][1], i + 1))
    nodes.sort(key=lambda x: [-x[1], x[0]])

    tree = Tree((nodes[0][0], nodes[0][1]), nodes[0][2])
    for i in range(1, len(nodeinfo)):
        tree.insert((nodes[i][0], nodes[i][1]), nodes[i][2])

    answer = [tree.postorder(), tree.preorder()]
    return answer