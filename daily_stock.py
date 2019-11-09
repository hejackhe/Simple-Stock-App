import csv

"""
Functions:
    daily_movement()    ---> change in price of a stock on a given date
    daily_high()        ---> highest price of a stock on a given date
    daily_low()         ---> lowest price of a stock on a given date
    daily_average()     ---> average price of a stock on a given date
    percentage_change() ---> percentage change in price of a stock on a given date
"""

def daily_movement(data, code, date):
    if date in [row['date'] for row in data]:
        if code in [row['code'] for row in data]:
            dailyPrices = [float(row['price']) for row in data if (row['code']==code and row['date']==date)]
            return(round(dailyPrices[len(dailyPrices)-1] - dailyPrices[0], 2))
        else:
            return("Error: Data for selected code does not exist, try another code.")
    else:
        return("Error: Data for selected date not available, try another date.")
    
def daily_high(data, code, date):
    if date in [row['date'] for row in data]:
        if code in [row['code'] for row in data]:
            dailyPrices = [float(row['price']) for row in data if (row['code']==code and row['date']==date)]
            return(round(max(dailyPrices), 2))
        else:
            return("Error: Data for selected code does not exist, try another code.")
    else:
        return("Error: Data for selected date not available, try another date.")

def daily_low(data, code, date):
    if date in [row['date'] for row in data]:
        if code in [row['code'] for row in data]:
            dailyPrices = [float(row['price']) for row in data if (row['code']==code and row['date']==date)]
            return(round(min(dailyPrices), 2))
        else:
            return("Error: Data for selected code does not exist, try another code.")
    else:
        return("Error: Data for selected date not available, try another date.")

def daily_avg(data, code, date):
    if date in [row['date'] for row in data]:
        if code in [row['code'] for row in data]:
            dailyPrices = [float(row['price']) for row in data if (row['code']==code and row['date']==date)]
            return(round(sum(dailyPrices) / len(dailyPrices), 2))
        else:
            return("Error: Data for selected code does not exist, try another code.")
    else:
        return("Error: Data for selected date not available, try another date.")

def percentage_change(data, code, date):
    if date in [row['date'] for row in data]:
        if code in [row['code'] for row in data]:
            dailyPrices = [float(row['price']) for row in data if (row['code']==code and row['date']==date)]
            pc_change = round(((dailyPrices[-1] - dailyPrices[0]) / dailyPrices[0]) * 100, 2)
            return(pc_change)
        else:
            return("Error: Data for selected code does not exist, try another code.")
    else:
        return("Error: Data for selected date not available, try another date.")


if __name__ == "__main__":
    # data is ftse100.csv read in using a DictReader
    data = []
    with open("ftse100.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]
    # code is a string value
    code = "III"
    # date is a string formatted 'dd/mm/yyyy'
    date = "14/10/2019"
    
    # Tests
    #print(f"code = {first_row['code']}")
    #print(f"price = {first_row['price']}")
    #print(f"date = {first_row['date']}")
    #print(daily_movement(data, 'ABF', '10/10/2019'))
    #print(daily_high(data, '123', '14/10/2019'))
    #print(daily_low(data, 'ABF', '14/10/2019'))
    #print(daily_avg(data, 'ABF', '17/10/2019'))
    #print(percentage_change(data, 'ABF', '14/10/2019'))
    pass
