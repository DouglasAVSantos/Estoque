import sys
from bd_sqlite3 import DataBase
from PySide2.QtWidgets import (QApplication, QMainWindow,QWidget,QMessageBox)
from PySide2.QtSql import QSqlDatabase, QSqlTableModel
from ui_login import Ui_Login
from ui_MainWindow import Ui_MainWindow
from Produtos_ui import Ui_Produtos
import pandas as pd
import requests
import json

#instancia do Login
class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login,self).__init__()
        self.setupUi(self)
        #botao de login para se conectar ao sistema principal chamando a funcao de verificar senha

        self.pb_login.clicked.connect(self.verifica_senha)
    def messagebox_critical(self, txt):
        msg = QMessageBox()
        msg.setIcon(msg.Critical)
        msg.setWindowTitle('ERRO DE DADOS')
        msg.setText(txt)
        msg.exec()

    #Verifica a senha e chama o Sistema caso True
    def verifica_senha(self):
        try:
            db = DataBase()
            db.conecta()
            if db.db_check_user_admin(self.lineEdit_usuario.text().strip(),self.lineEdit_senha.text().strip()) == 'user':
                self.login = self.lineEdit_usuario.text()
                self.senha = self.lineEdit_senha.text()
                self.w = MainWindow(self.login,self.senha)
                self.w.bt_novo_usuario.hide()
                self.w.show()
                self.close()
                db.close_conecta()
            elif db.db_check_user_admin(self.lineEdit_usuario.text().strip(),self.lineEdit_senha.text().strip()) == 'admin':
                self.login = self.lineEdit_usuario.text()
                self.senha = self.lineEdit_senha.text()
                self.w = MainWindow(self.login,self.senha)
                self.w.show()
                self.close()
                db.close_conecta()
        except:
                    # abre uma caixa de msg com erro
            self.messagebox_critical('LOGIN OU SENHA INVÁLIDOS')
            self.lineEdit_senha.setText('')


class Produtos(QWidget, Ui_Produtos):
    def __init__(self,user) -> None:
        super(Produtos,self).__init__()
        self.setupUi(self)
        self.user = user

        self.bt_novo_produto.clicked.connect(self.add_produto)

    def messagebox_critical(self, txt):
        msg = QMessageBox()
        msg.setIcon(msg.Critical)
        msg.setWindowTitle('ERRO DE DADOS')
        msg.setText(txt)
        msg.exec()

    def messagebox_accept(self, txt):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("DADOS ACEITOS")
        msg.setText(txt)
        msg.exec_()


    def add_produto(self):
        produto = self.le_produto.text()
        user = self.user
        ref = self.comboBox_quantidade.currentText()
        quantidade = self.le_quantidade.text()
        quantidade_int = int(quantidade)
        valor = self.le_valor.text().replace(',','.')
        valor_int = float(valor)
        valor_total = f"{valor_int*quantidade_int:.2f}".replace('.',',')
        valorstr = self.le_valor.text()
        if ref == 'KG':
            db = DataBase()
            db.conecta()
            db.insert_novo_produto(produto,user,valorstr,valor_total,kg=quantidade)
            self.messagebox_accept('PRODUTO CADASTRADO COM SUCESSO')
            self.close()
            db.close_conecta()
        elif ref == 'G':
            db = DataBase()
            db.conecta()
            db.insert_novo_produto(produto, user, valorstr, valor_total, g=quantidade)
            self.messagebox_accept('PRODUTO CADASTRADO COM SUCESSO')
            self.close()
            db.close_conecta()
        elif ref == 'UN':
            db = DataBase()
            db.conecta()
            db.insert_novo_produto(produto, user, valorstr, valor_total, un=quantidade)
            self.messagebox_accept('PRODUTO CADASTRADO COM SUCESSO')
            self.close()
            db.close_conecta()



