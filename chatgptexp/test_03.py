#!/usr/bin/python3

import importlib as il

import dag0  # dagNode definition
import dag1  # DAG class
#import dag2  as digviz # basic DAG Visualzer
#import dag4  as dagViz # 2nd DAG Visualzer
import dag5  as dagViz # 2nd DAG Visualzer


import pdb


dag = dag1.DAG()

a = dag0.dagNode('a',50,60)
b = dag0.dagNode('b',100,65)
dag.add_edge( a, b )

dagVis = dagViz.DAGVisualizer( dag )
dagVis.run()

def reload():
    il.reload(dag0)
    il.reload(dag1)
    il.reload(dag2)
    
    
