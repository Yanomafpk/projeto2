import pandas as pd

def calculate_demographic_data(print_data=True):
    # Carrega os dados do arquivo CSV
    dados = pd.read_csv('adult.data.csv')

    # Exibe as primeiras linhas se solicitado
    if print_data:
        print(dados.head())

    # Contagem de cada raça no dataset
    contagem_raca = dados['race'].value_counts()
    
    # Calcula a idade média dos homens
    homens = dados[dados['sex'] == 'Male']
    media_idade_homens = round(homens['age'].mean(), 1)
    
    # Percentual de pessoas com grau de bacharelado
    percentual_bacharelado = round((dados['education'] == 'Bachelors').mean() * 100, 1)

    # Separa pessoas com e sem educação superior (Bacharelado, Mestrado, Doutorado)
    educacao_superior = dados[dados['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    educacao_inferior = dados[~dados['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Percentual de pessoas com educação superior que ganham >50K
    ricos_educacao_superior = round((educacao_superior['salary'] == '>50K').sum() * 100 / len(educacao_superior), 1)
    # Percentual de pessoas sem educação superior que ganham >50K
    ricos_educacao_inferior = round((educacao_inferior['salary'] == '>50K').sum() * 100 / len(educacao_inferior), 1)

    # Mínimo de horas trabalhadas por semana
    horas_minimas_trabalho = dados['hours-per-week'].min()

    # Percentual de pessoas que trabalham o mínimo de horas por semana e ganham >50K
    trabalhadores_horas_minimas = dados[dados['hours-per-week'] == horas_minimas_trabalho]
    percentual_ricos_horas_minimas = round((trabalhadores_horas_minimas['salary'] == '>50K').sum() * 100 / len(trabalhadores_horas_minimas), 1)

    # País com maior percentual de pessoas que ganham >50K
    pais_maior_percentual_rico = dados.groupby(by=['native-country'])['salary'].apply(lambda x: (x == '>50K').mean() * 100)
    pais_mais_rico = pais_maior_percentual_rico.idxmax()
    percentual_pais_mais_rico = round(pais_maior_percentual_rico.max(), 1)

    # Ocupação mais comum entre os ricos (>50K) na Índia
    ocupacao_top_india = dados[(dados['native-country'] == 'India') & (dados['salary'] == '>50K')].groupby('occupation').size().idxmax()

    # Se solicitado, imprime os dados
    if print_data:
        print("Number of each race:\n", contagem_raca) 
        print("Average age of men:", media_idade_homens)
        print(f"Percentage with Bachelors degrees: {percentual_bacharelado}%")
        print(f"Percentage with higher education that earn >50K: {ricos_educacao_superior}%")
        print(f"Percentage without higher education that earn >50K: {ricos_educacao_inferior}%")
        print(f"Min work time: {horas_minimas_trabalho} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {percentual_ricos_horas_minimas}%")
        print("Country with highest percentage of rich:", pais_mais_rico)
        print(f"Highest percentage of rich people in country: {percentual_pais_mais_rico}%")
        print("Top occupations in India:", ocupacao_top_india)

    # Retorna os dados calculados
    return {
        'race_count': contagem_raca,
        'average_age_men': media_idade_homens,
        'percentage_bachelors': percentual_bacharelado,
        'higher_education_rich': ricos_educacao_superior,
        'lower_education_rich': ricos_educacao_inferior,
        'min_work_hours': horas_minimas_trabalho,
        'rich_percentage': percentual_ricos_horas_minimas,
        'highest_earning_country': pais_mais_rico,
        'highest_earning_country_percentage': percentual_pais_mais_rico,
        'top_IN_occupation': ocupacao_top_india
    }
