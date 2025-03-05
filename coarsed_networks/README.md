# Results of the coarse-graining methods appplied to the networks

This directory contains coarse-grained networks and their partitions (supernodes) data.

The file [cg_index.csv](/coarsed_networks/cg_index.csv) contains an index of all coarse-graining runs that were done in this project. Each row represents a combination of a microscopic network sample, a coarse-graining method, the coarse-graining hyperparameters and a seed to the coarse-graining method. Each row also contains a path to the coarse-grained network file and the partitions file.

## Columns of `cg_index.csv`

- `micro_networks_file`: path to the microscopic network, before coarse-graining.
- `cg_method`: name of the coarse-graining method employed.
- `seed`: for probabilistic coarse-graining methods, this value identifies one independent execution.
- `hyperparams`: \[TO BE IMPLEMENTED\] a json string with hyperparameters used for this method.
- `cg_network_file`: path to the coarsed network file. By default, it is saved as in edgelist format.
- `cg_supernodes_file`: path to the mapping between micro nodes and coarse-graining supernodes in json format ("supernode_id": \["node_1", "node_2", ...\])


