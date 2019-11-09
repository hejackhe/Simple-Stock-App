import matplotlib.pyplot as plt
import csv

"""
Classes:
    Company()              ---> Creates a company class
Functions:
    predict_next_average() ---> Takes in a company class and predicts the average price in the next period using hard-coded linear regression
    classify_trend()       ---> Takes in a company class and classifies whether the trend is "Volatile", "Increasing", "Decreasing" or "Other"
"""

class Company:
    #Instance variables
    def __init__(self, code, name, currency, data):
        self.code = code
        self.name = name
        self.currency = currency
        self.data = [row for row in data if (row['code']==code and row['name']==name and row['currency']==currency)]
    #Functions
    def daily_movement(self, date):
        if date in [row['date'] for row in self.data]:
            dailyPrices = [float(row['price']) for row in self.data if row['date']==date]
            return(round(dailyPrices[-1] - dailyPrices[0], 2))
        else:
            return("Error: Data for selected date not available, try another date.")
    def daily_high(self, date):
        if date in [row['date'] for row in self.data]:
            dailyPrices = [float(row['price']) for row in self.data if row['date']==date]
            return(round(max(dailyPrices), 2))
        else:
            return("Error: Data for selected date not available, try another date.")
    def daily_low(self, date):
        if date in [row['date'] for row in self.data]:
            dailyPrices = [float(row['price']) for row in self.data if row['date']==date]
            return(round(min(dailyPrices), 2))
        else:
            return("Error: Data for selected date not available, try another date.")
    def daily_avg(self, date):
        if date in [row['date'] for row in self.data]:
            dailyPrices = [float(row['price']) for row in self.data if row['date']==date]
            return(round(sum(dailyPrices) / len(dailyPrices), 2))
        else:
            return("Error: Data for selected date not available, try another date.")
    def percentage_change(self, date):
        if date in [row['date'] for row in self.data]:
            dailyPrices = [float(row['price']) for row in self.data if row['date']==date]
            pc_change = round(((dailyPrices[-1] - dailyPrices[0]) / dailyPrices[0]) * 100, 2)
            return(pc_change)
        else:
            return("Error: Data for selected date not available, try another date.")
    pass


def predict_next_average(company):
    dates = sorted(set([row['date'] for row in company.data if row['code'] == company.code]))
    daily_avgs = [company.daily_avg(date) for date in dates]
    x_bar = sum(range(len(dates))) / len(dates)
    y_bar = sum(daily_avgs) / len(daily_avgs)
    m_numerators = [(i-x_bar)*(daily_avgs[i]-y_bar) for i in range(len(dates))]
    m_denominators = [(i-x_bar)**2 for i in range(len(dates))]
    m = sum(m_numerators) / sum(m_denominators)
    b = y_bar - m*x_bar
    return(round(m*(len(dates)) + b, 2)) # Use len() because it returns the next index after the end of range(0, len())


def classify_trend(company):
    dates = sorted(set([row['date'] for row in company.data if row['code'] == company.code]))
    daily_highs = [company.daily_high(date) for date in dates]
    daily_lows = [company.daily_low(date) for date in dates]
    x_bar = sum(range(len(dates))) / len(dates)
    high_y_bar , low_y_bar = sum(daily_highs) / len(daily_highs) , sum(daily_lows) / len(daily_lows)
    high_m_numerators = [((i-x_bar)*(daily_highs[i]-high_y_bar)) for i in range(len(dates))]
    low_m_numerators = [((i-x_bar)*(daily_lows[i]-low_y_bar)) for i in range(len(dates))]
    m_denominators = [((i-x_bar)**2) for i in range(len(dates))]
    high_m, low_m = (sum(high_m_numerators) / sum(m_denominators)), (sum(low_m_numerators) / sum(m_denominators))
    high_b, low_b = (high_y_bar - high_m*x_bar), (low_y_bar - low_m*x_bar)
    next_high, next_low = (high_m*(len(dates)) + high_b), (low_m*(len(dates)) + low_b)
    if next_high > daily_highs[-1] and next_low < daily_lows[-1]:
        return("Volatile")
    elif next_high > daily_highs[-1] and next_low > daily_lows[-1]:
        return("Increasing")
    elif next_high < daily_highs[-1] and next_low < daily_lows[-1]:
        return("Decreasing")
    else:
        return("Other")


if __name__ == "__main__":
    data = []
    with open("ftse100.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]
    # Tests
    #iii = Company('III', '3I GRP.', 'GBX', data)
    #avv = Company('AVV', 'AVEVA GRP', 'GBX', data)
    #cpg = Company('CPG', 'COMPASS GROUP', 'GBX', data)
    #print(avv.data[5])
    #print(avv.daily_movement('14/10/2019'))
    #print(avv.daily_high('14/10/2019'))
    #print(avv.daily_low('14/10/2019'))
    #print(avv.daily_avg('14/10/2019'))
    #print(avv.percentage_change('14/10/2019'))
    #print(predict_next_average(iii))
    #print(predict_next_average(cpg))
    #print(cpg.daily_low('18/10/2019'))
    #print(classify_trend(cpg))
    pass