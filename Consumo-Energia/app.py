#Programa de cálculo de consumo de energia
#Ronaldo da Silva Prado
#Tecnico de Desenvolvimento de Sistemas - Etec CPS

#Entrada de dados

nomeAparelho = input("Nome do aparelho: ")
potencia = int(input("Potência do equipamento em Watts(W): "))
horasDia = int(input("Tempo médio de uso diário em horas(h): "))
valorKWh = float(0.75)

#Processamento

consumoMensal = (potencia * horasDia * 30) / 1000
consumoDinheiro = float(consumoMensal * valorKWh)

#Resultado

print(f"O consumo mensal do equipamento {nomeAparelho}")
print(f"tem o consumo mensal de energia estimado em {consumoMensal}kW/h por mês")
print(f"o valor estimado do consumo será de R${consumoDinheiro:.2f}, sendo R$",valorKWh,"o preço do kW/h.")