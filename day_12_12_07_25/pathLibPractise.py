import os
from pathlib import Path
print(len(dir(Path)))
print(dir(Path))
print(Path.cwd())
print(os.getcwd())
data_file = Path("data/report_2024.csv")
print(data_file.name)
print(data_file.suffix)
print(data_file.stem)
print(data_file.parent)