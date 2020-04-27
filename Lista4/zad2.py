# Author: Paweł Dychus
import random


# Iterative method of generating binary tree of height {height} using BFS 'like' approach
# In the first step add root and atleast 1 node
# For each added node add [0-2] new children nodes
# Continue through queue until height is reached => until queue is not empty
def generateTree(height):
    if height == 1:
        return ['1', None, None]

    nodes_to_gen = random.randint(1, 2)
    count = 1
    node = [f"{count}"]
    count += 1
    current_height = 1

    queue = []
    for i in range(1, nodes_to_gen+1):
        node.append([])
        queue.append((node[i], current_height, count),)
        count += 1

    if nodes_to_gen == 1:
        node.append(None)

    current_height = 2

    while len(queue) > 0:
        (item_node, item_height, item_count) = queue.pop(0)
        item_node.append(f"{item_count}")

        if item_height == current_height:  # We reached next level
            current_height += 1

        if current_height >= height:  # Too high
            item_node.append(None)
            item_node.append(None)
            continue

        # Higher chance for more nods in children
        nodes_to_gen = random.randint(0, 4)
        for i in range(1, nodes_to_gen+1):
            if i >= 3:
                break

            item_node.append([])
            queue.append((item_node[i], current_height, count))
            count += 1

        if nodes_to_gen == 1:  # Add Nones...
            item_node.append(None)

        if nodes_to_gen == 0:
            if len(queue) == 0:
                if item_height < height:  # Make sure we don't end too fast
                    item_node.pop()
                    queue.append((item_node, item_height, item_count))
                    continue

            item_node.append(None)
            item_node.append(None)

    return node


def DFS(tree, start=True):
    if tree == None:
        return

    if start:
        print("Printing Tree in DFS order:")

    yield tree[0]
    for i in DFS(tree[1], False):
        yield i

    for i in DFS(tree[2], False):
        yield i


def BFS(tree):
    if tree == None:
        return

    print("Printing Tree in BFS order:")
    queue = []
    print(tree[0])
    queue.append(tree[1])
    queue.append(tree[2])

    while len(queue) > 0:
        item = queue.pop(0)
        if item == None:
            continue
        yield item[0]
        queue.append(item[1])
        queue.append(item[2])


t = generateTree(3)
print(t)
for i in DFS(t):
    print(i)

for i in BFS(t):
    print(i)
