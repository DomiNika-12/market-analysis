import pandas as pd
import csv

#Gives the user list of tickers of all the companies from S&P500 index
AllTickers=[]
with open ('sandp500.csv','r') as df:
    ReaderCSV = csv.reader(df)
    for line in ReaderCSV:
        ticker=line[0]
        print(line)
        if '.' in ticker:
            ticker = ticker.replace('.','-')
            AllTickers.append(ticker)
        else:
            AllTickers.append(ticker)
with open ('list.csv', 'w') as file:
    del AllTickers[0]
    writer = csv.writer(file)
    writer.writerow(AllTickers)

print(len(AllTickers))