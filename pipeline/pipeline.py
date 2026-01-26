import sys

import pandas as pd

print('arguments', sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df['month'] = month

df.to_parquet(f"output_day_{sys.argv[1]}.parquet") # parquet is file that saves data as column based: column day: [1, 2], column num_passengers: [3, 4]

print(df.head())

print(f'hello pipeline, month = {month}')