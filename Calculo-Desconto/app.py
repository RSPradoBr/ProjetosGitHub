#Ronaldo da Silva Prado - TDS turma FML
#Sistema de calculo de desconto progressivo

#Entrada de dados

valorCompra = float(input("Digite o valor da compra R$: ").replace(",", "."))

#Processamento e saída de dados

if valorCompra < 200:
    print(f"O valor da compra com desconto, de 5%, é de R$ {(valorCompra * -0.05) + valorCompra:.2f}!")
elif valorCompra <= 300:
    print(f"O valor da compra com desconto, de 10%, é de R$ {(valorCompra * -0.10) + valorCompra:.2f}!")
else:
    print(f"O valor da compra com desconto, de 15%, é de R$ {(valorCompra * -0.15) + valorCompra:.2f}!")

#Fim do programa