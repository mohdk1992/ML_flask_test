import pandas as pd
import pathlib

path = pathlib.Path('data').absolute()
inputFolder = path
df = pd.read_csv(path / 'iris.csv')
print(df.head())