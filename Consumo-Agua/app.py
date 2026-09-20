#Ronaldo da Silva Prado
#TDS, turma FML

#Programa ambiental de água e classificacao de consumidor

#Entrada de dados

print("Bem-vindo ao programa ambiental de conscientização de consumo de água!")
tipo_imovel = int(input("Informe o tipo de imóvel( 1 - comercial, 2 - casa, 3 - apartamento ): "))
consumo_mensal = int(input("Informe o consumo mensal de água em metros cúbicos (m3): "))

#Processamento e saída de dados

match tipo_imovel:
    case 1:
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
    case 3:
            if consumo_mensal < 10:
                print("Consumo econômico – excelente controle de água!")
            elif consumo_mensal <= 25:
                print("Consumo moderado – dentro do padrão residencial.")
            else:
                print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
    case 2:
        if consumo_mensal <= 25:
            print("Consumo moderado – dentro do padrão residencial.")
        else:
            print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
    case _:
        print("Tipo de imóvel inválido. Por favor, informe um tipo válido (1, 2 ou 3).")