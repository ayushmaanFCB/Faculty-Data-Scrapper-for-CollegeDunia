import pandas as pd

df1 = pd.read_excel("./data/karnataka1.xlsx")
df2 = pd.read_excel("./data/karnataka2.xlsx")

print("Intial Lengths : ", df1.shape, "\t", df2.shape)

combined_df = pd.concat([df1, df2], axis=0)

print("New Shape : ", combined_df.shape)
combined_df.to_excel("./data/KARNATAKA.xlsx")
