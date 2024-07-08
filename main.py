from banks_project import extract, transform

url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv'
table_attribs = ["Name", "MC_USD_Billion"]
table_attribs_final = ['Name', "MC_USD_Billion", 'MC_GBP_Billion', 'MC_EUR_Billion', 'MC_INR_Billion']

if __name__ == '__main__':
    df = extract(url, table_attribs)
    df2 = transform(df, csv_path)
    print(df2)
