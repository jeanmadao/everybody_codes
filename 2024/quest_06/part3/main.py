FILENAME = "everybody_codes_e2024_q06_p3.txt"

class Node:
    def __init__(self, char, parent=None):
        self.char = char
        self.parent = parent
        self.children = []
        self.layer = None

    def __str__(self):
        return self.char

nodes = {}

def fifo(root):
    queue = [(root, root.char[0])]
    root.layer = 0

    curr_layer = 0
    contendant_layer = None
    unique_layer = True
    while queue:
        curr, path = queue.pop(0)
        curr_layer = curr.layer
        if contendant_layer and contendant_layer[0] != curr_layer:
            if unique_layer:
                return contendant_layer
            else:
                unique_layer = True
                contendant_layer = None
        for child in curr.children:
            if child == '@':
                if contendant_layer == None:
                    contendant_layer = (curr_layer, path + '@')
                else:
                    unique_layer = False
            else:
                child.layer = curr_layer + 1
                queue.append((child, path + child.char[0]))

with open(FILENAME) as f:
    line = f.readline().strip()
    while line:
        curr, children = line.split(':')
        curr_node = nodes.get(curr)
        if not curr_node:
            curr_node = Node(curr)
            nodes[curr] = curr_node
        children = children.split(',')
        for child in children:
            if child != '@':
                child_node = nodes.get(child)
                if not child_node:
                    child_node = Node(child)
                    nodes[child] = child_node
                curr_node.children.append(child_node)
                child_node.parent = curr_node
            else:
                curr_node.children.append('@')
        line = f.readline().strip()


print(fifo(nodes['RR']))
