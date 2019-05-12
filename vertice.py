class vertice:
    def __init__(self, name, args = None , inode = -1):
        self.name = name
        self.args = args
        self.inode = inode
        self.edges = edge()

    def set_inode(self, num ):
        self.inode = num