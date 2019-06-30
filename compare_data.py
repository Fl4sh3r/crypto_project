import os
import csv
import time

path = 'data/'
final_list = []
i = -1
files = len(os.listdir(path))

# from all saved files saves data to list
for filename in os.listdir(path):
    if filename.endswith('.txt'):
        file_time = float(os.path.getmtime(path+filename))
        valid_time = ((time.time() - file_time) / (3600 * 24))  # how old is file in days
        # if file isn't older than 7 days
        if valid_time <= 7:
            i += 1
            final_list.append([])
            with open(path+filename, mode='r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    final_list[i].append({'name': row['name'], 'symbol': row['symbol'], 'price': row['price'],
                                          'market cap': row['market cap']})

list_of_files = []
for i in range(len(final_list)):
    list_of_files.append([])
    for data in final_list[i]:
        print(data)
        for data2 in list_of_files[i]:
            if data['name'] in data2:
                print('ahoj')
        list_of_files[i].append({'name': [data['name']], 'price': [data['price']]})

