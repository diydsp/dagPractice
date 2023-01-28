dag = DAG()
json_str = '{"nodes": [{"id": 140729206835248, "val": 3, "x": 1, "y": 2}, {"id": 140729206835296, "val": 4, "x": 2, "y": 3}], "edges": [{"source": 140729206835248, "target": 140729206835296}]}'
dag.deserialize(json_str)
print(dag.graph)
