import pandas as pd

def calculate_demographic_data(print_data=True):
    
    df = pd.read_csv('adult.data.csv')  
    print(df.head())  # Exibe as primeiras linhas do DataFrame

    race_count = df['race'].value_counts()  # Conta as ocorrências de cada raça

    man = df[df['sex'] == 'Male']  
    average_age_men = round(man['age'].mean(), 1)  # Calcula a idade média dos homens

    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)  # Percentual de pessoas com bacharelado

    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]  
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]  

    higher_education_rich = round((higher_education['salary'] == '>50K').sum() * 100 / len(higher_education), 1)  
    lower_education_rich = round((lower_education['salary'] == '>50K').sum() * 100 / len(lower_education), 1)  

    min_work_hours = df['hours-per-week'].min()  # Menor número de horas trabalhadas por semana

    num_min_workers = df[df['hours-per-week'] == min_work_hours]  
    rich_percentage = round((num_min_workers['salary'] == '>50K').sum() * 100 / len(num_min_workers), 1)  # Percentual que ganha >50K

    highest_earning_country_values = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)  
    highest_earning_country = highest_earning_country_values.idxmax()  
    highest_earning_country_percentage = round(highest_earning_country_values.max(), 1)  

    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')].groupby('occupation').size().idxmax()  
    # Ocupação mais comum na Índia para quem ganha >50K

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
