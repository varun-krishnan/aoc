from prob1 import node, create_tree

NET_SIZE = 70000000
REQUIRED_SIZE = 30000000

def get_dir_to_delete(root):
    size_req = REQUIRED_SIZE-(NET_SIZE - root.size)
    node_to_remove = root
    stack = list()
    stack.append(root)
    while len(stack):
        current = stack.pop(0)
        if current.type == 1:
            stack.extend(current.dirs)
            stack.extend(current.files)
            if current.size >= size_req and current.size < node_to_remove.size:
                node_to_remove = current

    return node_to_remove

if __name__ == "__main__":
    with open("input.txt", 'r') as fp:
        lines = fp.readlines()

    root = create_tree(lines)
    root.calculate_size()

    node_to_remove = get_dir_to_delete(root)
    print("Node to remove is {} size is {}".format(node_to_remove.name, node_to_remove.size))