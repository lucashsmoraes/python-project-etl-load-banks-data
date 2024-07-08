from banks_project import extract
url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Bank name", "Market cap"]

if __name__ == '__main__':
    df = extract(url, table_attribs)
    print(df)