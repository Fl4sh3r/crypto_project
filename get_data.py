import errno
import os
import requests
import datetime
from bs4 import BeautifulSoup
import csv
import time


def get_data():
    # url request, soup
    url = 'https://coinmarketcap.com/all/views/all/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # gets symbol of cryptocurrencies
    data_symbol = []
    for symbol in soup.find_all('td', class_='col-symbol'):
        data_symbol.append(symbol.text)

    # gets name of cryptocurrencies
    data_name = []
    for name in soup.find_all('a', class_='currency-name-container'):
        data_name.append(name.text)

    # gets price of cryptocurrencies
    data_price = []
    for price in soup.find_all('a', class_='price'):
        price = price.text
        price = price.replace('$', '')
        price = float(price)
        data_price.append(price)

    # gets market cap of cryptocurrencies
    data_price_total = []
    for price_total in soup.find_all('td', class_='market-cap'):
        price_total = price_total.text
        price_total = price_total.replace('\n', '')
        price_total = price_total.replace(',', ' ')
        data_price_total.append(price_total)

    # creates final list of all data
    final_list = []
    for i in range(len(data_symbol)):
        final_list.append({'name': data_name[i], 'symbol': data_symbol[i], 'price': data_price[i],
                           'market cap': data_price_total[i]})

    # gets current time and creates csv file name
    time_now = datetime.datetime.now()
    time_now = str(time_now)[:19]
    time_now = time_now.replace(':', '-')
    f_name = str(time_now) + '.txt'

    # create dir if not exists
    dir_name = 'data'
    try:
        os.makedirs(dir_name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    # saves list of all crypto to csv file
    with open(dir_name + '/' + f_name, mode='w') as f:
        fields = ['name', 'symbol', 'price', 'market cap']
        write = csv.DictWriter(f, quoting=csv.QUOTE_ALL, fieldnames=fields)
        write.writeheader()
        write.writerows(final_list)


# function that runs every hour
def do_every_hour():
    start_time = time.time()
    while True:
        print('adding... ', datetime.datetime.now())
        get_data()
        print('added ', datetime.datetime.now())
        time.sleep(3600.0 - ((time.time() - start_time) % 3600.0))


do_every_hour()