import os

folder = "data/raw"
for f in sorted(os.listdir(folder)):
    if f.endswith(".csv"):
        print(f)