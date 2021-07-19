import pandas as pd
import glob


def process_data(data):
    result = data.copy()
    result["Library"] = result["Key Feature"]
    result["Solution"] = result["Solution"].str.replace(" _", "_")
    result["Solution Code"] = result["Solution Code"].str.replace(" ", "")
    result["Snapshot"] = pd.to_datetime(result["Snapshot"], format="%d/%m/%Y")
    result["Completeness Ratio"] = result["Completeness Ratio"].str.replace(",", ".")
    result["Completeness Ratio"] = result["Completeness Ratio"].astype(float)
    result["Completeness Ratio"] = result["Completeness Ratio"].fillna(value="N/A")

    result["Level of automation"] = result["Level of automation"].str.replace(",", ".")
    result["Level of automation"] = result["Level of automation"].astype(float)
    result["Level of automation"] = result["Level of automation"].fillna(value="N/A")

    result["Difference"] = result["Difference"].str.replace(",", ".")
    result["Difference"] = result["Difference"].astype(float)
    result["Difference"] = result["Difference"].fillna(value="N/A")

    result["Coverage"] = result["Coverage"].fillna(value="N/A")

    return result


dataset_names = glob.glob("assets/*.XLS")

processed_datasets = []
for name in dataset_names:
    dataset = pd.read_excel(name)
    processed_datasets.append(process_data(dataset))

merged_dataset = pd.concat(processed_datasets)
merged_dataset.to_excel("processed_data.xlsx", index=False)
