import pandas

data = pandas.read_csv('squirel_data.csv')
grey = len(data[data['Primary Fur Color'] == 'Gray'])
black = len(data[data['Primary Fur Color'] == 'Black'])
cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])

new_data = {
    'Fur Color':['grey', 'black', 'cinnamon'],
    'Count': [grey, black, cinnamon]
}

new_pandas = pandas.DataFrame(new_data)
print(new_pandas)

new_pandas.to_csv('Squirel_color_count')