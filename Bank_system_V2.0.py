
import time

Dados_usuario = {
    12345678910: {'nome': 'José Pedro', 'senha': 123456, 'nascimento': '01/01/2001', 'cpf': 12345678910, 'tipo_de_conta': 1, 'endereco': {'rua': 'Rua dos Ficticios, 145', 'cep': 44454647, 'cidade': 'Alguma', 'sigla_estado': 'SP'}},
    10987654321: {'nome': 'Jorge Rodrigo', 'senha': 123123, 'nascimento': '01/01/2001', 'cpf': 10987654321, 'tipo_de_conta': 2, 'endereco': {'rua': 'Rua dos Verdadeiros, 936', 'cep': 41424344, 'cidade': 'Cideda', 'sigla_estado': 'SP'}},                
}

Dados_bancarios = {
    12345678910: {'nome': 'José Pedro', 'saldo': 0, 'limite': 3, 'tipo_de_conta': 1, 'extrato': ''},
}

Dados_contas_correntes = {
    10987654321: {"Jorge Rodrigo" : { "usuarios":{
                "Paulo Rodrigo":{'saldo':0 , 'limite': 3, 'extrato': ''},
                "Pedro Matos":{'saldo':0 , 'limite': 3, 'extrato': ''},
                "Tim Teressa":{'saldo':0 , 'limite': 3, 'extrato': ''}
                }}}, 
}     



