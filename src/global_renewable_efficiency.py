import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


def clean_data_renew(filepath):

    '''
    input is a filepath leading to the dataset. This won't help you very much unless you're using the exact data set lined out in the readme

    output is a parsed dataframe, mostly just dropping unuseable columns and rows that had null values
    '''
    df_renew_stp1 = pd.read_csv(filepath)
    df_renew_stp2 = df_renew_stp1.drop(columns=['Series Code', 'Country Code'], axis=1)
    df_renew_stp3 = df_renew_stp2.drop(df_renew_stp2.loc[df_renew_stp2['1990 [YR1990]'] == '..'].index)
    df_renew_index_series = df_renew_stp3.astype({'1990 [YR1990]': float,
                                                '1991 [YR1991]': float,
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

def clean_data_efficiency(filepath):

    '''
    input is a filepath leading to the dataset. This won't help you very much unless you're using the exact data set lined out in the readme

    output is a parsed dataframe, mostly just dropping unuseable columns and rows that had null values.

    You may notice that both of these functions do essentially the same job and that's because they are compiled in a similar format with few deviations.
    '''
    df_eff_stp1 = pd.read_csv(filepath)
    df_eff_stp2 = df_eff_stp1.drop(columns=['Series Code', 'Country Code'], axis=1)
    df_eff_stp3 = df_eff_stp2.drop(df_eff_stp2.loc[df_eff_stp2['1990 [YR1990]'] == '..'].index)
    df_eff_country_series = df_eff_stp3.astype({'1990 [YR1990]': float,
                                                '1991 [YR1991]': float,
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
    return df_eff_country_series

def global_graph(input_graph_renew, input_graph_eff):
    '''
    input are the two graphs cleaned up above.

    output is a graph of my design, showing two graphs, one which compares global increases in non-renewable to renewable energy and the other that shows the relative efficiency of energy to global value produced.

    for the graphing, I believe most of this code is fairly understandable - There's not complex math happening here. The biggest thing is that I had to create a different ratio to more accurately reflect a global ratio
    '''
    df_renew_stp1 = input_graph_renew.drop('Country Name', axis=1)
    df_renew = df_renew_stp1.groupby('Series Name').mean(numeric_only=True)
    df_eff = input_graph_eff.groupby('Series Name').mean(numeric_only=True)
    x_renew = df_renew.columns[:]
    y_renew = df_renew.loc['Renewable electricity output (GWh)']
    y1_renew = df_renew.loc['Renewable electricity output (GWh)'] / df_renew.loc['Total electricity output (GWh)'] 
    y2_renew = df_renew.loc['Total electricity output (GWh)']
    fig, (axs1, axs2)  = plt.subplots(2, figsize=(10,14), sharex=True)
    ax2 = axs1.twinx()
    x_eff = df_eff.columns[:]
    y_eff = df_eff.loc['Energy intensity level of primary energy (MJ/2011 USD PPP)']
    axs1.plot(x_renew, y_renew, label="Renewable electricity output (GWh)", color="blue", marker='.')
    ax2.plot(x_renew, y1_renew, label="Renewable electricity share of total electricity output (%)", color="purple", marker='.')
    axs1.plot(x_renew, y2_renew, label="Total electricity output (GWh)", color="red", marker='.')
    axs1.set_title("Renewable Energy")
    axs1.set_xlabel("Years")
    axs1.legend()
    ax2.legend(loc = 1)
    axs2.plot(x_eff, y_eff, label="Energy intensity level of primary energy (MJ/2011 USD PPP)", color="blue", marker='.')
    axs2.set_title('Efficiency')
    axs2.set_xlabel("Years")
    axs2.set_ylabel('Energy Efficeincy in terms of USD PPP')
    axs2.legend()
    fig.autofmt_xdate()
    plt.show()

if __name__ == '__main__':
    '''
    If name = main block. Setting out file paths and plugging them in to the functions defined above.
    '''
    renew_path = '../data/Renewable - gtfrenewableenergydata.csv'
    eff_path = '../data/Efficiency - gtfprimaryenergyintensitydata.csv'
    global_graph(clean_data_renew(renew_path),clean_data_efficiency(eff_path))
