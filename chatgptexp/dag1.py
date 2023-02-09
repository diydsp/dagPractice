import pdb
import json

class DAG:
    def __init__(self):
        self.graph = {}

    def add_node( self, node, x, y ):
        if node not in self.graph:
            node.x = x
            node.y = y
            self.graph[ node ] = []
        
    def add_edge(self, node1, node2):
        #pdb.set_trace()
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        self.graph[node1].append(node2)

    def remove_node(self, node):
        for n in self.graph:
            if node in self.graph[n]:
                self.graph[n].remove(node)
        del self.graph[node]
        
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
            node = self.add_node( node_data["val"], node_data["x"], node_data["y"] )
            #node = Node(node_data["x"], node_data["y"], node_data["val"])
            nodes[node_data["id"]] = node
            self.add_node(node)
        for edge_data in edges_data:
            self.add_edge(nodes[edge_data["source"]], nodes[edge_data["target"]])

