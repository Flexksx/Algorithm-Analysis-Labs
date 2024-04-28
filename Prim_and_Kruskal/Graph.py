class Graph:
    def __init__(self, vertices:list=None) -> None:
        self.vertices = vertices
        self.graph = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]
        
    def __repr__(self) -> str:
        return str(self.graph)
    
    