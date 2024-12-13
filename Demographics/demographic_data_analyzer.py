import pandas as pd


def calculate_demographic_data(print_data=True):

    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    # average_age_men['average_age_men']

    percentage_bachelors = round(df['education'].value_counts()['Bachelors']/df['education'].value_counts().sum()*100,1)
    # percentage_bachelors['percentage_bachelors']

    adv_edu = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters')| (df['education'] == 'Doctorate')]
    higher_education_rich = round(adv_edu[adv_edu['salary'] == '>50K'].shape[0]/adv_edu.shape[0]*100,1)
    # higher_education_rich['higher_education_rich']

    low_edu = df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]
    lower_education_rich = round(low_edu[low_edu['salary'] == '>50K'].shape[0]/low_edu.shape[0]*100,1)
    # lower_education_rich['lower_education_rich']

    min_work_hours = df['hours-per-week'].min()
    # min_work_hours['min_work_hours']

    min_rich = df[df['hours-per-week'] == 1]
    rich_percentage = int(round(min_rich[min_rich['salary'] == '>50K'].shape[0]/min_rich.shape[0]*100,1))
    # rich_percentage['rich_percentage']

    country_rich = df[df['salary'] == '>50K']
    highest_earning_country = country_rich['native-country'].value_counts().to_frame().idxmax().item()
    # highest_earning_country['highest_earning_country']

    country_rich = df[df['salary'] == '>50K']
    # country_rich['native-country'].value_counts()
    highest_earning_country_percentage = round(country_rich['native-country'].value_counts()['United-States']/country_rich['native-country'].value_counts().sum()*100,1)
    # highest_earning_country_percentage['highest_earning_country_percentage']

    india = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_IN_occupation = india['occupation'].value_counts().to_frame().idxmax().item()
    # top_IN_occupation['top_IN_occupation']

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
