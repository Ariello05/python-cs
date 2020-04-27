# Author: Paweł Dychus
import random


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.height = 1

    def add_child(self, value=None):
        node = Node(value)
        node.height = self.height + 1
        self.children.append(node)

    def get_last_added(self):
        return self.children[-1]


# Iterative method of generating n-ary tree of height {height} using all nodes approach
def generateTree(height):

    tree = Node(1)

    if height == 1:
        return tree

    free_nodes = [tree]
    while True:
        # Every node has an equal chance to get a new child
        index = random.randint(0, len(free_nodes)-1)
        selected = free_nodes[index]

        if selected.height >= height:
            break
        selected.add_child()
        free_nodes.append(selected.get_last_added())

    # Giving correct BFS numeration for nodes
    queue = []
    for el in tree.children:
        queue.append(el)
    count = 2
    while len(queue) > 0:
        item = queue.pop(0)
        if item == None:
            continue
        item.value = f"{count}"
        count += 1
        for el in item.children:
            queue.append(el)

    return tree


def DFS(tree, start=True):
    if tree == None:
        return

    if start:
        print("Printing Tree in DFS order:")

    yield tree.value
    for el in tree.children:
        for i in DFS(el, False):
            yield i


def BFS(tree):
    if tree == None:
        return

    print("Printing Tree in BFS order:")
    queue = [tree]
    while len(queue) > 0:
        item = queue.pop(0)
        if item == None:
            continue
        yield item.value
        for el in item.children:
            queue.append(el)


t = generateTree(3)
for i in DFS(t):
    print(i)

for i in BFS(t):
    print(i)
