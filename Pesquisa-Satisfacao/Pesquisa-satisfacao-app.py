#Ronaldo da Silva Prado
#Tuma FML, DS_I
#Programa de pesquisa de satisfação do cliente


#Armazenadores da apuração das avaliações

qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

#Limitador da quantidade de entrevistados

quantidade_entrevistados = 10

#Entrada de dados e classificação das respostas

print("\n===== PESQUISA DE SATISFAÇÃO DO CLIENTE =====")
print("\nDigite 1-Excelente, 2-Bom, 3-Ruim")
for i in range(1, quantidade_entrevistados + 1):
    print(f"\nEntrevistado {i}")
    
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    opiniao = int(input("Atribua sua satisfação: "))

    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 2:
        qtd_bom += 1
    elif opiniao == 3:
        qtd_ruim += 1
    else:
        print("Opção inválida!")

# Saída do resultado da pesquisa

print("\n===== RESULTADO DA PESQUISA =====")
print("\nQuantidade de respostas EXCELENTE:", qtd_excelente)
print("Quantidade de respostas BOM:", qtd_bom)
print("Quantidade de respostas RUIM:", qtd_ruim)
