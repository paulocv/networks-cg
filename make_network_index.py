"""
Create an index file for the networks in the dataset
"""
import glob
from pathlib import Path

import pandas as pd


def main():
    """"""

    # Parameters
    # ===============
    # repo_dir = Path("networks-cg")
    repo_dir = Path(".")
    input_data_dict = {
        # "erdos-renyi": {
        #     "dirpath": Path("micro_networks/erdos-renyi"),
        # },
        "erdos-renyi-typical": {
            "dirpath": Path("micro_networks/erdos-renyi-typical"),
        },
        "barabasi-albert": {
            "dirpath": Path("micro_networks/barabasi-albert"),
        },
        "random-hyperbolic-graphs": {
            "dirpath": Path("micro_networks/random-hyperbolic-graphs"),
        },
        "erdos-renyi-connected": {
            "dirpath": Path("micro_networks/erdos-renyi-connected"),
        },
    }

    out_index_fpath = repo_dir / "micro_networks" / "index.csv"
    do_export = True


    # =============

    df_list = list()
    for entry_name, entry_data in input_data_dict.items():
        dirpath = entry_data["dirpath"]
        full_dirpath = repo_dir / dirpath
        network_format = entry_data.get("network_format", "edgelist")

        # --- Check path existence
        if not full_dirpath.exists():
            print(f"Directory not found [SKIPPED]:{full_dirpath}")
            continue

        # --- Get list of files
        file_list = glob.glob(str(full_dirpath / "*"))  # Get all txt files in the folder

        # --- Filter files
        file_list = [f for f in file_list if "dummy" not in f]

        print(f"Found {len(file_list)} files in {full_dirpath}")

        # --- Save data on a dataframe
        n = len(file_list)
        df = pd.DataFrame(
            {
                "network_type": [entry_name] * n,
                "network_format": [network_format] * n,
                "file_path": file_list,
            },

        )

        # keys_list.append(entry_name)
        df_list.append(df)

    out_df = pd.concat(df_list, axis=0)

    # --- Export
    if do_export:
        out_df.to_csv(out_index_fpath, index=False)


if __name__ == "__main__":
    main()
