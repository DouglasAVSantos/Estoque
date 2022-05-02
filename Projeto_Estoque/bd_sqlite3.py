import sqlite3
import pandas as pd
from datetime import datetime

class DataBase():
    def __init__(self, name='Administradores.db'):
        self.name = name

    def conecta(self):
        self.conection = sqlite3.connect(self.name)

    def close_conecta(self):
        try:
            self.conection.close()
        except:
            pass

    def create_table_usuarios(self):
        try:
            c = self.conection.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS users(
                iD INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                NOME TEXT NOT NULL,
                SENHA TEXT NOT NULL
                );""")
        except AttributeError:
            print('erro ao criar a tabela')

    def create_table_clientes(self):
        try:
            cursor = self.conection.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clientes(
            ID INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
            NOME TEXT NOT NULL,
            DATA TEXT NOT NULL,
            EMAIL TEXT NULL,
            ENDERECO TEXT NOT NULL,
            NUMERO TEXT NULL,
            BAIRRO TEXT NULL,
            CIDADE TEXT NULL,
            COMPLEMENTO TEXT NULL,
            CEP TEXT NOT NULL,
            CPF TEXT NOT NULL,
            CELULAR TEXT NOT NULL 
            );
            ''')
        except AttributeError:
            print('Erro ao criar a tabela')

    def create_table_estoque(self):
        try:
            cursor = self.conection.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS estoque(
            ID INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
            PRODUTO TEXT NOT NULL,
            VALOR TEXT NOT NULL,
            UN TEXT NULL,
            KG TEXT NULL,
            G TEXT NULL,
            DATA TEXT NOT NULL,
            HORA TEXT NOT NULL
            );
            ''')
        except AttributeError:
            print('Erro ao criar a tabela estoque')

    def insert_novo_produto(self, produto, valor, un='--', kg='--', g='--'):
        d = datetime.now()
        data = d.strftime('%d/%m/%y')
        hora = d.strftime('%H:%M')
        try:
            cursor = self.conection.cursor()
            cursor.execute(f'''
                INSERT INTO estoque(produto, valor,un,kg,g,data,hora) VALUES('{produto.strip().title()}','{valor}','{un}','{kg}','{g}','{data}','{hora}');
            ''')
            self.conection.commit()
        except AttributeError:
            print('faça a conexão')

    def insert_novo_usuario(self, nome, senha):
        try:
            cursor = self.conection.cursor()
            cursor.execute(f'''
                INSERT INTO users(nome, senha) VALUES('{nome}','{senha}');
            ''')
            self.conection.commit()
        except AttributeError:
            print('faça a conexão')

    def insert_novo_cliente(self,nome,data,email,endereco,numero,bairro,cidade,complemento,cep,cpf,celular):
            try:
                cursor = self.conection.cursor()
                cursor.execute(f'''
                    INSERT INTO Clientes(NOME,data,email,ENDERECO,numero,bairro,cidade,complemento,cep,cpf,celular) VALUES ('{nome}','{data}','{email}','{endereco}','{numero}','{bairro}','{cidade}','{complemento}','{cep}','{cpf}','{celular}');
                ''')
                self.conection.commit()
            except AttributeError:
                print('faça a conexão')

    def db_check_user(self, nome, senha):
        try:
            cursor = self.conection.cursor()
            cursor.execute('''
            SELECT * FROM users;
            ''')
            for linha in cursor.fetchall():
                if linha[1].upper().strip() == nome and linha[2].upper().strip() == senha:
                    return True
                else:
                    continue
            return False

        except Exception:
             print('ERRO VAGABUNDO')
    def cria_excel(self):
        result = pd.read_sql('SELECT * FROM Clientes;',self.conection)
        result.to_excel('CLIENTES.xlsx', sheet_name='Resumo', index=False)



if __name__ == '__main__':
    db = DataBase()
    db.conecta()
    db.create_table_usuarios()
    db.create_table_clientes()
    db.create_table_estoque()
    db.insert_novo_produto('limao','3,25',un='7')
    # db.insert_novo_usuario('douglas','1234')
    # db.cria_excel()
    db.close_conecta()

