import json

class DAG:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        self.graph[node] = set()

    def add_edge(self, node1, node2):
        self.graph[node1].add(node2)

    def remove_node(self, node):
        for n in self.graph:
            if node in self.graph[n]:
                self.graph[n].remove(node)
        del self.graph[node]

    def serialize(self):
        nodes = []
        edges = []
        for node in self.graph:
            nodes.append({"id": id(node), "val": node.val, "x": node.x, "y": node.y})
            for neighbor in self.graph[node]:
                edges.append({"source": id(node), "target": id(neighbor)})
        return json.dumps({"nodes": nodes, "edges": edges})

