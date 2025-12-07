import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data", header=None, names=[
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race",
        "sex", "capital-gain", "capital-loss", "hours-per-week",
        "native-country", "salary"
    ])

    # Fix extra spaces (very important)
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # 1. Number of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelors
    percentage_bachelors = round(
        (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1
    )

    # 4. Higher education
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # >50K among higher education
    higher_education_rich = round(
        (
            higher_education[higher_education['salary'] == '>50K'].shape[0] /
            higher_education.shape[0]
        ) * 100,
        1
    )

    # 5. Lower education
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # >50K among lower education
    lower_education_rich = round(
        (
            lower_education[lower_education['salary'] == '>50K'].shape[0] /
            lower_education.shape[0]
        ) * 100,
        1
    )

    # 6. Minimum hours per week
    min_work_hours = df['hours-per-week'].min()

    # 7. % of rich among those who work min hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']

    rich_percentage = round(
        (rich_min_workers.shape[0] / min_workers.shape[0]) * 100,
        1
    )

    # 8. Country with highest % of >50K earners
    country_total = df['native-country'].value_counts()
    country_rich = df[df['salary'] == '>50K']['native-country'].value_counts()

    country_rich_percentage = (country_rich / country_total) * 100

    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # 9. Most popular occupation in India for >50K earners
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # Printing section
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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

if __name__ == "__main__":
    calculate_demographic_data()
