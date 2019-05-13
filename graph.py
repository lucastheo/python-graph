from .edge import edge

class graph:
    def __init__( self ):
        self._vertices = dict()
        self._listVertices = list()

        self._edges = dict()
        self._listEdges = list()
    
    def add_vertice( self , name, args = None ):
        if name not in self._vertices.keys():
            # gerando o numero do no

            newInode = len( self._listVertices )
            newVertice = vertice( name , args, newInode )
            newVertice.set_inode( newNode )

            # adicionando
            self._vertices[ name ] = newInode 
            self._listVertices.append( newVertice )
            return newVertice
        else:
            print("Tem que tratar")
            return None

    def add_vertice( self , ver ):
        if ver.name not in self._vertices.keys():
            # gerando o numero do no
            newNode = len( self._listVertices )
            ver.set_inode( newNode )

            # adicionando
            self._vertices[ ver.name ] = newNode 
            self._listVertices.append( ver )
            return ver
        else:
            print("Tem que tratar")
            return None
    
    def add_name_egde(self, name: str ,name1: str , args = None):
        inode = self._vertices[ name ]
        inode1 = self._vertices[ name1 ]

        return self.add_inode_egde( inode , inode1, args )

    def add_inode_egde(self, inode: int , inode1: int, args = None ):
        ver = self._listVertices[ inode ]
        ver1 = self._listVertices[ inode1 ]
        return self.add_vertice_egde( ver , ver1, args )        

    def add_vertice_egde(self, ver ,ver1, args = None ):
        newInode = len( self._listEdges ) 
        
        in_inode = ver.inode
        out_inode = ver1.inode 

        newEdge = edge( in_inode, out_inode, args )

        if in_inode not in self._edges:
            self._edges[ in_inode ] = dict()
        
        if out_inode not in self._edges[ in_inode ]:
            ver.edges.add( newEdge )

            self._edges[ in_inode ][ out_inode ] = newInode
            self._listEdges.append( newEdge )

        return newEdge

    def get_name_vertice( self , name ):
        inode = self._listVertices[ self._vertices[ name ] ]
        return self.get_inode_vertice( inode )

    def get_inode_vertice( self, inode ):
        ver = self._listVertices[ inode ]    
        return ver

    def get_inode_edge( self , inode : int):
        edge = self._listEdges[ inode ]
        return edge
    
    def get_vertice_edge( self, ver , ver1 ):
        edge = self._edges[ ver.inode ][ ver1.inode ]
        return edge
    
    def get_inode_edge( self, inode: int , inode1:int ):
        edge = self._edges[ inode ][ inode1 ]
        return edge

    def get_name_edge( self , name:str, name1:str ):
        inode = self._vertices[ name ]
        inode1 = self._vertices[ name1 ]
        return self.get_inode_edge( inode , inode1 )

    def in_name_graph_vertice( self , name:str ):
        if name in self._vertices.keys():
            return True
        else:
            return False
    def in_inode_graph_vertice( self , inode:int ):
        if inode < len( self._listVertices ):
            return True
        else:
            return False

    def __str__(self):
        s =  f"vertices size: {len( self._listVertices)}\n"
        s += f"egds size: {len( self._listEdges)}\n"
        for inode in range(len( self._listVertices)):
            s += f"inode: {inode}->"
            s += f"{self._listVertices[ inode ]}\n" 
        return s

    