def CRIAR_USUARIO():
    
    def TIPO_VALIDO():
        while True :           
            tipo_de_conta = str(input("Digite o tipo de conta: \n [1]comum \n [2]corrente \n => ")) 
         
            if tipo_de_conta == "1":
                print("Tipo conta comum foi selecionado!\n ")
                return int(tipo_de_conta)

            elif tipo_de_conta == "2":
                print("Tipo conta corrente foi selecionado! \n")
                
                return int(tipo_de_conta)
            
            elif tipo_de_conta != "1" or tipo_de_conta != "2":
                print("Tipo da Conta Inválida, tente Novamente!")
            
            else:
                print("Comando invalido!\n")
        
    def CPF_VALIDO(): 
     
        while True:
            cpf = str(input("Digite seu CPF: \n => "))
          
            if len(cpf) == 11:
                return int(cpf)
        
            elif len(cpf) != 11:
                print("CPF inválido! Tente novamente!")
            
            else:
                print("Comando inválido!")
        
    def NASCIMENTO_VALIDO():
       
        while True:
            print("\nColoque sua data de nascimento(dd/mm/aaaa):")
            dia = str(input("Insira o dia(dd):\n==> "))
            mes = str(input("Insira o mês(mm): \n==> "))
            ano = str(input("Insira o ano(aaaa):\n==> "))
            
            dia_numero = dia.isdigit()  
            mes_numero = mes.isdigit()  
            ano_numero = ano.isdigit()            
            nascimento = f"{dia}/{mes}/{ano}"
            
            if dia_numero == True and mes_numero == True and ano_numero == True:
                
                if len(dia) == 2 and len(mes) == 2 and len(ano) == 4:
                    print(f"Data de nascimento salva com sucesso! \nData registrada: {nascimento} \n ")
                    return nascimento
                
                elif len(dia) != 2 :
                    print("Dia Inválido. Tente Novamente.\n ")
                    
                elif len(mes) != 2:
                    print("Mês Inválido. Tente Novamente.\n ")
                    
                elif len(ano) != 2:
                    print("Ano Inválido. Tente Novamente.\n ")
                    
                else:
                    print("Comando inválido!")
            
            else:
                print("Data Inválida! tente novamente")
    
    def SENHA_VALIDA():
        while True:
            senha = str(input("Digite sua senha de 6 à 9 caracteres(Apenas numeros): \n => "))
            sem_letra = senha.isdigit()
            
            if len(senha) >= 6 and len(senha) <= 9:
                if sem_letra == False:
                    print("Senha inválida! A senha não pode conter letras!\n")
                    
                elif sem_letra == True:
                    print("Senha cadastrada com sucesso!\n")
                    return int(senha)
            
                else:
                    print("Comando inválido!\n")
            
            elif len(senha) > 9:
                
                print("Senha inválida! Senha muito grande!\n")
            
            elif len(senha) < 6:
                print("Senha inválida! Senha muito curta!\n")
                
            elif sem_letra == False:
                print("Senha inválida! Contém letra!\n")
                
            else:
                print("Comando inválido!\n")
        
    def RUA():
        nome_rua = str(input("Digite o nome da rua:\n  => "))    
        while True:          
            numero_rua = str(input("Digite o número de sua residência:\n  => "))
            numero_rua_verificado = numero_rua.isdigit()
            
            if numero_rua_verificado == True:
                return(f"{nome_rua.title()}, {numero_rua}")
            
            elif numero_rua_verificado == False:
                print("O número não pode conter letra!")
                
            else:
                print("Comando inválido!")
       
    def NOME():
        nome = str(input("Insira seu nome: \n => "))
        sobrenome = str(input("Insira seu sobrenome: \n => "))

        return (f"{nome.title()} {sobrenome.title()}")
          
    def CEP():
        while True:
            cep = str(input('Informe seu cep \n => '))
            cep_verify = cep.isdigit()
            
            if cep_verify == True:
                return int(cep)
            
            elif cep_verify == False:
                print("CEP não pode conter letra!")
            
            else:
                print("Comando inválido!")
         
    def ESTADO():
        while True:
            estados = ('AC', 'AL', 'AP', 'AM', 'BA','CE','DF','ES',
                   'GO','MA','MT','MS','MG','PA','PB','PR','PE',
                   'PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO')
            
            estado_input = str(input("Digite a sigla da sua estado: \n => " ))
            estado_input_organized = estado_input.upper()
            
            tem_estado = estado_input_organized in estados
            
            if tem_estado == True:
                return estado_input_organized
            
            elif tem_estado == False:
                print("Estado inválido! Tente novamente\n")
      
      
    def USUARIO_CORRENTE(tipo_de_conta=0):     
        
        if tipo_de_conta == 2:
            primeiro_nome = str(input("Digite o primeiro nome do usuario inicial:\n==> "))
            segundo_nome = str(input("Digite o segundo nome do usuario inicial:\n==> "))
            usuario_corrente = f"{primeiro_nome.title()} {segundo_nome.title()}"
            print(f"O usuário {usuario_corrente} foi cadastrado com sucesso!")
            return usuario_corrente
        
        else:
            pass
        
    def CIDADE():
        Cidade = str(input("Digite sua cidade: \n => " ))
        return Cidade.title
        
        
    
    nome = NOME()
    cpf = CPF_VALIDO()
    tipo_de_conta = TIPO_VALIDO() 
    usuario_conta_corrente = USUARIO_CORRENTE(tipo_de_conta=tipo_de_conta)
    nascimento = NASCIMENTO_VALIDO()
    senha = SENHA_VALIDA()
    rua = RUA()
    cep = CEP()
    cidade = CIDADE()
    estado = ESTADO()

    def criar_usuario(nome="vazio", nascimento=0, cpf=0, senha=0 ,tipo_de_conta=0):         
        conta = Dados_usuario.copy()
        conta_corrente = Dados_contas_correntes.copy()
        nome_usuario = usuario_conta_corrente
        cpf_existe = cpf in Dados_usuario or cpf in Dados_contas_correntes
        
        if cpf_existe == True:
            return(print("Falha ao fazer cadastrado! Usuário já cadastrado"))
        
        elif cpf_existe == False:
            if tipo_de_conta == 1:
                conta.update({cpf: {"nome":nome, "senha": senha, "nascimento": nascimento, "cpf": cpf, "tipo_de_conta": tipo_de_conta, "endereco": {"rua": rua, "cep": cep, "cidade": cidade, "sigla_estado": estado}}})
                Dados_bancarios.update({cpf: {"nome":nome, "saldo":0, "limite":3, "tipo_de_conta":tipo_de_conta, "extrato":""}})
                Dados_usuario.update(conta)
                return(print(f"Parabéns {nome}! Sua conta foi cadastrada com sucesso"))
            
            elif tipo_de_conta == 2:
                conta.update({cpf: {"nome":nome, "senha": senha, "nascimento": nascimento, "cpf": cpf, "tipo_de_conta": tipo_de_conta, "endereco": {"rua": rua, "cep": cep, "cidade": cidade, "sigla_estado": estado}}})
                Dados_usuario.update(conta)
                conta_corrente.update({cpf: {nome: {"usuarios": {nome_usuario:{'saldo':0 , 'limite': 3, 'extrato': ''}}}}})
                Dados_contas_correntes.update(conta_corrente)
                return(print(f"Parabéns {nome}! Sua conta foi cadastrada com sucesso"))

    criar_usuario(nome=f"{nome}", nascimento=f"{nascimento}",senha=senha, cpf=cpf, tipo_de_conta=tipo_de_conta)
    
