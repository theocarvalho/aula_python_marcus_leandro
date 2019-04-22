
# coding: utf-8

# # Exercício - Theo - Marcus Leandro
# 
# ### Objetivo
# - Resolver exercícios mencionados no link https://stonepgto.slack.com/archives/CHH394R4Z/p1555332079003900
# 
# 
# ### Resumo comando das questões
# 
# 11. Reajuste de salário baseado em condição e apresentação descritiva da relação de nova e antiga informação
# 
# 12. Cálculo descritivo folha de pagamento. Variáveis como desconto e FGTS.
# 
# 13. Conversão número em dia da semana
# 
# 14. Interpretação e status de avaliação dado duas notas

# ## Questão 11.

# In[2]:


11.

# importando algumas bibliotecas que costumo usar
import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

#input usuário
input_monthly_payment = int(input("Qual valor de salário você gostaria de saber informações sobre reajuste? R$") )

#inserção do valor salário
monthly_payment = input_monthly_payment

#condição de reajuste
if monthly_payment <= 280:
  new_monthly_payment = monthly_payment * 1.2
elif monthly_payment < 700:
  new_monthly_payment = monthly_payment * 1.15
elif monthly_payment < 1500:
  new_monthly_payment = monthly_payment * 1.1
else:
    new_monthly_payment = monthly_payment * 1.05

#variacao_absoluta
monthly_payment_delta = new_monthly_payment - monthly_payment

#variacao percentual
monthly_payment_percentage = (monthly_payment_delta/monthly_payment)

#formatando valor. fonte: https://stackoverflow.com/questions/5306756/how-to-show-percentage-in-python
formated_monthly_payment_percentage = '{:.1%}'.format(monthly_payment_percentage)

#formatação da tabela de visualização
d = {'salario_antes_reajuste': [monthly_payment], 'percentual_aumento': [formated_monthly_payment_percentage], 'valor_aumento': [monthly_payment_delta], 'novo_salario': [new_monthly_payment]}
df = pd.DataFrame(data=d)
df.rename(index={0:'Colaborador'}, inplace=True)

#apresentando informação
df


# ## Questão 12.

# In[3]:


12.

# importando algumas bibliotecas que costumo usar
import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

#input usuário
input_money_per_hour_payment = int(input("Qual o valor da sua hora? R$") )
amount_hours = int(input("Qual a quantidade de horas trabalhas no mês? "))

#cálculo do salário dado quantidade de horas e valor por hora
salary = input_money_per_hour_payment * amount_hours

#condição de desconto do IR
if salary <= 900:
  ir_discount_salary = salary * 1.0
elif salary <= 1500:
  ir_discount_salary = salary * 0.05
elif salary <= 2500:
  ir_discount_salary = salary * 1.1
else:
    ir_discount_salary = salary * 0.2

#condição de desconto INSS
inss_discount_salary = salary * 0.1

#contribuição forçada FGTS
fgts_deduction = salary * 0.11

# total de descontos
total_discounts = ir_discount_salary + inss_discount_salary

#salário líquido
net_salary = salary - total_discounts

# detalhe cálculo salário
detailed_salary = "Salário Bruto: ({} * {})".format(amount_hours, input_money_per_hour_payment)

#formatação da tabela de visualização
d = {detailed_salary: [salary], '(-)  IR (5%)': [ir_discount_salary], '(-)  INSS (10%)': [inss_discount_salary],
     'FGTS (11%)': [fgts_deduction], 'Total de descontos': [total_discounts], 'Salário Líquido': [net_salary]}
df = pd.DataFrame(data=d)
df.rename(index={0:''}, inplace=True)

#apresentando informação. Vou realizar transpose apenas para ficar mais semelhante ao exemplo,
#apesar de preferir as variáveis nas colunas
df.transpose()


# ## Questão 13.

# In[5]:


# importando algumas bibliotecas que costumo usar
import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

numero_semana = int(input("Qual o numero da semana? "))

if numero_semana == 1:
    dia_semana = "Domingo"
elif numero_semana == 2:
    dia_semana = "Segunda"
elif numero_semana == 3:
    dia_semana = "Terça"
elif numero_semana == 4:
    dia_semana = "Quarta"
elif numero_semana == 5:
    dia_semana = "Quinta"
elif numero_semana == 6:
    dia_semana = "Sexta"
elif numero_semana == 7:
    dia_semana = "Sabado"
else:
    dia_semana = "valor inválido"

print(dia_semana)


# ## Questão 14.

# In[8]:


# importando algumas bibliotecas que costumo usar
import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

number_grade_1 = round(float(input("Qual foi sua primeira nota parcial do semestre? ")),2)
number_grade_2 = round(float(input("Qual foi sua segunda nota parcial do semestre? ")),2)
name_just_for_fun = input("Qual o seu nome? ")

average = round((number_grade_1 + number_grade_2) / 2,3)

if average <= 4:
    letter_grade = "E"
elif average <= 6:
    letter_grade = "D"
elif average <= 7.5:
    letter_grade = "C"
elif average <= 9:
    letter_grade = "B"
else:
    letter_grade = "A"
    
if letter_grade == "E":
    final_status = "REPROVADO"
elif letter_grade == "D":
    final_status = "REPROVADO"
else:
    final_status = "APROVADO"

d = {"Nota_01": [number_grade_1], 'Nota_02': [number_grade_2], 'Média': [average],
     'Conceito': [letter_grade], 'Status_final': [final_status]}
df = pd.DataFrame(data=d)
df.rename(index={0:name_just_for_fun}, inplace=True)

df.transpose()


# ## Comentários das questões
# 11. Um dos dois exercício mais legais. Erro de português 'contraram' ao invés de 'contrataram'
# 12. Talvez o exercício mais interessante. Comando da questão está super confuso nas primeiras 04 linhas. Achei mal escrito nesse primeiro parágrafo.
# 13. Achei chato. Fiquei curioso para saber outras maneiras de se realizar isso, de forma mais sofisticada, com menor quantidade de 'ifs'
# 14. Divertidinha. Mas bem parecido com as primeiras 02 questões.
