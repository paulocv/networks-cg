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
