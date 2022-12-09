
FILE_THRESHOLD = 100000

class node:
    def __init__(self, name, type=1, size=0, parent=None):
        self.name = name
        self.type = type
        self.size = size
        self.parent = parent
        self.dirs = list()
        self.files = list()

    def add_child(self, node):
        if node.type == 1:
            self.dirs.append(node)
        else:
            self.files.append(node)

    def calculate_size(self):
        size = 0
        for dire in self.dirs:
            dire.calculate_size()
            size += dire.size

        for file in self.files:
            size += file.size

        self.size = size

    def get_dir_by_name(self, name):
        for dire in self.dirs:
            if name == dire.name:
                return dire

def create_tree(lines):
    root = None
    ls = False
    current = None

    for line in lines:
        line = line.strip('\n')
        if ls  and '$' not in line:
            if 'dir' in line:
                new_node = node(name=line.split(' ')[1], type=1, parent=current)
                current.add_child(new_node)
            else:
                new_node = node(name=line.split(' ')[1], type=2, size=int(line.split(' ')[0]), parent=current)
                current.add_child(new_node)
        elif 'cd' in line:
            ls = False
            dir_name = line.split(' ')[2]
            if dir_name == '/':
                root = node(name=dir_name)
                current = root
            elif dir_name == '..':
                current = current.parent
            else:
                current = current.get_dir_by_name(dir_name)
        elif 'ls' in line:
            ls = True

    return root

def get_net_files_below_threshold(root):
    stack = list()
    stack.append(root)
    sum_size = 0
    while len(stack):
        current = stack.pop(0)
        if current.type == 1:
            stack.extend(current.dirs)
            stack.extend(current.files)
            if current.size <= FILE_THRESHOLD:
                sum_size += current.size

    return sum_size


if __name__ == "__main__":
    with open("input.txt", 'r') as fp:
        lines = fp.readlines()

    root = create_tree(lines)
    root.calculate_size()

    sum_size = get_net_files_below_threshold(root)
    print("Sum size {}".format(sum_size))

