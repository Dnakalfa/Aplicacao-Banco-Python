import tkinter as tk
from tkinter import messagebox


class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.extrato_descricao = ""
        self.credito_extra = 0
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        self.ESPECIAL = 500
        self.credito_base = 0

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato_descricao += f'Depósito: R${valor:.2f}\n'
            return f"Valor depositado: R${valor:.2f}"
        else:
            return "Operação irregular"

    def saque(self, valor):
        excede_saldo = valor > self.saldo
        excede_limite = valor > self.limite
        excede_saque = self.numero_saques >= self.LIMITE_SAQUES

        if excede_saldo:
            opcao_credito = messagebox.askyesno("Erro", "Saldo insuficiente. Deseja fazer um empréstimo?")
            if opcao_credito:
                credito_extra = float(messagebox.askfloat("Empréstimo", f"Digite valor do empréstimo, limite de R${self.limite:.2f} : "))
                self.credito_base += credito_extra
                self.saldo += credito_extra
                if credito_extra >= self.ESPECIAL:
                    return "Não é possível realizar o empréstimo!"
            else:
                return "Voltando ao Menu!"
        elif excede_limite:
            return "Limite do dia alcançado!"
        elif excede_saque:
            return "Número máximo de saques atingido!"
        elif valor > 0:
            self.saldo -= valor
            self.extrato_descricao += f'Saque: R$: {valor:.2f}\n'
            self.numero_saques += 1
            return f"Valor sacado: R${valor:.2f}"
        else:
            return "Valor inválido!"

    def imprimir_extrato(self):
        saldo_credito_especial = self.limite - self.credito_base
        extrato = "\n*******************Extrato*********************\n"
        extrato += 'Não foram realizadas operações de depósito/saque.' if not self.extrato_descricao else self.extrato_descricao
        extrato += f'\nSaldo no crédito especial: R$ {saldo_credito_especial:.2f}'
        extrato += f'\nSaldo total: R$ {self.saldo:.2f}'
        extrato += "\n***********************************************"
        return extrato


class InterfaceGrafica(tk.Tk):
    def __init__(self, conta):
        super().__init__()
        self.title("Menu Banco")
        self.geometry("500x300")
        self.conta = conta

        self.label_input_valor = tk.Label(self, text="", font=("Arial", 12))
        self.label_input_valor.pack()

        self.entry_valor = tk.Entry(self, font=("Arial", 12))
        self.entry_valor.pack()

        self.btn_deposito = tk.Button(self, text="Depósito", command=self.handle_deposito, font=("Arial", 12))
        self.btn_deposito.pack()

        self.btn_saque = tk.Button(self, text="Saque", command=self.handle_saque, font=("Arial", 12))
        self.btn_saque.pack()

        self.btn_extrato = tk.Button(self, text="Extrato", command=self.handle_extrato, font=("Arial", 12))
        self.btn_extrato.pack()

        self.btn_sair = tk.Button(self, text="Sair", command=self.destroy, font=("Arial", 12))
        self.btn_sair.pack()

        self.acao_atual = None

    def handle_deposito(self):
        self.label_input_valor.config(text="Digite o valor do depósito:")
        self.acao_atual = self.conta.deposito
        self.btn_confirmar = tk.Button(self, text="Confirmar", command=self.executar_acao_deposito, font=("Arial", 12))
        self.btn_confirmar.pack()

    def handle_saque(self):
        self.label_input_valor.config(text="Digite o valor do saque:")
        self.acao_atual = self.conta.saque
        self.btn_confirmar = tk.Button(self, text="Confirmar", command=self.executar_acao_saque, font=("Arial", 12))
        self.btn_confirmar.pack()

    def handle_extrato(self):
        self.label_input_valor.config(text="")
        self.acao_atual = self.conta.imprimir_extrato
        self.executar_acao_extrato()

    def executar_acao_deposito(self):
        try:
            valor = float(self.entry_valor.get())
            resultado = self.acao_atual(valor)
            messagebox.showinfo("Resultado", resultado)
            self.btn_confirmar.pack_forget()
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido!")

    def executar_acao_saque(self):
        try:
            valor = float(self.entry_valor.get())
            resultado = self.acao_atual(valor)
            messagebox.showinfo("Resultado", resultado)
            self.btn_confirmar.pack_forget()
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido!")

    def executar_acao_extrato(self):
        resultado = self.acao_atual()
        messagebox.showinfo("Extrato", resultado)


if __name__ == "__main__":
    conta = ContaBancaria()
    app = InterfaceGrafica(conta)
    app.mainloop()


