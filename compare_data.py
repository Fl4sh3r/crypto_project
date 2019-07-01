import os
import csv
import time
import statistics

path = 'data/'

# files_list = []
# i = -1
# files = len(os.listdir(path))
#
# # from all saved files saves data to list
# for filename in os.listdir(path):
#     if filename.endswith('.txt'):
#         file_time = float(os.path.getmtime(path+filename))
#         valid_time = ((time.time() - file_time) / (3600 * 24))  # how old is file in days
#         # if file isn't older than 7 days
#         if valid_time <= 7:
#             i += 1
#             files_list.append([])
#             with open(path+filename, mode='r', newline='') as f:
#                 reader = csv.DictReader(f)
#                 for row in reader:
#                     files_list[i].append({'name': row['name'], 'symbol': row['symbol'], 'price': row['price'],
#                                           'market cap': row['market cap']})
#
# list_of_files = {}
# for k in files_list[0]:
#     list_of_files[k] = tuple(list_of_files[k] for list_of_files in test_list)


def dict_all_data():
    crypto_currencies = {}
    for file in os.listdir(path):
        if file.endswith('.txt'):
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
                            crypto_currencies[symbol] = {'Name': name, 'Price (USD)': [price],
                                                         'Market Cap (USD)': [market_cap]}
    return crypto_currencies


# {
#     'BTC': {'Name': 'Bitcoin', 'Price (USD)': [11084.13], 'Market Cap (USD)': [197198912240]},
#     'LTC': {...},
#     ...
# }

# gets stats max,min,avg of cryptocurrencies
def crypto_stats():
    dict_prices = {}
    for key in crypto_currency.keys():
        max_price = float(max(crypto_currency[key]['Price (USD)']))
        min_price = float(min(crypto_currency[key]['Price (USD)']))

        x = 0
        for i in crypto_currency[key]['Price (USD)']:
            x += float(i)
        avg_price = x / len(crypto_currency[key]['Price (USD)'])
        dict_prices[key] = {'Name': crypto_currency[key]['Name'], 'Max Price': max_price,
                            'Min Price': min_price, 'Average Price': avg_price}

    return dict_prices


if __name__ == '__main__':
    crypto_currency = dict_all_data()




    crypto_stats()
