import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

df = pd.DataFrame({'one': [-1, np.nan, 2.5],
                   'two': ['foo', 'bar', 'baz'],
                   'three': [True, False, True]})

table = pa.Table.from_pandas(df)
pq.write_table(table, 'example.parquet')
table2 = pq.read_table('example.parquet')
print(table2.to_pandas())

df = pd.DataFrame({'four': [-1, np.nan, 3],
                   'five': ['foo', 'bar', 'baz'],
                   'six': ['foo1', 'bar1', 'baz1'],
                   'seven': [True, False, True]})

table = pa.Table.from_pandas(df)
pq.write_table(table, 'example.parquet')
table2 = pq.read_table('example.parquet')
print(table2.to_pandas())

