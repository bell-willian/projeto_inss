name = input('Qual seu nome? ')
age = input('Qual sua idade? ')
try:
    #Aqui eu tratei os possiveis erros que seria a pessoa não digitar um numero valido de idade e ja fiz as contas pra saber qual ano ela poderia se aposentar
    age_int = int(age)
    age_minus_retirement = 65 - age_int
    year_retire = age_minus_retirement + 2024
    if age_int < 65:
        print(f'Olá senhor {name}, você podera se aposentar no ano de {year_retire}')
    else:
        print('Você já pode se aposentar')
except:
    print('Digite uma idade valida.')

sair= input('Pressione enter para sair.')