import matplotlib.pyplot as plt
import csv

"""
Functions:
    plot_company()   ---> Plots the price movements of a given stock between a given period
    plot_portfolio() ---> Plots a maximum of 6 given stocks between a given period
"""

def plot_company(data, code, start_date, end_date):
    if end_date > start_date:
        if code in set([row['code'] for row in data]):
            fig, ax = plt.subplots(1, 1, figsize=(20,11))
            x_values = []
            y_values = []
            for row in data:
                if row['code'] == code and row['date'] >= start_date and row['date'] <= end_date:
                    date_time_value = row['date'] + ' ' + row['time']
                    x_values.append(date_time_value)
                    y_values.append(float(row['price']))
                else:
                    continue
            ax.plot(x_values, y_values, label=code)
            plt.title(label='%s' % code)
            plt.tick_params(axis='x', labelsize=5, labelrotation=90)
            plt.xlabel('From %s 9AM to %s 5PM' % (start_date, end_date))
            plt.ylabel('GBX')
            fig.legend([code], loc='center right', title="Legend")
            plt.savefig('plot1.png')
        else:
            print("Error: Company code does not exist")
    else:
        print("Error: Start date cannot be after end date")


def plot_portfolio(data, portfolio, start_date, end_date):
    if end_date > start_date:
        fig = plt.figure(figsize=(15,25), dpi=180)
        line_colors = ["red", "blue", "green", "orange", "cyan", "violet"]
        if len(portfolio) > 6:
            print("Showing a maximum of 6 graphs")
            portfolio = portfolio[0:6]
        else:
            pass
        i = 1
        for code in portfolio:
            x_values = []
            y_values = []
            plt.subplot(6,1,i)
            plt.subplots_adjust(hspace=0.8)
            for row in data:
                if row['code'] == code and row['date'] >= start_date and row['date'] <= end_date:
                    date_time_value = row['date'] + ' ' + row['time']
                    x_values.append(date_time_value)
                    y_values.append(float(row['price']))
                else:
                    continue
            plt.plot(x_values, y_values, label=code, color=line_colors[i-1])
            plt.title(label='%s' % code)
            plt.tick_params(axis='x', labelsize=5, labelrotation=90)
            plt.xlabel('%s - %s' % (start_date, end_date))
            plt.ylabel('GBX')
            i += 1
        fig.legend(portfolio, loc='center right', title="Legend")
        plt.savefig('plot2.png')
    else:
        print("Error: Start date cannot be after end date")
    

if __name__ == "__main__":
    data = []
    with open("ftse100.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]
    # Tests
    #portfolio = ['BHP', 'III', 'AVV', 'BA.', 'BARC', 'BNZL', 'BATS', 'CPG']
    #plot_company(data, 'AVV', '14/10/2019', '18/10/2019')
    #plot_portfolio(data, portfolio, '14/10/2019', '18/10/2019')
    pass