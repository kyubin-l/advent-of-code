from utils.base_solution import BaseSolution

Q_NUM = 7
YEAR = 2022


class Node:
    nodes = []
    def __init__(self, name: str, parent, filesize: int = 0) -> None:
        self.name = name
        self.children = []
        self.parent = parent
        self.filesize = filesize        # 0 if it's a directory, otherwise the filesize
        Node.nodes.append(self)

    def add_children(self, obj):
        self.children.append(obj)

    def navigate(self, node_name):
        if node_name == '..':
            return self.parent
        for child in self.children:
            if child.name == node_name:
                return child
        
    @property
    def size(self):
        if self.filesize:
            return self.filesize
        return sum(child.size for child in self.children)

    def __repr__(self) -> str:
        return f'{self.name}'


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        self.root = Node('/', parent=None)
        cur = self.root
        with open(self.filename) as f:
            f.readline()
            for line in f.readlines():
                line = line.rstrip()
                if line.startswith('$ ls'):
                    continue
                if line.startswith('$ cd'):
                    file = line.split()[-1]
                    cur = cur.navigate(file)
                else:
                    """
                    Either
                        - dir 'dirname' or
                        - filesize 'filename'
                    """
                    arg, file = line.split()
                    if file in [child.name for child in cur.children]:
                        continue
                    size = 0 if arg == 'dir' else int(arg)
                    new_node = Node(file, cur, size)
                    cur.add_children(new_node)

    def solve_part_one(self):
        total = 0
        for node in Node.nodes:
            if node.size <= 100000 and node.filesize == 0:
                total += node.size
        return total

    def solve_part_two(self):
        smallest = float('inf')
        required = 3e7 - (7e7 - self.root.size)
        for node in Node.nodes:
            if node.size < smallest and node.size > required:
                smallest = node.size
        return smallest
    

if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())