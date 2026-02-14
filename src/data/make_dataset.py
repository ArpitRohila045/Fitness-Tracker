from glob import glob
import pandas as pd
from typing import List, Tuple

#---------------------------------------------
# Read all the files
#---------------------------------------------
file_path = "../../data/raw/MetaMotion/*.csv"
data_path = r"C:\\Users\\hp\\Desktop\\Fitness-Tracker\\data\\raw\\MetaMotion\\"

def read_from_files(files : List[str]):
    """
    Docstring for read_from_files
    
    :param path: Description
        files : list of files path 
    
    """

    acc_data = pd.DataFrame()
    gyr_data = pd.DataFrame()
    acc_set = 1
    gyr_set = 1

    for f in files:
        participant = f.split("-")[0].replace(data_path, "")
        label = f.split("-")[1]
        category = f.split("-")[2].rstrip("123").rstrip("_MetaWear_2019")

        df = pd.read_csv(f)

        df["participant"] = participant
        df["label"] = label
        df["category"] = category

        if "Acceleromenter" in f:
            df["set"] = acc_set
            acc_set += 1
            acc_data = pd.concat([acc_data, df])
        else:
            df["set"] = gyr_set
            gyr_set += 1
            gyr_data = pd.concat([gyr_data, df])
    
    acc_data.index = pd.to_datetime(acc_data["epoch (ms)"], unit="ms")
    gyr_data.index = pd.to_datetime(gyr_data["epoch (ms)"], unit="ms")

    del acc_data["epoch (ms)"]
    del acc_data["time (1:00)"]
    del acc_data["elapsed (s)"]

    del gyr_data["epoch (ms)"]
    del gyr_data["time (1:00)"]
    del gyr_data["elapsed (s)"]

    return acc_data, gyr_data

files = glob(r"C:\Users\hp\Desktop\Fitness-Tracker\data\raw\MetaMotion\*.csv")

if not files:
    print("No files found!")

print(files)

acc_data, gyr_data = read_from_files(files=files)

merged_data = pd.concat([acc_data.iloc[:, :3], gyr_data], axis=1)

merged_data.columns = [
    "acc_x",
    "acc_y",
    "acc_z",
    "gyr_x",
    "gry_y",
    "gry_z",
    "participant",
    "label",
    "category",
    "set"
]


sampling = {
    "acc_x" : "mean",
    "acc_y" : "mean",
    "acc_z" : "mean",
    "gyr_x" : "mean",
    "gry_y" : "mean",
    "gry_z" : "mean",
    "participant" : "last",
    "label" : "last",
    "category" : "last",
    "set" : "last"
}


days = [g for n, g in merged_data.groupby(pd.Grouper(freq="D"))]

data_resampled = pd.concat([df.resample(rule="200ms").apply(sampling).dropna() for df in days])

data_resampled["set"] = data_resampled["set"].astype("int")

data_resampled.to_pickle("../data/interme/01_data_processed.pkl")

