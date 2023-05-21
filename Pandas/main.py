# with open('weather_data.csv', mode='r') as file:
#     data = file.readlines()
# print(data)

# import csv
# with open('weather_data.csv', mode='r') as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
# print(temperature)

import pandas

data = pandas.read_csv('weather_data.csv')
print(data)
print()

monday = data[data.day == 'Monday']
print(monday)
temp = data.temp
print(temp.max())
#
# data of row:
# monday = data[data.day == 'Monday']
# print((monday.temp * 9/5) + 32)
# print(data[data.temp == temp.max()])

#creating dataframe:

# data_dict = {
#     'students':["Laura", 'Jorge', 'Reginaldo'],
#     'score':[10, 2, 7]
# }
#
# data_ = pandas.DataFrame(data_dict)
# print(data_)
#
# data_.to_csv('data_')