import pandas as pd
import numpy as np

data = pd.read_csv(r"D:\lesha\coursera\hse\week1\TestTask\train.csv")

def get_first_name(name):
	return name.split(',')[0]

women = data[data.Sex == 'female']
women_names = women['Name']

names = women_names.str.split(',').to_numpy()

list_names = np.array(women_names)

first_names = []
for names in list_names:
	first_names.append(names.split(',')[0])

print(first_names)



