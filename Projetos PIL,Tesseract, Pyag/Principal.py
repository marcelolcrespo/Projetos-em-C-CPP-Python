from tinydb import Query, TinyDB
import sys


class Janela:
    def __init__(self):
        self.nome = ' '
        self.email = ' '
        self.plano = ' '
        self.lista_plano = ['Free', 'Vip']
        self.bd = TinyDB('BancoDados.txt')

    def database(self):
        self.bd.insert({"#=== Nome: ": self.nome, "Email: ": self.email, "Plano: ": self.plano})

    def cadastro(self):
        self.nome = str(input('Digite o nome: '))
        self.email = int(input('Digite seu email: '))
        self.plano = str(input('Digite seu plano: '))
