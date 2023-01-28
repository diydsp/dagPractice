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
    
    def deserialize(self, json_str):
        data = json.loads(json_str)
        nodes_data = data["nodes"]
        edges_data = data["edges"]
        self.graph = {}
        nodes = {}
        for node_data in nodes_data:
            node = Node(node_data["x"], node_data["y"], node_data["val"])
            nodes[node_data["id"]] = node
            self.add_node(node)
        for edge_data in edges_data:
            self.add_edge(nodes[edge_data["source"]], nodes[edge_data["target"]])
