import os

import numpy as np
import pandas as pd
import pyproj

script_directory = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_directory, "..", "data")

crs = pyproj.CRS.from_string("EPSG:4326")
dataset = pd.read_csv(os.path.join(data_path, "Torino_bookings.csv"))

p = pyproj.Proj(proj="utm", zone="32", ellps="WGS84")
dataset["init_x"], dataset["init_y"] = p(dataset["init_lon"], dataset["init_lat"])
dataset["final_x"], dataset["final_y"] = p(dataset["final_lon"], dataset["final_lat"])

dataset["path_length"] = np.sqrt(
    (dataset["init_x"] - dataset["final_x"]) ** 2
    + (dataset["init_y"] - dataset["final_y"]) ** 2
)
dataset["path_length"] = dataset["path_length"] / 1000

dataset.to_csv(os.path.join(data_path, "Torino_bookings_clean.csv"), index=False)
