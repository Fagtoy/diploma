import pandas as pd
import yfinance as yf


def get_historical_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    ticker = yf.Ticker(ticker)
    return ticker.history(start=start, end=end, interval='3mo')


def save_historical_data_by_year(history_data: pd.DataFrame, file_to_save: str, column_prefix: str) -> pd.DataFrame:
    years = []
    open_prices = []
    close_prices = []
    i = 0
    while i <= 68:
        closing_month_index = i + 3
        open_price = history_data.iloc[i, 0]
        close_price = history_data.iloc[closing_month_index, 3]
        years.append(1999 + closing_month_index // 4)
        open_prices.append(open_price)
        close_prices.append(close_price)
        i = i + 4
    data_by_year = pd.DataFrame(
        {'year': years, f'{column_prefix}_open': open_prices, f'{column_prefix}_close': close_prices}
    )
    data_by_year.to_csv(file_to_save, index=False)
    return data_by_year


def save_historical_data_by_quarter(history_data: pd.DataFrame, file_to_save: str, column_prefix: str) -> pd.DataFrame:
    quarter_columns = [
        [[], []],
        [[], []],
        [[], []],
        [[], []],
    ]
    quarter_count = 0
    year = 1999
    for index, row in history_data[['Open', 'Close']].iterrows():
        quarter = quarter_columns[quarter_count]
        quarter[0].append(row['Open'])
        quarter[1].append(row['Close'])
        quarter_count += 1
        if quarter_count == 4:
            year += 1
            quarter_count = 0
    data_by_year = pd.DataFrame(
        {
            'year': range(1999, 2017),
            f'{column_prefix}_first_quarter_open': quarter_columns[0][0],
            f'{column_prefix}_first_quarter_close': quarter_columns[0][1],
            f'{column_prefix}_second_quarter_open': quarter_columns[1][0],
            f'{column_prefix}_second_quarter_close': quarter_columns[1][1],
            f'{column_prefix}_third_quarter_open': quarter_columns[2][0],
            f'{column_prefix}_third_quarter_close': quarter_columns[2][1],
            f'{column_prefix}_fourth_quarter_open': quarter_columns[3][0],
            f'{column_prefix}_fourth_quarter_close': quarter_columns[3][1],
        }
    )
    data_by_year.to_csv(file_to_save, index=False)
    return data_by_year


if __name__ == '__main__':
    nasdaq_data = get_historical_data('^IXIC', '1999-01-01', '2016-12-31')
    nasdaq_data[['Open', 'Close']].to_csv('nasdaq_1999_2016.csv', index=False)
    nasdaq_data_by_year = save_historical_data_by_year(nasdaq_data, 'nasdaq_1999_2016_by_year.csv', 'nasdaq')
    nasdaq_data_by_quarter = save_historical_data_by_quarter(nasdaq_data, 'nasdaq_1999_2016_by_quarter.csv', 'nasdaq')

    dow_jones_data = get_historical_data('^DJI', '1999-01-01', '2016-12-31')
    dow_jones_data[['Open', 'Close']].to_csv('dow_jones_1999_2016.csv', index=False)
    dow_jones_data_by_year = save_historical_data_by_year(dow_jones_data, 'dow_jones_1999_2016_by_year.csv', 'dow_jones')
    dow_jones_data_by_quarter = save_historical_data_by_quarter(dow_jones_data, 'dow_jones_1999_2016_by_quarter.csv', 'dow_jones')

    snp500_data = get_historical_data('^GSPC', '1999-01-01', '2016-12-31')
    snp500_data[['Open', 'Close']].to_csv('s&p500_1999_2016.csv', index=False)
    snp500_data_by_year = save_historical_data_by_year(snp500_data, 's&p500_1999_2016_by_year.csv', 's&p500')
    snp500_data_by_quarter = save_historical_data_by_quarter(snp500_data, 's&p500_1999_2016_by_quarter.csv', 's&p500')
