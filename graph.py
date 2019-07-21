from .edge import edge
from .vertice import vertice
from .utils.GDF_Formatter import gdf_formatter
from graphviz import Digraph as graphviz_Digraph

class graph:
    def __init__( self ):
        self._vertices = dict()
        self._listVertices = list()

        self._edges = dict()
        self._listEdges = list()
    
    def size_vertices(self):
        return len( self._listVertices )

    def size_edges(self):
        return len( self._listEdges )
    def add_vertice( self , name, args = None ):
        if name not in self._vertices.keys():
            # gerando o numero do no

            newInode = len( self._listVertices )
            newVertice = vertice( name , args, newInode )
            #newVertice.set_inode( newVertice )

            # adicionando
            self._vertices[ name ] = newInode 
            self._listVertices.append( newVertice )
            return newVertice
        else:
            print("Tem que tratar: add_vertice" , name , args )
            return None

    def add_vertice_by_vertice( self , ver ):
        if ver.name not in self._vertices.keys():
            # gerando o numero do no
            newNode = len( self._listVertices )
            ver.set_inode( newNode )

            # adicionando
            self._vertices[ ver.name ] = newNode 
            self._listVertices.append( ver )
            return ver
        else:
            print("Tem que tratar: add_vertice_by_vertice")
            return None
    
    def add_name_egde(self, name: str ,name1: str , args = None):
        if name == None or name1 == None:
            return None
        
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

    def get_name_vertice( self , name:str ):
        inode = self._vertices[ name ]
        return self.get_inode_vertice( inode )

    def get_inode_vertice( self, inode:int ):
        ver = self._listVertices[ inode ]    
        return ver

    def get_inode_edge( self , inode : int):
        edge = self._listEdges[ inode ]
        return edge
    
    def get_vertice_edge( self, ver , ver1 ):
        edge = self._edges[ ver.inode ][ ver1.inode ]
        return edge
    
    def get_inode_ver_edge( self, inode: int , inode1:int ):
        edge = self._edges[ inode ][ inode1 ]
        return edge

    def get_name_edge( self , name:str, name1:str ):
        inode = self._vertices[ name ]
        inode1 = self._vertices[ name1 ]
        return self.get_inode_ver_edge( inode , inode1 )

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

    
    def saida_graph_viz_text( self, caminho = None):
        s = "digraph{\n"
        for edge in self._listEdges:
            inVer = self._listVertices[ edge.inode_in ]
            outVer = self._listVertices[ edge.inode_out ]

            s += f'"{inVer.name}" -> "{outVer.name}" [label="{edge.args}"];\n'
        s += "}"
        if caminho == None:
            return s
        
        arq = open( caminho , "w" )
        arq.write( s )
        arq.close()
    def funcAllTrue( self , args ):
        return True
    def saida_graph_viz( self, filename, name = 'graph', engine = 'dot',  funcLabel = None,funcNode = None, maximoNode = 200 ):

        g = graphviz_Digraph(name, filename = filename, engine = engine, format="svg" )
        
        cont = 0
        verticeSelect = set()

        if funcNode == None:
            funcNode = self.funcAllTrue
        if funcLabel == None:
            funcLabel = self.funcAllTrue

        for vertice in self._listVertices:
            flag = False
            for edge in vertice.edges.edges:
                if funcNode( edge ) == True:
                    flag = True
                    break

            if flag == True:
                g.node(vertice.name)
                verticeSelect.add( vertice.name)
                if cont == maximoNode:
                    break
                else:
                    cont += 1

        for vertice in self._listVertices:
            for edge in vertice.edges.edges:
                if funcNode( edge ) == True:
                    vertice1 =  self._listVertices[ edge.inode_out ]
                    #if vertice.name in verticeSelect or vertice1.name in verticeSelect :
                    g.edge( vertice.name , vertice1.name )

        g.render(filename=filename )
        

    
    def saida_graph_gdf( self, caminho, argsExiste = False, tipoDados:str = None ):

        s = ""
        if argsExiste == True:
            if tipoDados == None:
                s += "nodedef>name VARCHAR,label VARCHAR,args VARCHAR\n"
                for vertice in self._listVertices:
                    s += f"{vertice.inode},{vertice.name},{vertice.args}\n"
            else:
                s += f"nodedef>name VARCHAR,label VARCHAR, {tipoDados}\n"
                for vertice in self._listVertices:
                    s += f"{vertice.inode},{vertice.name}"
                    for args in vertice.args:
                        s += f",{args}"
                    s += "\n"
        else:
            s += "nodedef>name VARCHAR,label VARCHAR\n"
            for vertice in self._listVertices:
                s += f"{vertice.inode},{vertice.name}\n"

                        
        s += "edgedef>node1 VARCHAR, node2 VARCHAR\n"
        for vertice in self._listVertices:
            for edge in vertice.edges.edges:
                s += f"{vertice.inode},{edge.inode_out}\n"
        
        arq = open(caminho, "w")
        arq.write( s )
        arq.close()
