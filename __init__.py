from vertice import vertice

class graph:
    def __init__( self ):
        self._vertices = dict()
        self._listVertices = list()

        self._edges = dict()
        self._listEdges = list()
    
    def add_vertice( self , ver:vertice ):
        if ver.name not in self._vertices.keys():
            # gerando o numero do no
            newNode = len( self._listVertices )
            ver.set_inode( newNode )

            # adicionando
            self._vertices[ ver.name ] = newNode 
            self._listVertices.append( ver )

        else:
            print("Tem que tratar")
            exit()
    
    def add_name_egde(self, name: str ,edg: edge ):
        inode = self._listVertices[ self._vertices[ name ] ]
        return self.add_inode_egde( inode , edge )

    def add_inode_egde(self, inode: int ,edg: edge ):
        ver = self._listVertices[ i ]
        return self.add_vertice_egde( ver , edge )        

    def add_vertice_egde(self, ver: vertice ,edg: edge ):
        cont = 0
        ver.edges.union( edge )

        in_inode = ver.inode
        if in_inode not in self._edges:
            self._edges[ in_inode ] = dict()
        for out_inode in edg:
            if out_inoe not in self._edges[ in_inode ]:
                newInode = len( self._listEdges )
                edge.set_inode( newInode )

                self._edges[ in_inode ][ out_inode ] = newInode
                self._listEdges.append( ver.edges )

                cont += 1

        return cont
        
    def __str__(self):
        print("vertices size:", len( self._listEdges)
        for node in self._vertices.keys()
            s = self._listVertices[ s ]
            print( f"[{s}]" , end = "" )
        print("")

    