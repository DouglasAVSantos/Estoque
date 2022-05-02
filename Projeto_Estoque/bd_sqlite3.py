import sqlite3
import pandas as pd
from datetime import datetime
from PySide2.QtWidgets import QMessageBox

class DataBase():
    def __init__(self, name='system.db'):
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
                LOGIN TEXT NOT NULL,
                USER TEXT UNIQUE,
                SENHA TEXT NOT NULL,
                ACESS TEXT NOT NULL
                );""")
        except AttributeError:
            print('erro ao criar a tabela')

    def create_table_clientes(self):
        try:
            cursor = self.conection.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes(
            ID INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
            NOME TEXT NOT NULL,
            DATA TEXT NULL,
            EMAIL TEXT NULL,
            ENDERECO TEXT NOT NULL,
            NUMERO TEXT NULL,
            BAIRRO TEXT NULL,
            CIDADE TEXT NULL,
            COMPLEMENTO TEXT NULL,
            CEP TEXT NOT NULL,
            CPF TEXT NULL,
            CELULAR TEXT NULL 
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
            HORA TEXT NOT NULL,
            USER TEXT NOT NULL
            );
            ''')
        except AttributeError:
            print('Erro ao criar a tabela estoque')

    def insert_novo_produto(self, produto,user, valor, un='--', kg='--', g='--'):
        d = datetime.now()
        data = d.strftime('%d/%m/%y')
        hora = d.strftime('%H:%M')
        try:
            cursor = self.conection.cursor()
            cursor.execute(f'''
                INSERT INTO estoque(produto, valor,un,kg,g,data,hora,user) VALUES('{produto.strip().title()}','{valor}','{un}','{kg}','{g}','{data}','{hora}','{user}');
            ''')
            self.conection.commit()
        except AttributeError:
            print('faça a conexão')

    def insert_novo_usuario(self, login,user, senha, acess='user'):
        try:
            cursor = self.conection.cursor()
            cursor.execute(f'''
                INSERT INTO users(login,user, senha, acess) VALUES('{login}','{user}','{senha}','{acess}');
            ''')
            self.conection.commit()
        except AttributeError:
            print('faça a conexão')

    def insert_novo_cliente(self,nome,cep,data="--",email="--",endereco="--",numero="--",bairro="--",cidade="--",complemento="--",cpf="--",celular="--"):
            try:
                if data == '01/01/2000':
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle('Cadastrar Data de Nascimento')
                    msg.setText('Deseja Cadastrar a Data de Nascimento?\nClique em NÃO para deixar "Vazio"')
                    msg.setStandardButtons(QMessageBox.Yes| QMessageBox.No)
                    result = msg.exec_()
                    if result == QMessageBox.No:
                        data = ''
                        cursor = self.conection.cursor()
                        cursor.execute(f'''
                        INSERT INTO Clientes(NOME,data,email,ENDERECO,numero,bairro,cidade,complemento,cep,cpf,celular) VALUES ('{nome}','{data}','{email}','{endereco}','{numero}','{bairro}','{cidade}','{complemento}','{cep}','{cpf}','{celular}');
                            ''')
                        self.conection.commit()
                    else:
                        cursor = self.conection.cursor()
                        cursor.execute(f'''
                            INSERT INTO Clientes(NOME,data,email,ENDERECO,numero,bairro,cidade,complemento,cep,cpf,celular) VALUES ('{nome}','{data}','{email}','{endereco}','{numero}','{bairro}','{cidade}','{complemento}','{cep}','{cpf}','{celular}');
                        ''')
                        self.conection.commit()
            except AttributeError:
                print('faça a conexão')

    def db_check_user(self, login, senha):
        # try:
            cursor = self.conection.cursor()
            cursor.execute('''
            SELECT * FROM users;
            ''')
            for linha in cursor.fetchall():
                if linha[0]== login and linha[2]== senha and linha[3] == 'admin':
                    return 'admin'
                else:
                    continue
            return 'user'

        # except Exception:
        #      return False



    def cria_excel(self):
        result = pd.read_sql('SELECT * FROM Clientes;',self.conection)
        result.to_excel('CLIENTES.xlsx', sheet_name='Resumo', index=False)



if __name__ == '__main__':
    db = DataBase()
    db.conecta()
    db.create_table_usuarios()
    db.create_table_clientes()
    db.create_table_estoque()
    # db.insert_novo_usuario('douglas','doug_avs','123','admin')
    # db.insert_novo_usuario('gabriela','gabs','123',)
    # print(db.db_check_user('douglas','123'))
    # print(db.db_check_user('gabriela','123'))
    # db.cria_excel()
    db.close_conecta()

