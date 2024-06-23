# # This entrypoint file to be used in development. Start by reading README.md
# import demographic_data_analyzer
# from unittest import main

# # Test your function by calling it here
# demographic_data_analyzer.calculate_demographic_data()

# # Run unit tests automatically
# main(module='test_module', exit=False)

# ----------------------------------------------------------------------------------------------#

# import pandas as pd


# def calculate_demographic_data(print_data=True):
#     # Read data from file
#     df = None

#     # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
#     race_count = None

#     # What is the average age of men?
#     average_age_men = None

#     # What is the percentage of people who have a Bachelor's degree?
#     percentage_bachelors = None

#     # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
#     # What percentage of people without advanced education make more than 50K?

#     # with and without `Bachelors`, `Masters`, or `Doctorate`
#     higher_education = None
#     lower_education = None

#     # percentage with salary >50K
#     higher_education_rich = None
#     lower_education_rich = None

#     # What is the minimum number of hours a person works per week (hours-per-week feature)?
#     min_work_hours = None

#     # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
#     num_min_workers = None

#     rich_percentage = None

#     # What country has the highest percentage of people that earn >50K?
#     highest_earning_country = None
#     highest_earning_country_percentage = None

#     # Identify the most popular occupation for those who earn >50K in India.
#     top_IN_occupation = None

#     # DO NOT MODIFY BELOW THIS LINE

#     if print_data:
#         print("Number of each race:\n", race_count) 
#         print("Average age of men:", average_age_men)
#         print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
#         print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
#         print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
#         print(f"Min work time: {min_work_hours} hours/week")
#         print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
#         print("Country with highest percentage of rich:", highest_earning_country)
#         print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
#         print("Top occupations in India:", top_IN_occupation)

#     return {
#         'race_count': race_count,
#         'average_age_men': average_age_men,
#         'percentage_bachelors': percentage_bachelors,
#         'higher_education_rich': higher_education_rich,
#         'lower_education_rich': lower_education_rich,
#         'min_work_hours': min_work_hours,
#         'rich_percentage': rich_percentage,
#         'highest_earning_country': highest_earning_country,
#         'highest_earning_country_percentage':
#         highest_earning_country_percentage,
#         'top_IN_occupation': top_IN_occupation
#     }

import pandas as pd

df = pd.read_csv('adult.data.csv')

#race represented
rc = df['race'].value_counts()
print(rc)

#average age of men
sex = df['sex'].value_counts()
men = sex['Male']
mmen = df[df['sex'] == 'Male']['age'].mean()
print(f"{mmen:.2f}")

#percentage Bachelor's degree
Bach = df[df['education']== 'Bachelors'].shape[0]
bachp = (Bach/df['education'].shape[0])*100
print(f"{bachp:.2f}%")

#percentage bach, mas, doc and earn >50K
adv_edu = df[df['education'].isin(['Bachelors','Masters','Doctorate'])& (df['salary'] == '>50K')].shape[0]
gajit = (adv_edu/df['education'].shape[0])*100
print(f"{gajit:.2f}%")

#percentage no bach, mas, doc and earn >50K
biasa = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])& (df['salary'] == '>50K')].shape[0]
gajib = (biasa/df['education'].shape[0])*100
print(f"{gajib:.2f}%")

#min hours per week of a person
hpw = df['hours-per-week'].min()
print(f"{hpw}")

#min hpw work and earn >50K
mhpw = df[df['hours-per-week'] == hpw]
power = mhpw[mhpw['salary'] == '>50K'].shape[0]
sperc = (power/len(mhpw))*100
print(f"{sperc:.2f}%")

#country has the highest percentage that earn >50K
country = df['native-country'].value_counts()
hecountry = df[df['salary'] == '>50K']['native-country'].value_counts()
perc_hecountry = (hecountry/country) * 100
hi_perc_country = perc_hecountry.idxmax()
hi_perc = perc_hecountry.max()
print(hi_perc_country + " with " + f"{hi_perc:.2f}%")

#most popular occupation in India earn >50K
# india_occs = df[df['native-country'].isin(['India'])& (df['salary'] == '>50K')].value_counts()
# india_occ = df[df['native-country'].isin(['India'])& (df['salary'] == '>50K')].shape[0]
india_occu = df[(df['native-country']=='India')& (df['salary'] == '>50K')]
india_occu_data = india_occu.shape[0]
miocc = india_occu['occupation'].value_counts()
maxoccu = miocc.idxmax()
maxoccuno = miocc.max()
# hiindia = india_occs[india_occs['occupation']].value_counts()
print(f"No of 50K earner in India is {india_occu_data} and the occupation is {maxoccu} at {maxoccuno}")
