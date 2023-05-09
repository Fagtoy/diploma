import pandas as pd

if __name__ == '__main__':
    # gdp_data = pd.read_csv(
    #     'API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_4901640/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_4901640.csv')
    # usa_gdp = gdp_data[gdp_data['Country Name'] == 'United States']
    # mexico_gdp = gdp_data[gdp_data['Country Name'] == 'Mexico']
    # latin_america_gdp = gdp_data[gdp_data['Country Name'] == 'Latin America & Caribbean']
    # usa_gdp_growth = []
    # mexico_gdp_growth = []
    # latin_america_gdp_growth = []
    # for year in range(1999, 2017):
    #     year = str(year)
    #     usa_gdp_growth.append(usa_gdp[year].values[0])
    #     mexico_gdp_growth.append(mexico_gdp[year].values[0])
    #     latin_america_gdp_growth.append(latin_america_gdp[year].values[0])
    # full_data = pd.read_csv('full_data.csv')
    # full_data['usa_gdp_growth'] = usa_gdp_growth
    # full_data['mexico_gdp_growth'] = mexico_gdp_growth
    # full_data['latin_america_gdp_growth'] = latin_america_gdp_growth
    # full_data.to_csv('full_data.csv')

    gdp_by_quarter = [
        4.8, 4.7, 4.8, 4.8, 4.2, 5.2, 4.0, 2.9, 2.2, 1.0, 0.5, 0.2, 1.3, 1.3, 2.1, 2.0, 1.7, 2.0, 3.2, 4.3, 4.4, 4.2,
        3.5, 3.4, 3.9, 3.6, 3.4, 3.0, 3.2, 3.0, 2.3, 2.6, 1.5, 1.9, 2.4, 2.2, 1.4, 1.4, 0.2, -2.5, -3.3, -4.0, -3.1,
        0.1, 1.8, 2.9, 3.3, 2.8, 2.0, 1.7, 0.9, 1.5, 2.6, 2.4, 2.6, 1.6, 1.6, 1.3, 1.9, 2.5, 1.3, 2.5, 2.8, 2.6, 3.8,
        3.0, 2.2, 1.9, 1.6, 1.4, 1.6, 2.0,
    ]
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    i = 0
    while i < 72:
        q1.append(gdp_by_quarter[i])
        i += 1
        q2.append(gdp_by_quarter[i])
        i += 1
        q3.append(gdp_by_quarter[i])
        i += 1
        q4.append(gdp_by_quarter[i])
        i += 1
    full_data = pd.read_csv('full_data.csv')
    full_data['usa_q1_gdp_growth'] = q1
    full_data['usa_q2_gdp_growth'] = q2
    full_data['usa_q3_gdp_growth'] = q3
    full_data['usa_q4_gdp_growth'] = q4
    full_data.to_csv('full_data.csv')
