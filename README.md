# Networks for testing Coarse-Graining methods

A repository of networks for benchmarking network coarse-graining methods.

# Usage

Networks with no coarse-graining are located in the [micro_networks](/micro_networks) subdirectory.

To load a network `txt` file, just import with Networkx as an edgelist. Example:

```python
import networkx as nx

fpath = "micro_networks/erdos-renyi/er_n0100_m010_0001.txt"
g = nx.read_edgelist(fpath)
```

To save a Networkx graph in the same format, you can use `write_edgelist`. If the network has no weights or any other info appended to the links, you can use `data=False`:

```python
import networkx as nx

g = nx.erdos_renyi_graph(n=100, p=0.1)
fpath = "example_output/my-graph.txt"
nx.write_edgelist(g, fpath, data=False)
```
