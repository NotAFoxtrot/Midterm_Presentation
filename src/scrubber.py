import pandas as pd
import numpy as np

df_renew_stp1 = pd.read_csv('../data/Renewable - gtfrenewableenergydata.csv')
df_renew_stp2 = df_renew_stp1.drop(columns=['Series Code', 'Country Code'], axis=1)
df_renew_stp3 = df_renew_stp2.sort_values('Country Name')
print(df_renew_stp3.head())

def clean_data():
    pass

if __name__ == '__main__':
    clean_data()
