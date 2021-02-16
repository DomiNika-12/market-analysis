import pandas as pd
import csv

goodCompanies = []
A1 = []
A2 = []
with open('list.csv', 'r') as Tfile:
    TList = csv.reader(Tfile)
    count = 1
    for i in TList:
        for x in i:

            ticker = x
            print(count + 'Getting data about ' + ticker + '...')
            count = count + 1
            sampleURL = 'https://finance.yahoo.com/quote/' + ticker + '/key-statistics?p=' + ticker
            try:
                df = pd.read_html(sampleURL)
                try:
                    balanceSheet = df[8]  # current radio
                    balanceSheet.fillna(999)  # fixing NaN values
                except:
                    balanceSheet = 999
                try:
                    currentRatio = float(balanceSheet.iat[4, 1])
                except:
                    currentRatio = 999
                try:
                    valuationMeas = df[0]  # price/book
                except:
                    valuationMeas = 999
                valuationMeas.fillna(999)  # fixing NaN values
                try:
                    priceBook = float(valuationMeas.iat[6, 1])
                except:
                    priceBook = 999
                try:
                    priceToEarnings = float(valuationMeas.iat[2, 1])
                except:
                    priceToEarnings = 999
                try:
                    enterpriseValue = str(valuationMeas.iat[1, 1])
                except:
                    enterpriseValue = 999

                if 'T' in enterpriseValue:
                    enterpriseValue = float(enterpriseValue.strip('T')) * 1000000000000
                elif 'B' in enterpriseValue:
                    enterpriseValue = float(enterpriseValue.strip('B')) * 1000000000
                elif 'M' in enterpriseValue:
                    enterpriseValue = float(enterpriseValue.strip('M')) * 1000000
                else:
                    enterpriseValue = float(enterpriseValue)

                totalDebttoEquity = float(balanceSheet.iat[3, 1])

                totalDebt = str(balanceSheet.iat[2, 1])

                if 'T' in totalDebt:
                    totalDebt = float(totalDebt.strip('T')) * 1000000000000
                elif 'B' in totalDebt:
                    totalDebt = float(totalDebt.strip('B')) * 1000000000
                elif 'M' in totalDebt:
                    totalDebt = float(totalDebt.strip('M')) * 1000000
                else:
                    totalDebt = float(totalDebt)

                equity = totalDebt / totalDebttoEquity
                assets = totalDebt + equity
                DA = totalDebt / assets

                if (currentRatio >= 2) & (DA < 1.1) & (priceToEarnings <= 9) & (priceBook < 1.5):
                    goodCompanies.append(ticker)
                    print(ticker)

                if (currentRatio >= 2) & (priceBook < 1.5):
                    A1.append(ticker)

                if priceToEarnings <= 9:
                    A2.append(ticker)

            except:
                pass

print('Good companies are:')
print(goodCompanies)
print('Current ratio greater than 2 and price to book value less than 1.5:')
print(A1)
print('Price to earnings less than 9:')
print(A2)
