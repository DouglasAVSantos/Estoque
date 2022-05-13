import sqlite3
import sys

from PySide2.QtCore import Qt

from bd_sqlite3 import DataBase
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem, QDialog, QInputDialog)
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
        else:
            self.messagebox_critical('LOGIN OU SENHA INVÁLIDOS')
            self.lineEdit_senha.setText('')

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
        self.bt_estoque.clicked.connect(self.reset_table_estoque)
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

        self.tv_estoque.doubleClicked.connect(self.get_produto_via_table)
        # self.bt_gerar_saida.clicked.connect(self.gerar_saida)
        self.le_valor.textChanged.connect(self.mascara_valor)
        self.le_quantidade.textChanged.connect(self.mascara_quantidade)
        self.le_valor.textEdited.connect(self.clear_id)
        self.le_quantidade.textEdited.connect(self.clear_id)
        self.le_produto.textEdited.connect(self.clear_id)

        self.le_valor_saida.setReadOnly(True)
        self.le_produto_saida.setReadOnly(True)
        self.le_ID_produto_saida.setReadOnly(True)
        self.le_ID_produto.setReadOnly(True)
        self.comboBox_un_saida.setEnabled(False)


    def mascara_valor(self,s):
        l = [i for i in s if i.isdigit() or i == ',' or i == '.']
        p = ''
        for i in l:
            p += str(i).strip()
        self.le_valor.setText(f'R${p}')

    def mascara_quantidade(self,s):
        l = [i for i in s if i.isdigit()]
        p = ''
        for i in l:
            p += str(i).strip()
        self.le_quantidade.setText(f'{p}')

    def clear_id(self):
        self.le_ID_produto.clear()



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
            self.messagebox_critical('Usuario não encontrado','Usuario não encontrado')

    def import_produto(self):
        produto = self.le_produto.text()
        user = self.usuario
        ref = self.comboBox_un.currentText()
        quantidade = self.le_quantidade.text()
        quantidade_int = int(quantidade)
        valor = self.le_valor.text().replace(',', '.').replace('R','').replace('$','')
        valor_int = float(valor)
        valor_total = f"{valor_int * quantidade_int:.2f}".replace('.', ',')
        valorstr = self.le_valor.text().replace(',', '.').replace('R','').replace('$','')
        if ref == 'KG':
            db = DataBase()
            db.conecta()
            db.insert_novo_produto(produto, user, valorstr, valor_total, kg=quantidade)
            self.messagebox_accept('PRODUTO CADASTRADO','PRODUTO CADASTRADO COM SUCESSO')
            self.reset_tables()
            self.le_produto.setText('')
            self.le_valor.setText('')
            self.le_quantidade.setText('')
            db.close_conecta()
        elif ref == 'G':
            db = DataBase()
            db.conecta()
            db.insert_novo_produto(produto, user, valorstr, valor_total, g=quantidade)
            self.messagebox_accept('PRODUTO CADASTRADO','PRODUTO CADASTRADO COM SUCESSO')
            self.reset_tables()
            self.le_produto.setText('')
            self.le_valor.setText('')
            self.le_quantidade.setText('')
            db.close_conecta()
        elif ref == 'UN':
            db = DataBase()
            db.conecta()
            db.insert_novo_produto(produto, user, valorstr, valor_total, un=quantidade)
            self.messagebox_accept('PRODUTO CADASTRADO','PRODUTO CADASTRADO COM SUCESSO')
            self.reset_tables()
            self.le_produto.setText('')
            self.le_valor.setText('')
            self.le_quantidade.setText('')
            db.close_conecta()

        #FUNCAO QUE VERIFICA SE AS SENHAS INFORMADAS AO CRIAR UM NOVO USUARIO ESTAO VAZIAS OU NAO SÃO IGUAIS

    def get_produto_via_table(self):
        y = self.tv_estoque.currentIndex()
        x = self.model_estoque.primaryValues(y.row())
        id_produto = x.value('ID_produto')
        db = DataBase()
        db.conecta()
        cursor = db.conection.cursor()
        cursor.execute(f'select * from estoque where ID_PRODUTO = "{id_produto}";')
        for campo in cursor.fetchall():
            id_produto = campo[0]
            produto = campo[1]
            valor = campo[2].replace('R','').replace('$','')
            quantidade_kg = campo[5]
            quantidade_g = campo[6]
            quantidade_un = campo[4]
            ref = '--'
            if quantidade_un == ref and quantidade_g == ref:
                self.comboBox_un.setCurrentIndex(0)
                quantidade = quantidade_kg
            elif quantidade_kg == ref and quantidade_g == ref:
                self.comboBox_un.setCurrentIndex(2)
                quantidade = quantidade_un
            else:
                self.comboBox_un.setCurrentIndex(1)
                quantidade = quantidade_g
            self.le_ID_produto.setText(str(id_produto))
            self.le_produto.setText(produto)
            self.le_valor.setText(valor)
            self.le_quantidade.setText(quantidade)

            db.close_conecta()

    # def gerar_saida(self):
    #     db = DataBase()
    #     db.conecta()
    #     cursor = db.conection.cursor()
    #     id_produto = self.le_ID_produto.text()
    #     cursor.execute(f'select * from estoque where ID_PRODUTO = "{id_produto}";')
    #     for campo in cursor.fetchall():




    def messagebox_critical(self,title, txt):
        msg = QMessageBox(self)
        msg.setIcon(msg.Critical)
        msg.setWindowTitle(title)
        msg.setText(txt)
        msg.exec()

    def messagebox_aviso(self,title, txt):
        msg = QMessageBox(self)
        msg.setIcon(msg.Warning)
        msg.setWindowTitle(title)
        msg.setText(txt)
        msg.exec()

    def messagebox_accept(self,title, txt):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(title)
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
            self.messagebox_critical("Senhas Divergentes",'As senhas informadas não são iguais\nPreencha os campos com as senhas iguais.')
            self.le_senha1.setText('')
            self.le_senha2.setText('')
        elif senha == '' or self.le_senha2.text() == '' or usuario == '' or login == '':
            self.messagebox_critical("Campos vazios",'Preencha os campos com Usuario e as senhas iguais.')
            self.le_senha1.setText('')
            self.le_senha2.setText('')
        elif db.check_login_exists(login, senha):
            self.messagebox_critical('Usuario e Senha ja Cadastrado','Preencha os campos com um novo Usuario e senha')
            self.le_senha1.setText('')
            self.le_senha2.setText('')
            self.le_novo_usuario.setText('')
        else:
            db.insert_novo_usuario(login,usuario,senha,acess)
            self.messagebox_accept('Senha Cadastrada','Senha Cadastrada com Sucesso!')
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
            msg = QMessageBox(self)
            msg.setWindowTitle('DELETAR USUARIO?')
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f'DELETAR O USUARIO : "{self.le_usuario_deletar.text()}"')
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setButtonText(QMessageBox.Yes,'SIM')
            msg.setButtonText(QMessageBox.No,'NÃO')

            r = msg.exec_()
            if r == QMessageBox.Yes:
                db.delete_user(usuario)
                self.messagebox_accept('USUARIO DELETADO','USUARIO DELETADO COM SUCESSO!')
                self.le_usuario_deletar.setText('')
                self.le_senha_deletar.setText('')
                db.close_conecta()
            else:
                pass
        else:
            self.messagebox_aviso("USUARIO NÃO ENCONTRADO",'USUARIO NÃO CADASTRADO')
            self.le_usuario_deletar.setText('')
            self.le_senha_deletar.setText('')
            db.close_conecta()

    def show_table_clientes(self):
        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName('system.db')
        db.open()

        self.model_clientes = QSqlTableModel(db=db)
        self.tv_clientes.setModel(self.model_clientes)
        self.model_clientes.setTable('clientes')
        self.model_clientes.select()
        self.tv_clientes.sortByColumn(0, Qt.AscendingOrder)
        for i in range(0, 9):
            self.tv_clientes.resizeColumnToContents(i)

    def show_table_estoque(self):
        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName('system.db')
        db.open()

        self.model_estoque = QSqlTableModel(db=db)
        self.tv_estoque.setModel(self.model_estoque)
        self.model_estoque.setTable('estoque')
        self.model_estoque.select()
        self.tv_estoque.sortByColumn(0, Qt.AscendingOrder)
        for i in range(0, 9):
            self.tv_estoque.resizeColumnToContents(i)

    def show_table_saida(self):
        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName('system.db')
        db.open()

        self.model_saida = QSqlTableModel(db=db)
        self.tv_saida.setModel(self.model_saida)
        self.model_saida.setTable('saida')
        self.model_saida.select()
        self.tv_saida.sortByColumn(0, Qt.AscendingOrder)
        for i in range(0, 9):
            self.tv_saida.resizeColumnToContents(i)

    def reset_tables(self):
        self.tv_clientes.update()
        self.tv_estoque.update()
        self.tv_saida.update()
        self.show_table_saida()
        self.show_table_estoque()
        self.show_table_clientes()

    def reset_table_estoque(self):
        self.StackedWidget.setCurrentWidget(self.estoque)
        self.reset_tables()

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
            self.messagebox_aviso("CAMPO VAZIO",'O CAMPO "NOME" ESTA VAZIO')

        elif nome.isnumeric():
            self.messagebox_aviso('O CAMPO "NOME" NÃO PODE CONTER NUMEROS')
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


