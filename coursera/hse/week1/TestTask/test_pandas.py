import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\Lenovo\Desktop\lesha\ML\coursera\hse\week1\TestTask\train.csv")

def get_first_name(name):
	return name.split(',')[0]

women = data[data.Sex == 'female']
women_names = women['Name']

names = women_names.str.split(',').to_numpy()

list_names = np.array(women_names)

first_names = []
for names in list_names:
	first_names.append(names.split(',')[0])

new_data = pd.DataFrame({'First_Names': first_names})

print(new_data.First_Names.value_counts())



