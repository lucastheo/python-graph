class edges:
    def __init__( self ):
        self.inodes = set()
        self.edges = set()
    def add( self , edg: edge ):
        self.inodes.add( edg.inode )
        self.edges.add( edg )

    
class edge:
    def __init__( self , args = None, inode = -1 ):
        self.args = args
        self.inode = inode
    def set_inode( self , inode ):
        self.inode = inode 