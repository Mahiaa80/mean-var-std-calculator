import pandas as pd
file_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 
                'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
                'hours-per-week', 'native-country', 'salary']
data = pd.read_csv(file_path, names=column_names, sep=',\s', na_values=" ?", engine='python')
race_counts = data['race'].value_counts()
average_age_men = data[data['sex'] == 'Male']['age'].mean()
bachelors_percentage = (data['education'] == 'Bachelors').mean() * 100
advanced_education = data[(data['education'] == 'Bachelors') | (data['education'] == 'Masters') | (data['education'] == 'Doctorate')]
percentage_50k_advanced = (advanced_education['salary'] == '>50K').mean() * 100
non_advanced_education = data[~((data['education'] == 'Bachelors') | (data['education'] == 'Masters') | (data['education'] == 'Doctorate'))]
percentage_50k_non_advanced = (non_advanced_education['salary'] == '>50K').mean() * 100
min_hours_per_week = data['hours-per-week'].min()
percentage_50k_min_hours = (data[(data['hours-per-week'] == min_hours_per_week) & (data['salary'] == '>50K')].shape[0] / data[data['hours-per-week'] == min_hours_per_week].shape[0]) * 100
country_50k = data[data['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100
country_50k_max = country_50k.idxmax()
percentage_50k_country_max = country_50k[country_50k_max]
india_50k = data[(data['salary'] == '>50K') & (data['native-country'] == 'India')]
most_popular_occupation_in_india = india_50k['occupation'].value_counts().idxmax()
race_counts = race_counts.round(1)
average_age_men = round(average_age_men, 1)
bachelors_percentage = round(bachelors_percentage, 1)
percentage_50k_advanced = round(percentage_50k_advanced, 1)
percentage_50k_non_advanced = round(percentage_50k_non_advanced, 1)
percentage_50k_min_hours = round(percentage_50k_min_hours, 1)
percentage_50k_country_max = round(percentage_50k_country_max, 1)

print(race_counts)
print(average_age_men)
print(bachelors_percentage)
print(percentage_50k_advanced)
print(percentage_50k_non_advanced)
print(min_hours_per_week)
print(percentage_50k_min_hours)
print(f"{country_50k_max}: {percentage_50k_country_max}")
print(most_popular_occupation_in_india)
