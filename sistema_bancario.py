from datetime import datetime

class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial
        self.depositos = []  # Armazena os depósitos
        self.saques = []  # Armazena os saques
        self.saques_diarios = 0  # Contador de saques diários

    def exibir_saldo(self):
        print(f"Saldo da conta {self.numero_conta} ({self.nome_titular}): R$ {self.saldo:.2f}")

    def depositar(self, valor):
        self.saldo += valor
        self.depositos.append((datetime.now(), valor))  # Armazena o depósito com data e valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if self.saques_diarios >= 3:
            print("Limite de 3 saques diários atingido.")
        elif valor > 500:
            print("O valor máximo permitido por saque é de R$ 500.00.")
        elif valor > self.saldo:
            print("Saldo insuficiente, não foi possível realizar a operação.")
        else:
            self.saldo -= valor
            self.saques.append((datetime.now(), valor))  # Armazena o saque com data e valor
            self.saques_diarios += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        print("\nExtrato da conta:")
        print("Depósitos:")
        for data, valor in self.depositos:
            print(f"Data: {data.strftime('%d/%m/%Y %H:%M:%S')} - Valor: R$ {valor:.2f}")
        
        print("\nSaques:")
        for data, valor in self.saques:
            print(f"Data: {data.strftime('%d/%m/%Y %H:%M:%S')} - Valor: R$ {valor:.2f}")
        
        self.exibir_saldo()
    
    def resetar_saques_diarios(self):
        """Reseta o contador de saques diários (chame essa função no início de cada dia)"""
        self.saques_diarios = 0

# Função para exibir o menu e capturar a escolha do usuário
def menu_conta(conta):
    while True:
        print("\nMenu de Opções:")
        print("1 - Exibir saldo")
        print("2 - Depósito")
        print("3 - Saque")
        print("4 - Exibir extrato")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            conta.exibir_saldo()
        elif opcao == '2':
            valor = float(input("Digite o valor do depósito: "))
            conta.depositar(valor)
        elif opcao == '3':
            valor = float(input("Digite o valor do saque: "))
            conta.sacar(valor)
        elif opcao == '4':
            conta.exibir_extrato()
        elif opcao == '5':
            print("Obrigado por usar nossos serviços!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Criando uma conta a partir de inputs do usuário
numero_conta = int(input("Digite o número da conta: "))
nome_titular = input("Digite o nome do titular: ")
saldo_inicial = float(input("Digite o saldo inicial: "))

conta1 = ContaBancaria(numero_conta, nome_titular, saldo_inicial)

# Exibindo o menu de opções
menu_conta(conta1)
