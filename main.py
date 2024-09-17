from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_data(year: str) -> pd.DataFrame:
    path = Path(__file__).parent / f'data/{year}.xlsx'

    return pd.read_excel(path)

def filter_data(data: pd.DataFrame) -> pd.DataFrame:
    data = data[pd.notna(data["Country Code"])]

    data = data.replace("..", pd.NA)
    thres = len(data) * 0.3

    new_data = data.loc[:, data.isna().sum() <= thres].set_index("Country Name").drop(columns=["Country Code"])

    return new_data.convert_dtypes()

def get_correlation(data: pd.DataFrame, columns: list[str] = None) -> pd.Series:
    if columns is not None:
        corr = data[columns[0]].corr(data[columns[1]])

        return corr
    
    corr = data.corr()

    np.fill_diagonal(corr.values, np.nan)

    correlation = corr.unstack().dropna().sort_values(ascending=False)
    
    correlation = correlation[~correlation.index.get_level_values(0).str.contains("Population", case=False) &
                         ~correlation.index.get_level_values(1).str.contains("Population", case=False)]
    
    return correlation

def plot_scatter(data, columns: list[str]):
    # plt.scatter(data[columns[0]], data[columns[1]])
    
    # for i, label in enumerate(data.index):
    #     plt.text(data[columns[0]].iloc[i], data[columns[1]].iloc[i], label, fontsize=12)

    # plt.title(columns[0].split()[0])
    # plt.xlabel(columns[0])
    # plt.ylabel(columns[1])
    # plt.grid(True)

    # plt.show()

    labels = list(data.index)

    for i in range(len(data)):
        x = data[columns[0]].iloc[i]
        y = data[columns[1]].iloc[i]
        label = labels[i]

        try:
            plt.scatter(x, y, color='blue') 
        except Exception as e:
            continue
    
        plt.text(x, y, label, fontsize=5, ha='right')

    plt.xlabel(columns[0])
    plt.ylabel(columns[1])
    plt.title(columns[0].split()[0])

    plt.show()

def plot_matrix(correaltion: pd.Series):
    sns.heatmap(correaltion)

    pass

data = filter_data(get_data(2023))

plot_scatter(data, ["2023 [YR2023] - GNI per capita, Atlas method (current US$) [NY.GNP.PCAP.CD]", "2023 [YR2023] - Age dependency ratio, old [SP.POP.DPND.OL]"])

correaltion = get_correlation(data)

# plot_matrix(correaltion=correaltion)
