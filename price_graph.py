import matplotlib.pyplot as plt
import compare_data
import sys

plt.rcParams.update({'font.size': 9})


# get list of prices of one cryptocurrency
def get_prices(crypto_name):
    crypto_name = crypto_name.lower()
    for line in crypto_currencies.items():
        if line[1]['Name'] == crypto_name:
            crypto_price = []
            for qwe in line[1]['Price (USD)']:
                crypto_price.append(float(qwe))
            return crypto_price


def show_graph(crypto_name):
    crypto_name = crypto_name.lower()  # every letter lowercase
    dates = compare_data.get_file_dates()  # saves file dates to list
    crypto_prices = get_prices(crypto_name)  # saves all prices of one cryptocurrency

    # change window title
    fig = plt.gcf()
    fig.canvas.set_window_title(crypto_name)
    plt.plot(dates, crypto_prices)  # insert data into graph
    plt.axis([0, len(crypto_prices), min(crypto_prices) * 0.98, max(crypto_prices) * 1.02])  # set axis of graph
    plt.xlabel("price date")
    plt.ylabel("Price (USD)")
    plt.title(crypto_name.capitalize())
    plt.show()


if __name__ == '__main__':
    try:
        param = sys.argv[1]
        crypto_currencies = compare_data.dict_all_data()
        print('standard deviation: ', compare_data.standard_deviation(param))
        # print('correlation coefficient: ', compare_data.correlation_coefficient(param, param2))
        show_graph(param)
    except ValueError:
        print('wrong parameter')
