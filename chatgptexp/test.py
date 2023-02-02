#!/usr/bin/python3

import importlib as il

import dag0
import dag1
import dag2

import pdb


dag = dag1.DAG()

a = dag0.dagNode('a',50,60)
b = dag0.dagNode('b',100,65)
dag.add_edge( a, b )

dagVis = dag2.DAGVisualizer( dag )
dagVis.run()

def reload():
    il.reload(dag0)
    il.reload(dag1)
    il.reload(dag2)
    
    
