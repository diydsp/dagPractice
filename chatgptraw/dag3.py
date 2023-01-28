dag = DAG()
dag.add_edge(node1, node2)
dag.add_edge(node2, node3)
...
vis = DAGVisualizer(dag)
vis.run()

