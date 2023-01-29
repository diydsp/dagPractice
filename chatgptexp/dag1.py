class DAG:
    def __init__(self):
        self.graph = {}

    def add_node( self, node, x, y ):
        if node not in self.graph:
            node.x = x
            node.y = y
            self.graph[ node ] = []
        
    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        self.graph[node1].append(node2)

    def topological_sort(self):
        in_degree = {}
        for node in self.graph:
            in_degree[node] = 0

        for node in self.graph:
            for neighbour in self.graph[node]:
                in_degree[neighbour] += 1

        queue = []
        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)

        top_sort = []
        while queue:
            node = queue.pop(0)
            top_sort.append(node)

            for neighbour in self.graph[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        return top_sort

