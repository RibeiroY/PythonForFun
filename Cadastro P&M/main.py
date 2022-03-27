from pessoa import Pessoa
from equipamento import Equipamento

lista_func=[]
lista_equip=[]
chaves=[]
chaves_equip=[]
#Essa brincadeira haverá atualizações. No momento, o único item sem repetições é a chave cadastrada.


print("OLÁ! BEM VINDO!")
operacao_diretor = 0
while operacao_diretor != 4:

    print("QUE OPERAÇÃO DESEJA FAZER?")
    print("1-CADASTRO DE FUNCIONÁRIOS OU MÁQUINAS")
    print("2-CONSULTA DE EXISTÊNCIA DE FUNCIONÁRIOS OU MÁQUINAS")
    print("3-REMOÇÃO DE DETERMINADO FUNCIONÁRIO OU MÁQUINA")
    print("4-ENCERRAR")
    operacao_diretor = input()
    operacao_diretor = int(operacao_diretor)

    while operacao_diretor != 1 and operacao_diretor != 2 and operacao_diretor != 3 and operacao_diretor != 4:
        print("Operador Inválido! Tente Novamente!")
        operacao_diretor = input()
        operacao_diretor = int(operacao_diretor)

    if operacao_diretor ==1:
        print("Deseja cadastrar um FUNCIONÁRIO(opção 1) ou uma MÁQUINA(opção 2) ou RETORNAR (opção 3)?")
        suboperacao = input()
        suboperacao = int(suboperacao)
        while suboperacao != 1 and suboperacao != 2 and suboperacao != 3:
            print("Operador Inválido! Tente Novamente!")
            suboperacao = input()
            suboperacao = int(suboperacao)
        if suboperacao == 1:
            print("Digite o CPF do cidadão")
            CPF = input()
            CPF = int(CPF)
            print("Digite o nome do cidadao")
            nome = input()
            print("Digite a chave do funcionário a ser cadastrado.")
            chave = input()
            a=1
        
            if chaves in chaves:
                print("Chave já cadastrada. Por favor, tente novamente!")
                a=0
            
                
            if a == 1:
                print("Chave inserida!")
                lista_func.append(Pessoa(CPF,nome,chave))
                chaves.append(chave)
            
                
        elif suboperacao == 2:
            print("Digite o setor da máquina correspondente.")
            setor = input()
            print("Digite o nome do equipamento")
            nome = input()
            print("Digite a chave do equipamento a ser cadastrado.")
            chave = input()
            a=1 

            if chave in chaves_equip:
                print("Chave já cadastrada. Por favor, tente novamente!")
                a=0
            if a == 1:
                print("Chave inserida!")
                lista_equip.append(Equipamento(setor,nome,chave))
                chaves_equip.append(chave)
            
        
    elif operacao_diretor==2:
        suboperacao = input(("Deseja pesquisar um funcionário(opção 1) ou uma máquina(opção 2)? Qualquer outra tecla retorna."))
        suboperacao = int(suboperacao)
        while suboperacao != 1 and suboperacao != 2 and suboperacao != 3:
            print("Operador Inválido! Tente Novamente!")
            suboperacao = input(int)
        if suboperacao == 1:
            print("Digite a chave do funcionário a ser pesquisado.")
            chave = input()
            if chave in chaves:
                print("Funcionário encontrado!")
                indice = chaves.index(chave)
                print(lista_func[indice])
                
            else:
                print("Funcionário não encontrado. Tente novamente!")
        elif suboperacao == 2:
            print("Digite a chave do equipamento a ser pesquisado.")
            chave = input()
            if chave in chaves_equip:
                indice = chaves_equip.index(chave)
                print(lista_equip[indice])
            else:
                print("Equipamento não encontrado. Tente novamente!")
    elif operacao_diretor == 3:
        print("Deseja deletar um funcionário(opção 1) ou uma máquina(opção 2)? Qualquer outra tecla retorna.")
        a = input()
        a = int(a)
        if a == 1:
            chave = input("Digite a chave do funcionário a ser deletado.")
            if chave in chaves:
                indice = chaves.index(chave)
                del lista_func[indice]
                del chaves[indice]
                print("Funcionário deletado!")
            else:
                print("Item não encontrado.")
        elif a == 2:
            chave = input("Digite a chave do equipamento a ser deletado.")
        
            if chave in chaves_equip:
                indice = chaves_equip.index(chave)
                del lista_equip[indice]
                del chaves_equip[indice]
                print("Equipamento deletado!")
            else:
                print("Item não encontrado.")

print("Programa encerrado!")
                

    