# instancia do Sistema
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,login,senha):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.login = login
        self.senha = senha

        self.get_usuario(self.login,self.senha)


            #**************BOTOES DO SISTEMA*************************
        self.bt_home.clicked.connect(lambda: self.StackedWidget.setCurrentWidget(self.home))
        self.bt_contato.clicked.connect(lambda: self.StackedWidget.setCurrentWidget(self.Contato))
        self.bt_estoque.clicked.connect(lambda: self.StackedWidget.setCurrentWidget(self.estoque))
        self.bt_cadastro.clicked.connect(lambda: self.StackedWidget.setCurrentWidget(self.cadastro))
        self.bt_clientes.clicked.connect(lambda: self.StackedWidget.setCurrentWidget(self.clientes))
        self.bt_novo_usuario.clicked.connect(lambda: self.StackedWidget.setCurrentWidget(self.Cadastro_novo_usuario))

                #BOTAO PARA CADASTRAR CLIENTE NO BANCO DE DADOS
        self.bt_cadastrar.clicked.connect(self.novo_cliente)

        self.bt_cadastrar_usuario.clicked.connect(self.new_user)
        self.bt_deletar_usuario.clicked.connect(self.delete_user)

        self.le_cep.textChanged.connect(self.alimenta_cep)


        self.bt_importar.clicked.connect(self.import_produto)

        self.reset_tables()

    def get_usuario(self,login,senha):
        try:
            db = DataBase()
            db.conecta()
            cursor = db.conection.cursor()
            cursor.execute(f'select user from users where login = "{login}" and senha = "{senha}" ')
            usuario = cursor.fetchone()
            self.usuario = usuario[0]
            print(self.usuario)
            db.close_conecta()
        except:
            self.messagebox_critical('Usuario não encontrado')

    def import_produto(self):
        self.p = Produtos(self.usuario)
        self.p.show()
        self.reset_tables()






        #FUNCAO QUE VERIFICA SE AS SENHAS INFORMADAS AO CRIAR UM NOVO USUARIO ESTAO VAZIAS OU NAO SÃO IGUAIS

    def messagebox_critical(self, txt):
        msg = QMessageBox()
        msg.setIcon(msg.Critical)
        msg.setWindowTitle('ERRO DE DADOS')
        msg.setText(txt)
        msg.exec()

    def messagebox_accept(self, txt):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("DADOS ACEITOS")
        msg.setText(txt)
        msg.exec_()

    def new_user(self):
        db = DataBase()
        db.conecta()
        login = self.le_novo_login.text().strip()
        senha = self.le_senha1.text().strip()
        usuario = self.le_novo_usuario.text().strip()
        acess = self.cb_users.currentText()


        if senha != self.le_senha2.text().strip():
            self.messagebox_critical('As senhas informadas não são iguais\nPreencha os campos com as senhas iguais.')
            self.le_senha1.setText('')
            self.le_senha2.setText('')
        elif senha == '' or self.le_senha2.text() == '' or usuario == '' or login == '':
            self.messagebox_critical('Campos vazios\nPreencha os campos com Usuario e as senhas iguais.')
            self.le_senha1.setText('')
            self.le_senha2.setText('')
        elif db.check_login_exists(login, senha):
            self.messagebox_critical('Usuario e Senha ja Cadastrado\nPreencha os campos com um novo Usuario e senha')
            self.le_senha1.setText('')
            self.le_senha2.setText('')
            self.le_novo_usuario.setText('')
        else:
            db.insert_novo_usuario(login,usuario,senha,acess)
            self.messagebox_accept('Senha Cadastrada com Sucesso!')
            self.le_senha1.setText('')
            self.le_novo_login.setText('')
            self.le_novo_usuario.setText('')
            self.le_senha2.setText('')
            db.close_conecta()
                #FUNÇÃO QUE ADICIONA UM CADASTRO DE CLIENTE NO BANCO DE DADOS

    def delete_user(self):
        db = DataBase()
        db.conecta()
        usuario = self.le_usuario_deletar.text()

        if self.le_senha_deletar.text() == self.senha and db.check_user_exists(usuario):
            db.delete_user(usuario)
            self.messagebox_accept('USUARIO DELETADO COM SUCESSO!')
            self.le_usuario_deletar.setText('')
            self.le_senha_deletar.setText('')
            db.close_conecta()
        else:
            self.messagebox_critical('USUARIO NÃO CADASTRADO')
            self.le_usuario_deletar.setText('')
            self.le_senha_deletar.setText('')
            db.close_conecta()

    def show_table_clientes(self):
        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName('system.db')
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tv_clientes.setModel(self.model)
        self.model.setTable('clientes')
        self.model.select()

    def show_table_estoque(self):
        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName('system.db')
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tv_estoque.setModel(self.model)
        self.model.setTable('estoque')
        self.model.select()

    def reset_tables(self):
        self.tv_estoque.update()
        self.tv_clientes.update()
        self.show_table_estoque()
        self.show_table_clientes()


    def novo_cliente(self):
        db = DataBase()
        db.conecta()
        nome = self.le_nome.text().upper().strip()
        data = self.le_nascimento.text().upper().strip()
        email = self.le_email.text().upper().strip()
        endereco = self.le_endereo.text().upper().strip()
        numero = self.le_numero.text().upper().strip()
        bairro = self.le_bairro.text().upper().strip()
        cidade = self.le_municipio.text().upper().strip()
        complemento = self.le_complemento.text().upper().strip()
        cep = self.le_cep.text().upper().strip()
        cpf = self.le_cpf.text().upper().strip()
        celular = self.le_celular.text().upper().strip()

        if nome == '':
            self.messagebox_critical('O CAMPO "NOME" ESTA VAZIO')

        elif nome.isnumeric():
            self.messagebox_critical('O CAMPO "NOME" NÃO PODE CONTER NUMEROS')
            self.le_nome.setText('')


        elif cep == '':
            self.messagebox_critical('O CAMPO "CEP" ESTA VAZIO')

        elif cep.isalpha():
            self.messagebox_critical('O CAMPO "CEP" DEVE SER NUMERICO')
            self.le_cep.setText('')

        elif len(cep) != 8:
            self.messagebox_critical('O CAMPO CEP DEVE TER 8 DIGITOS')

        else:
            db.insert_novo_cliente(nome, cep, data, email, endereco, numero, bairro, cidade, complemento, cpf,celular)
            self.reset_tables()
            self.messagebox_accept('CADASTRO REALIZADO COM SUCESSO!')
            self.le_nome.setText('')
            self.le_email.setText('')
            self.le_endereo.setText('')
            self.le_numero.setText('')
            self.le_bairro.setText('')
            self.le_municipio.setText('')
            self.le_complemento.setText('')
            self.le_cep.setText('')
            self.le_cpf.setText('')
            self.le_celular.setText('')
            db.close_conecta()

    def alimenta_cep(self,cep):
        if len(self.le_cep.text()) == 8:
            try:
                ceps = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
                ceps = ceps.json()
                self.le_endereo.setText(f'{ceps["logradouro"]}')
                self.le_bairro.setText(f'{ceps["bairro"]}')
                self.le_municipio.setText(f'{ceps["localidade"]}')
                self.le_complemento.setText(f'{ceps["complemento"]}')
            except:
                self.messagebox_critical('CEP INVÁLIDO')
                self.le_cep.setText('')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()


