# Cryptocurrency project  
**get_data.py** - takes 1 parameter(int)  
-downloads data from [https://coinmarketcap.com](https://coinmarketcap.com/all/views/all/) every x minutes where x is first parameter, then saves it to csv files
**compare_data.py** takes 2 parameters(names of cryptocurrencies)
-calculates correlation coefficient and writes it to console
-contains some functions for price_graph.py  
**price_graph.py** takes 1 parameter(name of cryptocurrency)  
-shows matplotlib graph of price changes of cryptocurrency
-writes standard deviation to console
**data** directory contains some saved csv files with cryptocurrency data(cryptocurrency name, cryptocurrency symbol, price, market cap)
