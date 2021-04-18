import networkx as nx 
import numpy as np


g1 = nx.complete_graph(["n{}".format(i) for i in range(0, 5)])
g2 = nx.complete_graph(["n{}".format(i) for i in range(0, 5)])

for i in range(0, 3):
    r_n = np.random.choice(g2.nodes())
    print("node removed: {}".format(r_n))
    print("edge removed: {}".format([e for e in g2.edges() if r_n in e]))
    g2.remove_node(r_n)
    print(nx.similarity.graph_edit_distance(g1, g2))
    print("="*50)