def LOGIN():    
    cpf = int(input("Digite seu CPF\n => "))
    senha = int(input("Digite sua senha\n => "))
    
    def login(cpf=0, senha=0):
        user_data = Dados_usuario.copy()       
        has_data = cpf in user_data 

        if has_data == True:
            data_pass = senha == user_data[cpf]["senha"]
            
            if data_pass == True:
                if user_data[cpf]["tipo_de_conta"] == 1:
                    MENU(cpf=cpf)
                    
                
                elif user_data[cpf]["tipo_de_conta"] == 2:
                    MENU_CORRENTE(cpf=cpf, Nome_titular=user_data[cpf]["nome"] )
                        
            elif data_pass == False:
                #print(user_data) - para verificar se está sendo validado
                return print ("Senha incorreta!")
                
            else:
                return print("not ok")
            
        elif has_data == False :
            print("usuario não cadastrado")
            
    login(cpf=cpf, senha=senha)
    
def MENU(cpf=0):
    
    cpf_user = cpf
    nome = Dados_bancarios[cpf_user]["nome"]
    saldo = Dados_bancarios[cpf_user]["saldo"]
    extrato = Dados_bancarios[cpf_user]["extrato"]
    tempo = 1.5
    limite = 500
    LIMITE_SAQUES = 3
    
    def DEPOSITAR(valor_deposito, /):
            valor = valor_deposito
            valor_organizado = str(valor_deposito).replace(",", ".").strip()
            valor = float(valor_organizado)
                
            if valor > 0:
                saldo = Dados_bancarios[cpf_user]["saldo"]
                extrato = Dados_bancarios[cpf_user]["extrato"]

                saldo += valor
                print(f"Depósito no valor de R${valor:.2f} realizado com sucesso!")
                extrato += f"+{valor:.2f} Deposito na conta.\n Saldo atual: R${saldo:.2f}.\n"

                Dados_bancarios[cpf_user]["saldo"] = saldo
                Dados_bancarios[cpf_user]["extrato"] = extrato
                    
                return Dados_bancarios
                
            elif valor < 0:
                print("Valor informado não exite!")
            
            elif valor == str:
                print("O valor não pode conter letras")
                
            else:
                print("Comando Inválido!")

    def SACAR(cpf=0, Saque_Limite=0):
        cpf_user = cpf
        LIMITE_SAQUES = Saque_Limite
        
        saldo = Dados_bancarios[cpf_user]["saldo"]
        extrato = Dados_bancarios[cpf_user]["extrato"]
        
        if LIMITE_SAQUES == 0:
                print("Você não tem mais saques disponivel. Volte amanhã para realizar novos saques.")
                
        if LIMITE_SAQUES > 0:
            
            print(f"Você tem {LIMITE_SAQUES} saques disponíveis")
            print(f"Lembrando que o limite de saque é de R$ {limite}")
            
            while True:         
                
                Valor = str(input((f"Qual o valor a ser sacado? \n")))
                valor_organizado = str(Valor).replace(",", ".").strip()
                valor = float(valor_organizado)
                
                if valor <= limite and valor > 0 and valor <= saldo:
                    LIMITE_SAQUES -= 1
                    saldo -= valor
                    print("sacando...")
                    time.sleep(tempo)
                    extrato += (f"-{valor:.2f}\tSaque na conta.\n Saldo atual: R${saldo: .2f}.\n")
                    print(f"Saque no valor de R${valor: .2f} realizado com sucesso!")
                    Dados_bancarios[cpf_user]["saldo"] = saldo
                    Dados_bancarios[cpf_user]["extrato"] = extrato
                    Dados_bancarios[cpf_user]["limite"] = LIMITE_SAQUES
                            
                    return Dados_bancarios,
                            
                elif valor > limite:
                    print("Não foi possível realizar o saque pois o valor desejado é maior que permitido\n")
                            
                elif valor > saldo:
                    print("Saldo insuficiente! Não será possível efetuar o saque!\n")
                     
                else:
                    print("\nValor inválido ou negativo!! Tente novamente.")
                    break
                
            else:
                print("\nValor inválido ou não numérico!! Tente novamente.")
        
    menu = f"""
    ======= menu =======
    Saldo: R${Dados_bancarios[cpf_user]["saldo"]:.2f}
    Usuário: {nome}

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

    => """
    


    while True:
        
        saldo = Dados_bancarios[cpf_user]["saldo"]
        LIMITE_SAQUES = Dados_bancarios[cpf_user]["limite"]
        
        opcao = input(menu)
        
        if opcao == "d":
                Valor = str(input(f"Informe o valor a ser depositado: "))
                DEPOSITAR(Valor)
                  
        elif opcao == "s":
            SACAR(cpf=cpf_user, Saque_Limite=LIMITE_SAQUES)
            
        elif opcao == "e":
            print("======== extrato ========\n")
            print("Não foram realizadas movimentações." if not Dados_bancarios[cpf_user]["extrato"] else Dados_bancarios[cpf_user]["extrato"])
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=========================")
            
            while True:
                visualizado = input("[1] Fechar\n=> ")
                if visualizado == "1":
                    break
                else:
                    print("\nComando Inválido, tente outra vez...\n=> ")
            
        elif opcao == "q":
            break
        
        else:
            print("Este comando é inválido. Escolha uma das opções do menu!")                    
        
        menu = f"""
    ======= menu =======
    Saldo: R${Dados_bancarios[cpf_user]["saldo"]:.2f}
    Usuário: {nome}

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

    => """
   
