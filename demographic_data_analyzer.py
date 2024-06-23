import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    print(rc)

    # What is the average age of men?
    sex = df['sex'].value_counts()
    men = sex['Male']
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    print(f"{average_age_men:.2f}")

    # What is the percentage of people who have a Bachelor's degree?
    Bach = df[df['education']== 'Bachelors'].shape[0]
    percentage_bachelors = (Bach/df['education'].shape[0])*100
    print(f"{percentage_bachelors:.2f}%")

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    adv_edu = df[df['education'].isin(['Bachelors','Masters','Doctorate'])& (df['salary'] == '>50K')].shape[0]
    higher_education_rich = (adv_edu/df['education'].shape[0])*100
    print(f"{higher_education_rich:.2f}%")
    
    # What percentage of people without advanced education make more than 50K?
    biasa = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])& (df['salary'] == '>50K')].shape[0]
    lower_education_rich = (biasa/df['education'].shape[0])*100
    print(f"{lower_education_rich:.2f}%")
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    adv_edu = df[df['education'].isin(['Bachelors','Masters','Doctorate'])& (df['salary'] == '>50K')].shape[0]
    higher_education_rich = (adv_edu/df['education'].shape[0])*100
    print(f"{higher_education_rich:.2f}%")
    
    biasa = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])& (df['salary'] == '>50K')].shape[0]
    lower_education_rich = (biasa/df['education'].shape[0])*100
    print(f"{lower_education_rich:.2f}%")

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    print(f"{min_work_hours}")

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mhpw = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = mhpw[mhpw['salary'] == '>50K'].shape[0]
    rich_percentage = (num_min_workers/len(mhpw))*100
    print(f"{rich_percentage:.2f}%")

    # What country has the highest percentage of people that earn >50K?
    country = df['native-country'].value_counts()
    highest_earning_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country_percentage = (highest_earning_country/country) * 100
    hi_perc_country = highest_earning_country_percentage.idxmax()
    hi_perc = highest_earning_country_percentage.max()
    print(hi_perc_country + " with " + f"{hi_perc:.2f}%")

    # Identify the most popular occupation for those who earn >50K in India.
    india_occu = df[(df['native-country']=='India')& (df['salary'] == '>50K')]
    india_occu_data = india_occu.shape[0]
    top_IN_occupation = india_occu['occupation'].value_counts()
    maxoccu = top_IN_occupation.idxmax()
    maxoccuno = top_IN_occupation.max()
    print(f"No of 50K earner in India is {india_occu_data} and the occupation is {maxoccu} at {maxoccuno}")

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
