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
            ID_PRODUTO INTEGER PRIMARY KEY AUTOINCREMENT,
            PRODUTO TEXT NOT NULL,
            VALOR TEXT NOT NULL,
            VALOR_TOTAL TEXT NOT NULL,
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

    def create_table_saida(self):
        try:
            cursor = self.conection.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS saida(
            ID_PRODUTO TEXT NOT NULL,
            PRODUTO TEXT NOT NULL,
            VALOR TEXT NOT NULL,
            VALOR_TOTAL TEXT NOT NULL,
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

    def insert_novo_produto(self, produto,user, valor,valor_total, un='--', kg='--', g='--'):
        d = datetime.now()
        data = d.strftime('%d/%m/%y')
        hora = d.strftime('%H:%M')
        valor = f'{float(valor):.2f}'
        try:
            cursor = self.conection.cursor()
            cursor.execute(f'''
                INSERT INTO estoque(produto, valor,valor_total,un,kg,g,data,hora,user) VALUES('{produto.strip().title()}','R${str(valor).replace('.',',')}','R${valor_total}','{un}','{kg}','{g}','{data}','{hora}','{user}');
            ''')
            self.conection.commit()
        except AttributeError:
            print('faça a conexão')

    def update_produto(self,id_produto,produto,user, valor,valor_total, un='--', kg='--', g='--'):
        d = datetime.now()
        data = d.strftime('%d/%m/%y')
        hora = d.strftime('%H:%M')
        cursor = self.conection.cursor()
        cursor.execute(f'''
                        UPDATE estoque set produto="{produto.strip().title()}", valor='R${valor}',valor_total='R${valor_total}',un='{un}',kg='{kg}',g='{g}',data='{data}',hora='{hora}',user='{user}' where id_produto = {id_produto};
                    ''')
        self.conection.commit()

    def insert_saida(self,id_produto,produto,user, valor,valor_total, un='--', kg='--', g='--'):
        d = datetime.now()
        data = d.strftime('%d/%m/%y')
        hora = d.strftime('%H:%M')
        try:
            cursor = self.conection.cursor()
            cursor.execute(f'''
                INSERT INTO saida(id_produto,produto, valor,valor_total,un,kg,g,data,hora,user) VALUES('{id_produto}','{produto.strip().title()}','R${valor}','R${valor_total}','{un}','{kg}','{g}','{data}','{hora}','{user}');
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

    def delete_user(self,usuario):
         try:
            self.usuario = usuario
            cursor = self.conection.cursor()
            cursor.execute(f'Delete from users where user = "{self.usuario}"')
            self.conection.commit()
         except:
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

    def db_check_user_admin(self, login, senha):
         try:
            cursor = self.conection.cursor()
            cursor.execute('''
            SELECT * FROM users;
            ''')
            for linha in cursor.fetchall():
                if linha[0]== login and linha[2]== senha and linha[3] == 'admin':
                    return 'admin'
                elif linha[0]== login and linha[2]== senha and linha[3] == 'user':
                    return 'user'
            return False
         except:
             print('faça a conexao')

    def check_login_exists(self,login,senha):
        try:
            cursor = self.conection.cursor()
            cursor.execute('''
           SELECT * FROM users;
           ''')
            for linha in cursor.fetchall():
                if linha[0] == login and linha[2] == senha:
                    return True
                else:
                    continue
            return False

        except Exception:
            print('faça a conexão')

    def check_user_exists(self,user):
        try:
            cursor = self.conection.cursor()
            cursor.execute('''
           SELECT * FROM users;
           ''')
            for linha in cursor.fetchall():
                if linha[1] == user:
                    return True
                else:
                    continue
            return False

        except Exception:
            print('faça a conexão')



    def cria_excel(self):
        result = pd.read_sql('SELECT * FROM Clientes;',self.conection)
        result.to_excel('CLIENTES.xlsx', sheet_name='Resumo', index=False)



if __name__ == '__main__':
    db = DataBase()
    db.conecta()
    db.create_table_usuarios()
    db.create_table_clientes()
    db.create_table_estoque()
    db.create_table_saida()
    db.insert_novo_usuario('douglas','doug_avs','123','admin')
    db.insert_novo_usuario('gabriela','gabs','123')
    # print(db.db_check_user('douglas','123'))
    # print(db.db_check_user('gabriela','123'))
    # db.cria_excel()
    db.close_conecta()

