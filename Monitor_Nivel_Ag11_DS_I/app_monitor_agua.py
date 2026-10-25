"""Ronaldo da Silva Prado, Turma FML, Agenda 11"""

"""Aplicativo de monitoramento do nível de água com cores e mensagens de alerta."""

# Importações de bibliotecas necessárias. Random para gerar números aleatórios e colorama para colorir o texto no terminal.
import random

from colorama import Fore, Style

# Função para exibir o nível da água com cores e mensagens correspondentes.
def exibir_nivel(nivel) -> None:#->None indica que a função não retorna nenhum valor
    niveis =  [
        f"{Fore.RED} 1 - Muito baixo(critico)",
        f"{Fore.YELLOW} 2 - Baixo",
        f"{Fore.GREEN} 3 - Médio",
        f"{Fore.CYAN} 4 - Alto",
        f"{Fore.BLUE} 5 - Muito alto (alerta)",
    ]#Lista com os níveis de água e suas cores correspondentes
    print(f"\nNível da água: {niveis[nivel]}{Style.RESET_ALL}\n")#Printa o nível da água com a cor correspondente e reseta a cor para o padrão

"""Processamento e entrada de dados, incluindo autenticação do usuário e exibição do nível de água."""

def main() -> None:        #def main() é para indicar que a função main é a função principal do programa 
    print(f"\n{Fore.CYAN}Bem-vindo ao sistema de monitoramento do nível de água!{Style.RESET_ALL}")
    for tentativa in range(1, 4): #Loop para permitir até 3 tentativas de autenticação
        usuario = input("\nUsuário: ")
        senha = input("Senha: ")
        
        if usuario == "administrador" and senha == "123456":#Dados de autenticação fixos para o usuário e senha
            print(f"\n{Fore.GREEN}Acesso autorizado!{Style.RESET_ALL}")
            break

        print(f"{Fore.RED}Usuário ou senha incorretos.{Style.RESET_ALL}")

        if tentativa < 3:  #Contagem de tentativas restantes
            print(f"Tentativas restantes: {3 - tentativa}")
    else: #O bloco else é executado se o loop for concluído sem um break, ou seja, se todas as tentativas falharem
        print(f"\n{Fore.RED}Limite de tentativas excedido. Encerrando o programa.{Style.RESET_ALL}")
        return
     
    nivel = random.randint(0, 4)   #Gera um número aleatório entre 0 e 4 para sortear o nível de água
    exibir_nivel(nivel)   #Chama a função exibir_nivel() para mostrar o nível de água sorteado com a cor correspondente
            
        

main()   #Chama a função main() para iniciar o programa