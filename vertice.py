from .edge import edges
class vertice:
    def __init__(self, name, args = None , inode = -1):
        self.name = name
        self.args = args
        self.inode = inode
        self.edges = edges()

    def set_inode(self, num ):
        self.inode = num


    def __str__( self ):
        s = f"{self.name[:30]}:"
        s += str( self.edges )
        return s