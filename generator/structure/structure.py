from anytree import Node, RenderTree


def create_tree(depth=2, width=2, parent=None):
    if depth < 1:
        return parent

    if parent is not None:
        n = Node("{}_{}".format(depth, width), parent)
    else:
        n = Node("{}_{}".format(depth, width))

    for w in range(width):
        create_tree(depth - 1, width, n)
    return n


def print_tree(root):
    for pre, fill, node in RenderTree(root):
        if hasattr(node, "label"):
            label = node.label
        else:
            label = ""
        print("%s%s[%s]" % (pre, node.name, label))


def path_to_root(node, suffix=""):
    if node.parent is None:
        return suffix
    return path_to_root(node.parent, node.label + "/" + suffix)
