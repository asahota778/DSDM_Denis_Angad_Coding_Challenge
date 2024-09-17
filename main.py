from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_data(year: str) -> pd.DataFrame:
    """
    Returns data from coressponding file. Using realtive path. 
    """
    path = Path(__file__).parent / f'data/{year}.xlsx'

    return pd.read_excel(path) # using read_excel finction since original data was downloaded in .xlsx format

def filter_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Returns new pd.DataFrame object with cleaned rows and columns
    """

    # deleting corrupted xlsx rows
    data = data[pd.notna(data["Country Code"])]

    # deleting country code column and setting country name as an index to ger rid off non numerical values
    data = data.set_index("Country Name").drop(columns=["Country Code"]) 
    
    # replacing typical ".." with nan values
    data = data.replace("..", pd.NA)

    # setting the threshold for number of nan values in each of the column
    thres = len(data) * 0.3

    # deleting all the columns where number of nan values is bigger than thres (for example, for len 100, 30 nan values for a column is a max)
    new_data = data.loc[:, data.isna().sum() <= thres]

    # since data from xlsx is corrupted, translating all "object" types to numerical
    return new_data.convert_dtypes() 

def get_correlation(data: pd.DataFrame, columns: list[str] = None) -> pd.Series:
    """
    If columns are not passed, returns correlation for each of the columns, otherwise returns correaltion of two pd.Series
    """
    if columns is not None:
        corr = data[columns[0]].corr(data[columns[1]])

        return corr
    
    corr = data.corr()

    # replace 1-1 correaltion with nan
    np.fill_diagonal(corr.values, np.nan)
    
    # make it long format and delete nan values, make it from top to bottom
    correlation = corr.unstack().dropna().sort_values(ascending=False)
    
    # delete all population related columns since they are too obvious 
    correlation = correlation[~correlation.index.get_level_values(0).str.contains("Population", case=False) &
                         ~correlation.index.get_level_values(1).str.contains("Population", case=False)]
    
    return correlation

def plot_scatter(data, columns: list[str]):
    # to use it for labeling
    labels = list(data.index)

    for i in range(len(data)):
        x = data[columns[0]].iloc[i]
        y = data[columns[1]].iloc[i]
        label = labels[i]

        if pd.isna(x) or pd.isna(y):
            continue

        plt.scatter(x, y, color='blue') 
    
        plt.text(x, y, label, fontsize=5, ha='right')

    plt.xlabel(columns[0])
    plt.ylabel(columns[1])
    plt.title(columns[0].split()[0])

    plt.show()

def main():
    years = [2021, 2022, 2023]

    for year in years:
        # get data
        data = filter_data(get_data(year))
        
        # # correlation for every column
        # base_correlation = get_correlation(data)

        # print(base_correlation)

        # identify columns to be scattered
        columns = [f'{year} [YR{year}] - GNI per capita, Atlas method (current US$) [NY.GNP.PCAP.CD]', f'{year} [YR{year}] - Age dependency ratio, old [SP.POP.DPND.OL]']

        correlation = get_correlation(data, columns=columns)

        print(f'Correaltion of {columns[0]} to {columns[1]} is {correlation}')

        plot_scatter(data, columns=columns)

if __name__ == "__main__":
    main()
    

