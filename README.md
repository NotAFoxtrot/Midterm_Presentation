# Midterm_Presentation

## Question?

How has renewable energy and electrical consumption changed over a 25 year period from 1990 to 2014? What kinds of conclusions can be reached by this? How can we expect the future of our renewable landscape to change?

## The Data

I got my datasets from Energydata.info
The datasets were compiled by the World Bank Group under the World - Global Tracking Framework model
There were three in total, but two of them shared a common timeline and complimented each other while the third would only provide ancillary information. One I used had a very basic data set of efficiency of electricity used as a ratio to global production (efficiency). The other had six categories to choose from (Renewable). Three of them were in terms of Terajoules and Three of them were in terms of Gigawatt Hours. For the sake of brevity and ease of consumption, I decided to use the categories that used Gigawatt hours, as the difference between the Terajoules and Gigawatt Hours is mostly semantic and they showed practically the same graph. After this, I pared them both down and plotted them on two graphs that had the same x axis so that they would show a global average over those 25 years.

## The Code
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
```

First, the imports. Nothing too crazy. Just pandas, numpy and the graphs

```python
def clean_data_renew(filepath):
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
```

Both of these data cleaners do effectively the same thing. I broke the cleaning process down into various steps for readability, but this wouldn't be feasible for larger data sets, unless you have a lot of memory. First step is read from a filepath. Then drop the columns which distracted from the data, Series and Country Code. After that, I had to get rid of the data which didn't have anything in them, denoted by '..'. After going through the data, I saw that any values which had those null pointers were too small to affect the data set at all - Think, Tonga, Togo, or the Canary Islands. The last step was to bring all numeric values from string to float (that one was a head scratcher for sure). 


```python
def global_graph(input_graph_renew, input_graph_eff):
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
```

The last step of the process was plotting it all out. I believe the only thing of note here is that because the original spreadsheet showed the ratio in terms of countries, those weren't weighted properly so compiling them through a mean would give bad data. For example, Switzerland's high percentage would even out with China's low percentage, despite China having much more energy production. Therfore, I decided to make a simple ratio with the data I had.


```python
if __name__ == '__main__':
    renew_path = '../data/Renewable - gtfrenewableenergydata.csv'
    eff_path = '../data/Efficiency - gtfprimaryenergyintensitydata.csv'
    global_graph(clean_data_renew(renew_path),clean_data_efficiency(eff_path))
```


[Test_data/Renewable_Graph.png](Test_Data/Renewable_Graph.png)

# The Outcome

The two graphs show interesting, but nearly conflicting information. On the one hand, the information in the graph up top shows a hopeful image of our renewable energy sources outpacing and eventually overcoming non-renewable. The purple line being the ratio and as it increases, the more renewables we use in comparison to non-renewables. The graph on the bottom, however, is more difficult to understand. After all, in most business classes a simple truth is taught: the more we do capitalism, the better we get at it. First we have sticks and stones and now we have Legend of Zelda: Tears of the Kingdom. More simply, the things we create get better and better. Our GDP (PPP) produced per unity of energy should be increasing, not decreasing. This points to a few different hypothesese which could be looked into with other sets of data in other projects.

1.) Our level of technological progress has not shown nearly the rate of improvement as in previous decades. The typepress changed everything. The steam engine changed everything. The internet changed everything... What after that? Without a technological improvement on the level of the introduction and proliferation of the internet, our rate of productivity will plateau, even if our energy production rises. As a corollary, we are increasing energy production to make up for the lack of productivity.

2.) Efficiency doesn't actually matter for the exact reason of technological advancement. As our methodologies improve, so too does our ability to extract large amounts of energy for a cheap price. As our technologies improve, the cost of our energy production goes down and our efficiency in using it decreases due to its abundance. To put more simply: because there's so much energy, we don't have to be efficient with it.

Though times are tough right now, capital reigns supreme. I suspect that because renewables are showing such leaps and bounds in progress we can see them continue to outpace non-renewables as their sources become cheaper and cheaper in comparison.