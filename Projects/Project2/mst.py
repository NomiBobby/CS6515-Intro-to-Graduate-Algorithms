# -*- coding: utf-8 -*-
"""
    mst.py       Intro to Graduate Algorithms, Spring 2023
    
    You will implement Kruskal's algorithm for finding a Minimum Spanning Tree.
    You will also implement the union-find data structure using path compression
    See [DPV] Sections 5.1.3 & 5.1.4 for details

    Only modify this template where instructed.
    Do not change the signatures of any functions.
    Do not import any libraries beyond those included by the template.
    You must complete every function
"""

import argparse
import GA_ProjectUtils as util

class unionFind:
    def __init__(self, n):
        self.pi = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def areConnected(self, p, q):
        """
            return True if 2 nodes are connected
			or False if they are not by comparing their roots
        """
        #TODO Your Code Goes Here

    def union(self, u, v):
        """
            build union of 2 components
            Be sure to maintain self.rank as needed to
            make sure your algorithm is optimal.
        """
        #TODO Your Code Goes Here

    def find(self, p):
        """
            find the root of the set containing the
            passed vertex p - Must use path compression!
        """
        #TODO Your Code Goes Here

def kruskal(G):
    """
        Kruskal algorithm
        G : graph object
    """
    #Build unionFind Object
    uf = unionFind(G.numVerts)
    #Make MST as a set
    MST = set()    
    #Get list of edges sorted by increasing weight
    sortedEdges = G.sortedEdges()   
    #Go through edges in sorted order smallest, to largest
    for e in sortedEdges:
        #TODO Your Code Goes Here (remove comments if you wish)

        # use the following line to add an edge to the MST.
        # You may change it's indentation/scope within the code
        # but do not otherwise modify it

        MST.add(util.buildMSTEdge(G,e))

        #Done - do not modify any other code below this line
    return MST, uf

def main():
    """
    main
    """
    #DO NOT REMOVE ANY ARGUMENTS FROM THE ARGPARSER BELOW
    parser = argparse.ArgumentParser(description='Minimum Spanning Tree')
    #use this flag, or change the default here to use different graph description files
    parser.add_argument('-g', '--graphFile',  help='File holding graph data in specified format', default='small.txt', dest='graphDataFileName')
    #use this flag to print the graph and resulting MST
    parser.add_argument('-p', '--print', help='Print the MSTs?', default=False, dest='printMST')
    parser.add_argument('-pg', '--print-graph', help='Print the graph?', default=False, dest='printGRAPH')
    #args for autograder, DO NOT MODIFY ANY OF THESE
    parser.add_argument('-a', '--autograde',  help='Autograder-called (2) or not (1=default)', type=int, choices=[1, 2], default=1, dest='autograde')	
    args = parser.parse_args()
    
    #DO NOT MODIFY ANY OF THE FOLLOWING CODE
    #Build graph object
    graph = util.build_MSTBaseGraph(args)
    #you may print the configuration of the graph -- only effective for graphs with up to 10 vertex
    if args.printGRAPH: graph.printMe()

    #Calculate kruskal's alg for MST
    MST_Kruskal, uf = kruskal(graph)
        
    #verify against provided prim's algorithm results
    util.verify_MSTKruskalResults(args, MST_Kruskal, args.printMST)
    
if __name__ == '__main__':
    main()