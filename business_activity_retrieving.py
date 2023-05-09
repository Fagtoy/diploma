import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('business_activity_by_quarters.csv')
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
        quarters[current_row_num].append(v['BFBF4QTOTALSAUS'])
        if current_row_num == 4:
            current_row_num = 0
    business_activity_df = pd.DataFrame(
        {
            'year': range(2005, 2017),
            'usa_business_activity_q1': quarters[1],
            'usa_business_activity_q2': quarters[2],
            'usa_business_activity_q3': quarters[3],
            'usa_business_activity_q4': quarters[4],
        }
    )
    df = pd.read_csv('full_data.csv')
    df = pd.merge(df, business_activity_df, on='year', how='outer').fillna('null')
    df.to_csv('full_data.csv')
