import os
import csv
import time
import math
import sys

path = 'data/'


# create dictionary from all files, cryptocurrencies have list of prices and market cap
def dict_all_data():
    crypto_currencies = {}
    for file in os.listdir(path):
        if file.endswith('.txt'):
            file_time = float(os.path.getmtime(path + file))
            valid_time = ((time.time() - file_time) / (3600 * 24))  # how old is file in days
            # if file isn't older than 7 days
            if valid_time <= 7:
                with open(path + file, mode='r') as input_file:
                    # Skip the first line of the csv file
                    next(input_file)
                    csv_reader = csv.reader(input_file)
                    for row in csv_reader:
                        if len(row) == 4:
                            name, symbol, price, market_cap = row
                            if symbol in crypto_currencies.keys():
                                crypto_currencies[symbol]['Price (USD)'].append(price)
                                crypto_currencies[symbol]['Market Cap (USD)'].append(market_cap)
                            else:
                                crypto_currencies[symbol] = {'Name': name.lower(), 'Price (USD)': [price],
                                                             'Market Cap (USD)': [market_cap]}
    return crypto_currencies


# gets stats max,min,avg of cryptocurrencies
def crypto_stats():
    dict_name = dict_all_data()
    dict_prices = {}
    for key in dict_name.keys():
        max_price = float(max(dict_name[key]['Price (USD)']))
        min_price = float(min(dict_name[key]['Price (USD)']))

        x = 0
        for i in dict_name[key]['Price (USD)']:
            x += float(i)
        avg_price = x / len(dict_name[key]['Price (USD)'])
        dict_prices[key] = {'Name': dict_name[key]['Name'], 'Max Price': max_price,
                            'Min Price': min_price, 'Average Price': avg_price}

    return dict_prices


def average_price(crypto_name):
    crypto_currencies = dict_all_data()
    for line in crypto_currencies.items():
        if line[1]['Name'] == crypto_name:
            x = 0
            for number in line[1]['Price (USD)']:
                x += float(number)

            avg_price = x / len(line[1]['Price (USD)'])
            return avg_price


def standard_deviation(crypto_name):
    crypto_name = crypto_name.lower()  # every letter lowercase
    dict_name = dict_all_data()
    for line in dict_name.items():
        if line[1]['Name'] == crypto_name:
            prices_length = (len(line[1]['Price (USD)']))
            avg_price = average_price(crypto_name)
            answer = 0
            for i in line[1]['Price (USD)']:

                answer += ((float(i)-avg_price)**2)
            answer = (1/prices_length)*answer
            answer = math.sqrt(answer)
            return answer


def correlation_coefficient(crypto_name, crypto_name2):
    crypto_name = crypto_name.lower()
    crypto_name2 = crypto_name2.lower()
    dict_name = dict_all_data()

    deviation = []
    deviation2 = []
    avg_price = average_price(crypto_name)
    avg_price2 = average_price(crypto_name2)
    sum_dev = 0
    sum_dev2 = 0
    sum_total = 0
    sum_total2 = 0

    for line in dict_name.items():
        if line[1]['Name'] == crypto_name:
            for n in line[1]['Price (USD)']:
                deviation.append(float(n)-avg_price)
                sum_dev += float(n)
                sum_total += (float(n)-avg_price)**2

        if line[1]['Name'] == crypto_name2:
            for n in line[1]['Price (USD)']:
                deviation2.append(float(n)-avg_price2)
                sum_dev2 += float(n)
                sum_total2 += (float(n) - avg_price2) ** 2

    deviation_multi = 0
    for i in range(len(deviation)):
        deviation_multi += (deviation[i]*deviation2[i])

    corr_coe = deviation_multi / (math.sqrt(sum_total*sum_total2))
    return corr_coe


correlation_coefficient('bitcoin', 'ethereum')


# get dates of all files
def get_file_dates():
    list_of_dates = []
    for file in os.listdir(path):
        file = file[5:]
        file = file[:11]
        file = file[0:-3] + ':' + file[-2:]
        file = file.replace(' ', '\n')
        list_of_dates.append(file)
    return list_of_dates


if __name__ == '__main__':
    try:
        param = sys.argv[1]
        param2 = sys.argv[2]
        print('correlation coefficient: ', correlation_coefficient(param, param2))
    except ValueError:
        print('wrong parameter')
    except IndexError:
        print('2 parameters needed')
