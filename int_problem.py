import csv
from decimal import Decimal
file = 'AAPL.csv'

#backtest trading strategy
#calculate max profit over a given day range, buy/sell restricted to start.
#def find_max_profit_range(start, high, low):

#Cleaning up data
#Date,Close/Last,Volume,start,high,low
#09/01/2023,$189.46,45766500,$189.485,$189.92,$188.28
#output: low, high, start
#output: start, high, low

#Date,Open,High,Low,Close,Adj Close,Volume

start = []
high = []
low = []

def order_csv(a, b, c):
    with open(file, 'r') as f:
        for i, j in enumerate(reversed(list(csv.reader(f)))):
            start.append(Decimal(j[a].replace("$", "")))
            high.append(Decimal(j[b].replace("$", "")))
            low.append(Decimal(j[c].replace("$", "")))

order_csv(1, 2, 3)

def max_profit(start):
    profit = 0
    min = start[0]
    for i in range(0, len(start)):
        diff = start[i] - min
        if start[i] < min:
            min = start[i]
        if diff > profit:
            profit = diff
    return profit

def max_profit_original(start):
    profit = 0
    for i in range(0, len(start) - 1):
        for j in range(0, len(start)):
            if j > i:
                if start[j] - start[i] > profit:
                    profit = start[j] - start[i]
    return profit

print(max_profit(start))
print(max_profit_original(start))