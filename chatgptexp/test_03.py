#!/usr/bin/python3

import importlib as il

import dag0 as dagNodeDef # dagNode definition
import dag1  # DAG class
#import dag2  as digviz # basic DAG Visualzer
#import dag4  as dagViz # 2nd DAG Visualzer
import dag5  as dagViz # 2nd DAG Visualzer


import pdb


dag = dag1.DAG()

a = dagNodeDef.dagNode('a',50,60)
b = dagNodeDef.dagNode('b',100,65)
dag.add_edge( a, b )

dagVis = dagViz.DAGVisualizer( dag, dagNodeDef )
dagVis.run()

def reload():
    il.reload( dagNodeDef )
    il.reload(dag1)
    il.reload(dag2)
    
    