def MENU_CORRENTE(cpf=0, Nome_titular=""):
    cpf_user = cpf
    Dados_user = Dados_usuario.copy()

    def numeros(dados, /):
        for posicao, listinha in enumerate(dados):
            print(f"[{posicao}] {listinha}")
    
    def Selecionando(dados, /):    
        while True:
            print("\nSelecione um usuário abaixo:\n")
            numeros(dados)
            opcao = int(input("==> "))
                
            if 0 <= opcao < len(dados):
                item_selecionado = dados[opcao]
                print("Item selecionado:", item_selecionado)
                return item_selecionado
                    
            else:
                print("\nÍndice inválido. Tente novamente.")
    
    Usuarios_Conta_Corrente = list(Dados_contas_correntes[cpf][Dados_user[cpf]["nome"]]["usuarios"])
    Nome_usuario_corrente = Selecionando(Usuarios_Conta_Corrente)
    
    nome = Nome_usuario_corrente          
    saldo = Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["saldo"]
    extrato = Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["extrato"]
    tempo = 1.5
    limite = 500
    LIMITE_SAQUES = 3
    
    def DEPOSITAR(valor_deposito, /):
            valor = valor_deposito
            valor_organizado = str(valor_deposito).replace(",", ".").strip()
            
            valor = float(valor_organizado)
                
            if valor > 0:
                saldo = Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["saldo"]
                extrato = Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["extrato"]

                saldo += valor
                print(f"Depósito no valor de R${valor:.2f} realizado com sucesso!")
                extrato += f"+{valor:.2f} Deposito na conta.\n Saldo atual: R${saldo:.2f}.\n"

                Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["saldo"] = saldo
                Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["extrato"] = extrato
                    
                return Dados_contas_correntes
                
            elif valor < 0:
                print("Valor informado não exite!")
                
            else:
                print("Comando Inválido!")


    def SACAR(cpf=0, Saque_Limite=0):
        cpf_user = cpf
        LIMITE_SAQUES = Saque_Limite
        saldo = Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["saldo"]
        extrato = Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["extrato"]
        
        if LIMITE_SAQUES == 0:
                print("Você não tem mais saques disponivel. Volte amanhã para realizar novos saques.")
                
        if LIMITE_SAQUES > 0:
            
            print(f"Você tem {LIMITE_SAQUES} saques disponíveis")
            print(f"Lembrando que o limite de saque é de R${limite}")
            
            while True:         
                
                Valor = str(input((f"Qual o valor a ser sacado? \n")))
                valor_organizado = str(Valor).replace(",", ".").strip()
                valor = float(valor_organizado)
                if valor <= limite and valor > 0 and valor <= saldo:
                    LIMITE_SAQUES -= 1
                    saldo -= valor
                    print("sacando...")
                    time.sleep(tempo)
                    extrato += (f"-{valor:.2f}\tSaque na conta.\n Saldo atual: R${saldo: .2f}.\n")
                    print(f"Saque no valor de R${valor: .2f} realizado com sucesso!")
                    Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["saldo"] = saldo
                    Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["extrato"] = extrato
                    Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["limite"] = LIMITE_SAQUES
                        
                    return Dados_contas_correntes
                            
                elif valor > limite:
                    print("Não foi possível realizar o saque pois o valor desejado é maior que permitido\n")
                        
                elif valor > saldo:
                    print("Saldo insuficiente! Não será possível efetuar o saque!\n")
                     
                else:
                    print("\nValor inválido ou negativo!! Tente novamente.")
                
            else:
                print("\nValor inválido ou não numérico!! Tente novamente.")
       
    def CRIAR_USUARIO_CORRENTE(cpf=0, nome_titular=""):
        primeiro_nome=str(input('Digite seu primeiro:\n ==> '))
        segundo_nome = str(input("\nDigite seu segundo nome:\n ==> "))
        Dados_contas_correntes[cpf][nome_titular]["usuarios"][f"{primeiro_nome.title()} {segundo_nome.title()}"] = {'saldo': 0, 'limite': 3, 'extrato': ''}
        print(f"Parabéns, a conta {primeiro_nome.title()} {segundo_nome.title()} foi criada com sucesso!")
        
    def TROCAR_USUARIO(cpf=0, nome_titular=""):
        dados_corrente = list(Dados_contas_correntes[cpf][nome_titular]["usuarios"])
        
        def numeros(dados, /):
            for posicao, listinha in enumerate(dados):
                print(f"[{posicao}] {listinha}")
    
        def Selecionando(dados, /):
                
            while True:
                print("\nSelecione um usuário abaixo:\n")
                numeros(dados)
                opcao = int(input("==> "))
                
                if 0 <= opcao < len(dados):
                    item_selecionado = dados[opcao]
                    print("Conta Selecionada:", item_selecionado)
                    return item_selecionado
                    
                else:
                    print("\nÍndice inválido. Tente novamente.")
                    
        
        
        return Selecionando(dados_corrente)
        
    menu = f"""
    ======= menu =======
    Saldo: R${Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["saldo"]:.2f}
    Usuário: {nome}

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [c] Criar novo usuario
        [t] Trocar de usuario
        [q] Sair

    => """
    
    while True:
        
        saldo = Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["saldo"]
        LIMITE_SAQUES = Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["limite"]
        
        opcao = input(menu)
        
        if opcao == "d":
            Valor = str(input(f"Informe o valor a ser depositado: "))
            DEPOSITAR(Valor)
          
                
        elif opcao == "s":
            SACAR(cpf=cpf_user, Saque_Limite=LIMITE_SAQUES)
            
        elif opcao == "e":
            print("======== extrato ========\n")
            print("Não foram realizadas movimentações." if not Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["extrato"] else Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["extrato"])
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=========================")
            
            while True:
                visualizado = input("[1] Fechar\n=> ")
                if visualizado == "1":
                    break
                else:
                    print("\nComando Inválido, tente outra vez...\n=> ")
            
        elif opcao == "c":
            CRIAR_USUARIO_CORRENTE(cpf=cpf_user, nome_titular=Nome_titular)
        
        elif opcao == "t":
            nome = TROCAR_USUARIO(cpf=cpf_user, nome_titular=Nome_titular)
            
        elif opcao == "q":
            break
        
        else:
            print("Este comando é inválido. Escolha uma das opções do menu!")                    
        
        menu = f"""
    ======= menu =======
    Saldo: R${Dados_contas_correntes[cpf_user][Nome_titular]["usuarios"][nome]["saldo"]:.2f}
    Usuário: {nome}

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [c] Criar novo usuario
        [t] Trocar de usuario
        [q] Sair

    => """
    
HOME = """
Seja bem-vindo ao banco Python

[1] Login
[2] Cadastrar
[0] Sair

=> """

while True:
    
    home_opcao = input(HOME)
    
    if home_opcao == "1":
        print("\n===== Área de login ====== \n")
        LOGIN()
        print("\n=============================== \n")

    elif home_opcao == "2":
        print("\n===== Criação de usuário ====== \n")
        CRIAR_USUARIO()
        print("\n===============================")

    elif home_opcao == "0":
        print("Saindo...")
        break

    else:
        print("Operação falhou! O valor informado é inválido.")


