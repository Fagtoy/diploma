import pandas as pd

if __name__ == '__main__':
    # df1 = pd.read_csv('aggregated_data.csv')
    # df2 = pd.read_csv('nasdaq_1999_2016_by_quarter.csv')
    # df3 = pd.read_csv('dow_jones_1999_2016_by_quarter.csv')
    # df4 = pd.read_csv('s&p500_1999_2016_by_quarter.csv')
    # df = pd.merge(df1, df2, on='year')
    # df = pd.merge(df, df3, on='year')
    # df = pd.merge(df, df4, on='year')
    # df.to_csv('full_data.csv')

    df1 = pd.read_csv('full_data.csv')
    df2 = pd.read_csv('nasdaq_1999_2016_by_year.csv')
    df3 = pd.read_csv('dow_jones_1999_2016_by_year.csv')
    df4 = pd.read_csv('s&p500_1999_2016_by_year.csv')
    df = pd.merge(df1, df2, on='year')
    df = pd.merge(df, df3, on='year')
    df = pd.merge(df, df4, on='year')
    df.to_csv('full_data.csv')
