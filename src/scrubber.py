import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


def clean_data():
    df_renew_stp1 = pd.read_csv('../data/Renewable - gtfrenewableenergydata.csv')
    df_renew_stp2 = df_renew_stp1.drop(columns=['Series Code', 'Country Code'], axis=1)
    df_renew_stp3 = df_renew_stp2.drop(df_renew_stp2.loc[df_renew_stp2['1990 [YR1990]'] == '..'].index)
    df_renew_index_series = df_renew_stp3.astype({'1991 [YR1991]': float,
                                                '1992 [YR1992]': float,
                                                '1993 [YR1993]': float,
                                                '1994 [YR1994]': float,
                                                '1995 [YR1995]': float,
                                                '1996 [YR1996]': float,
                                                '1997 [YR1997]': float,
                                                '1998 [YR1998]': float,
                                                '1999 [YR1999]': float,
                                                '2000 [YR2000]': float,
                                                '2001 [YR2001]': float,
                                                '2002 [YR2002]': float,
                                                '2003 [YR2003]': float,
                                                '2004 [YR2004]': float,
                                                '2005 [YR2005]': float,
                                                '2006 [YR2006]': float,
                                                '2007 [YR2007]': float,
                                                '2008 [YR2008]': float,
                                                '2009 [YR2009]': float,
                                                '2010 [YR2010]': float,
                                                '2011 [YR2011]': float,
                                                '2012 [YR2012]': float,
                                                '2013 [YR2013]': float,
                                                '2014 [YR2014]': float
                                                })
    return df_renew_index_series

def global_graph_renewdf(input_graph):
    df_stp1 = input_graph.drop('Country Name', axis=1)
    df = df_stp1.groupby('Series Name').mean(numeric_only=True)
    x = df.columns[:]
    y = df.loc['Renewable electricity output (GWh)']
    y1 = df.loc['Renewable electricity output (GWh)'] / df.loc['Total electricity output (GWh)'] 
    y2 = df.loc['Total electricity output (GWh)']
    fig, ax  = plt.subplots(figsize=(10,7), sharex=True)
    ax2 = ax.twinx()
    ax.plot(x, y, label="Renewable electricity output (GWh)", color="blue", marker='.')
    ax2.plot(x, y1, label="Renewable electricity share of total electricity output (%)", color="purple", marker='.')
    ax.plot(x, y2, label="Total electricity output (GWh)", color="red", marker='.')
    ax.set_title("Renewable Field")
    ax.set_xlabel("Years")
    ax.set_ylabel("Signifiers")
    ax.legend()
    ax2.legend(loc = 1)
    #plt.xticks(rotation=90)
    fig.autofmt_xdate()
    plt.show()

if __name__ == '__main__':
    global_graph_renewdf(clean_data())
