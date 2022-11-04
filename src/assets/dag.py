import networkx as nx
import matplotlib.pyplot as plt
#https://towardsdatascience.com/create-organization-diagrams-in-a-few-lines-of-code-the-5-minute-learn-dcca81dac3a2

graph = nx.DiGraph()
graph.add_edges_from([
    ('Division','Kingdom'),
    ('Class','Division'),
    ('Order','Class'),
    ('Order','Kingdom'),
    ('Family','Order'),
    ('Genus','Family'),
    ('Species','Genus'),
    ('Species', 'Clade_1')
    #('Species', 'Clade_2'),
    #('Species', 'Clade_3'),
    #('Species', 'Clade_4'),
    #('Species', 'Clade_5'),
    #('Species', 'Clade_6'),
])

print(nx.is_directed_acyclic_graph(graph)) 
print(list(nx.topological_sort(graph)))
plt.tight_layout()
nx.draw_networkx(graph, arrows=True)
#plt.savefig("g1.png", format="PNG")
#plt.clf()
plt.show()