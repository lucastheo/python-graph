class edge:
    def __init__( self , inode_in:int , inode_out:int , args = None ):
        self.args = args
        self.inode_in = inode_in
        self.inode_out = inode_out 

    def __str__( self ):
        s = f"[{self.inode_out},{str(self.args)[:10]}]"
        return s

class edges:
    def __init__( self ):
        self.inodes = set()
        self.edges = set()
    def add( self , edg: edge ):
        self.inodes.add( edg.inode_out )
        self.edges.add( edg )

    def __str__( self ):    
        s = ""
        for edge in self.edges:
            s += str( edge )
        return s
