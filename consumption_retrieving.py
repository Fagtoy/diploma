import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('inflation_quarterly.csv')
    years = []
    quarters = {
        1: [],
        2: [],
        3: [],
        4: [],
    }
    current_row_num = 0
    for i, v in df.iterrows():
        current_row_num += 1
        quarters[current_row_num].append(v['BPCCRO1Q156NBEA'])
        if current_row_num == 4:
            current_row_num = 0
    inflation_df = pd.DataFrame(
        {
            'year': range(1999, 2017),
            'usa_inflation_q1': quarters[1],
            'usa_inflation_q2': quarters[2],
            'usa_inflation_q3': quarters[3],
            'usa_inflation_q4': quarters[4],
        }
    )
    df = pd.read_csv('full_data.csv')
    df = pd.merge(df, inflation_df, on='year')
    df.to_csv('full_data.csv')
    # df = pd.read_csv('full_data.csv')[
    #     ['usa_consumption_q1', 'usa_consumption_q2', 'usa_consumption_q3', 'usa_consumption_q4']
    # ]
    # year_consumption = []
    # for _, row in df.iterrows():
    #     average = (
    #             row['usa_consumption_q1'] + row['usa_consumption_q2'] + row['usa_consumption_q3'] + row['usa_consumption_q4']
    #     ) / 4
    #     year_consumption.append(average)
    # df = pd.DataFrame(
    #     {
    #         'year': range(1999, 2017),
    #         'usa_consumption': year_consumption,
    #     }
    # )
    # df = pd.merge(pd.read_csv('full_data.csv'), df, on='year')
    # df.to_csv('full_data.csv')
