from pathlib import Path

def carregar_configuracoes():
    #abrindo o arquivo
    with open('config.txt', 'r') as arquivo:
        configuracoes = arquivo.readlines()
        for  configuracao in configuracoes:
            if 'Numero_secreto' in configuracao:
                numero_secreto = configuracao.replace('Numero_secreto = ', '')
            if 'Quantidade_tentativas' in configuracao:
                quantidade_tentativas = configuracao.replace('Quantidade_tentativas = ', '')
        
    numero_secreto = int(numero_secreto)
    quantidade_tentativas = int(quantidade_tentativas)

    return numero_secreto, quantidade_tentativas
    

def alterar_config_num_tentativas(novo_valor_tentativa):
    numero_secreto, quantidade_tentativas = carregar_configuracoes()
    with open('config.txt', 'w') as arquivo:
        arquivo.write(f'Numero_secreto = {numero_secreto}\n')
        arquivo.write(f'Quantidade_tentativas = {novo_valor_tentativa}')
    print('Novo valor configurado')

def alterar_config_num_adivinhacao(novo_numero):
    numero_secreto, quantidade_tentativas = carregar_configuracoes()
    with open('config.txt', 'w') as arquivo:
        arquivo.write(f'Numero_secreto = {novo_numero}\n')
        arquivo.write(f'Quantidade_tentativas = {quantidade_tentativas}')
    print('Numero ajustado')


def menu_principal():
    print('''Bem vindo ao sistema de advinhação!
          Digite o número correspondente às opções abaixo:
          1 - Alterar número a ser adivinhado
          2 - Ajustar tentativas
          3 - Entrar no jogo de advinhação
          0 - Sair do sistema''')
    opcao = int(input(''))
    return opcao


def jogo(numero_secreto, quantidade_tentativas):
    contagem = 0
    nova_tentativa = True
    while (contagem < quantidade_tentativas) and (nova_tentativa == True):
        number = int(input('Chute um número ou digite zero(0) para sair: '))
        if number == 0:
            nova_tentativa = False
        else:
            if number == numero_secreto:
                print(f'Valor correto, parabéns! Você acertou o número após {contagem+1} tentativa(s)')
                nova_tentativa = False
            else:
                contagem += 1
                if contagem == quantidade_tentativas:
                    print('Acabou sua quantidade de tentativas!')
                else:
                    if number < numero_secreto:
                        print('Valor incorreto! O número é maior')
                    else:
                        print('Valor incorreto! Número é menor!')


def iniciar_sistema():
    opcao = True
    while opcao:
        menu_opcao = menu_principal()
        match menu_opcao:
            case 1:
                novo_numero = int(input('Digite o novo número: '))
                alterar_config_num_adivinhacao(novo_numero)
            case 2:
                novo_valor_tentativas = int(input('Digite o novo valor de tentativas: '))
                alterar_config_num_tentativas(novo_valor_tentativas)
            case 3:
                print('Entrando no jogo...')
                numero_secreto, quantidade_tentativas = carregar_configuracoes()
                jogo(numero_secreto, quantidade_tentativas)
            case 0:
                print('Saindo do sistema...')
                opcao = False


#Iniciando o sistema 
iniciar_sistema()