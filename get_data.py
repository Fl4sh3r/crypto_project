from urllib import request
import os, errno
import datetime

class GetData:
    def __init__(self, url_add, data_folder):
        self.url_add = url_add
        self.f_name = ''
        self.lines = 0
        self.crypto_number = 0
        self.crypto_name = []
        self.crypto_symbol = []
        self.crypto_supply = []
        self.crypto_price_all = []
        self.final_list = []
        self.crypto_price = []
        self.data_folder = data_folder

    def save_file(self):
        # creates directory if not exists
        try:
            os.makedirs('data')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        # gets current time
        time = datetime.datetime.now()
        time = str(time)[:19]
        time = time.replace(' ', '_')
        time = time.replace(':', '-')
        self.f_name = self.data_folder + str(time) + '.txt'
        # saves html code to file
        url = request.urlopen(self.url_add)
        html = url.read()
        html_decoded = html.decode("UTF-8")
        with open(self.f_name, "w", encoding="utf-8") as f:
            f.write(html_decoded)
        f.close()

    def find_line(self):  # finds useful lines and saves data to lists
        with open(self.f_name, 'r', encoding='utf-8') as f:
            word = '<td class="no-wrap currency-name" data-sort='  # name of cryptocurrency
            word2 = '<td class="text-left col-symbol">'  # symbol of crypto
            word3 = '<span data-supply="'  # crypto supplies
            word4 = '<td class="no-wrap market-cap text-right" data-usd="'  # price per all
            for line in f:
                self.lines += 1
                if word in line:  # finds and saves all crypto names
                    self.crypto_number += 1  # counts number of cryptocurrencies
                    # removes html tags
                    line = line.replace('<td class="no-wrap currency-name" data-sort="', '')
                    line = line.replace('">', '')
                    line = line.replace('\n', '')
                    self.crypto_name.append(line)

        # saves all crypto prices
        with open(self.f_name, 'r', encoding='utf-8') as f:
            for line in f:
                if word4 in line:  # finds and saves all crypto prices
                    # remove html tags
                    line = line.replace('<td class="no-wrap market-cap text-right" data-usd="', '')
                    line = line.partition('"')[0]
                    line = line.replace('\n', '')
                    self.crypto_price_all.append(line)
        # saves all crypto symbols to list crypto_symbol
        with open(self.f_name, 'r', encoding='utf-8') as f:
            for line in f:
                if word2 in line:  # finds and saves all crypto symbols
                    # removes html tags
                    line = line.replace('<td class="text-left col-symbol">', '')
                    line = line.replace('</td>', '')
                    line = line.replace('\n', '')
                    self.crypto_symbol.append(line)
        # saves all crypto supplies to list crypto_supply
        with open(self.f_name, 'r', encoding='utf-8') as f:
            for line in f:
                if word3 in line:  # finds and saves all crypto supplies
                    # removes html tags
                    line = line.replace('<span data-supply="', '')
                    line = line.partition('"')[0]
                    line = line.replace('\n', '')
                    self.crypto_supply.append(line)

    # saves all data of every cryptocurrency into list
    def data_to_list(self):
        for i in range(self.crypto_number):
            # if price is known, gets price of of one token (total_price/total_supply)
            if '?' in self.crypto_price_all[i]:
                self.crypto_price.append('?')
            else:
                self.crypto_price.append(float(self.crypto_price_all[i]) / float(self.crypto_supply[i]))
            #  creates list with all data (ID,crypto_name,symbol,price,total_supply,total_price)
            text_all = str(i+1) + ' | ' + self.crypto_name[i] + ' | ' + self.crypto_symbol[i] + ' | '
            text_all += str(self.crypto_price[i]) + ' | ' + self.crypto_supply[i] + ' | '
            text_all += self.crypto_price_all[i]
            self.final_list.append(text_all)
