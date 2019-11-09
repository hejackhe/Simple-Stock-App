import csv

"""
Functions:
    create_portfolio()  ---> creates a stock portfolio from user input
    best_investments()  ---> finds the best x number of investments in a portfolio during a certain period
    worst_investments() ---> finds the worst x number of investments in a portfolio during a certain period
"""

def create_portfolio():
    portfolio = set()
    ftse_codes = set([row['code'] for row in data[0:len(data)]])
    code = input("Enter company code to add to portfolio. Enter EXIT when done: ")
    while code != "EXIT":
        if len(portfolio) >= 100:
            print("Sorry portfolio max reached. Your portfolio has been created")
            return(list(portfolio))
        else:
            if code in ftse_codes:
                portfolio.add(code)
                code = input("Enter another code or enter EXIT to exit: ")
            else:
                code = input("Company not in FTSE. Enter another code or enter EXIT: ")
    else:
        if len(portfolio) >= 1:
            print("Your portfolio has been created")
            return(list(portfolio))
        else:
            print("Portfolio is empty")
            return([])


def best_investments(data, portfolio, x, start_date, end_date):
    if end_date >= start_date and type(x) is int:
        if x >= 1 and x <= len(portfolio):
            returns = []
            for code in portfolio:
                for r in data:
                    if r['code'] == code and r['date'] == start_date and r['time'] == "09:00":
                        start_price = float(r['price'])
                    elif r['code'] == code and r['date'] == end_date and r['time'] == "17:00":
                        end_price = float(r['price'])
                    else:
                        continue
                percent_returns = ((end_price - start_price) / start_price) * 100
                returns.append(dict(code = code, percent_returns = percent_returns))
            ordered_returns = sorted(returns, key=lambda t: t['percent_returns'], reverse=True)
            print("Returning top %d investments in portfolio" % x )
            return([i['code'] for i in ordered_returns[0:x]])
        else:
            print("Error: x must more than 1 and cannot be more than items in portfolio")
            return([])
    else:
        print("Invalid input(s): End date cannot be earlier than start date and x has to be an integer")
        return([])


def worst_investments(data, portfolio, x, start_date, end_date):
    if end_date >= start_date and type(x) is int:
        if x >= 1 and x <= len(portfolio):
            returns = []
            for code in portfolio:
                for r in data:
                    if r['code'] == code and r['date'] == start_date and r['time'] == "09:00":
                        start_price = float(r['price'])
                    elif r['code'] == code and r['date'] == end_date and r['time'] == "17:00":
                        end_price = float(r['price'])
                    else:
                        continue
                percent_returns = ((end_price - start_price) / start_price) * 100
                returns.append(dict(code = code, percent_returns = percent_returns))
            ordered_returns = sorted(returns, key=lambda t: t['percent_returns'])
            print("Returning worst %d investments in portfolio" % x )
            return([i['code'] for i in ordered_returns[0:x]])
        else:
            print("Error: x must more than 1 and cannot be more than items in portfolio")
            return([])
    else:
        print("Invalid input(s): End date cannot be earlier than start date and x has to be an integer")
        return([])


if __name__ == "__main__":
    data = []
    with open("ftse100.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]

    # Tests
    #p = create_portfolio()
    #print(p)
    #print(best_investments(data, p, 3, "14/10/2019", "16/10/2019"))
    #print(worst_investments(data, p, 3, "14/10/2019", "16/10/2019"))
    #print(worst_investments(data, ["AVV", "BARC","BKG", "AV.", "BLND", "BATS"], 3, "14/10/2019", "16/10/2019"))
    pass