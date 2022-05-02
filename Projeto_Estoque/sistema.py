import sys
from bd_sqlite3 import DataBase
from PySide2.QtWidgets import (QApplication, QMainWindow,QWidget,QMessageBox)
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
        if db.db_check_user(self.lineEdit_usuario.text().upper().strip(),self.lineEdit_senha.text().strip().upper()):
            self.w = MainWindow()
            self.w.show()
            self.close()
            db.close_conecta()
        else:
                    # abre uma caixa de msg com erro
            self.messagebox_critical('LOGIN OU SENHA INVÁLIDOS')
            self.lineEdit_senha.setText('')
            db.close_conecta()

class Produtos(QWidget, Ui_Produtos):
    def __init__(self) -> None:
        super(Produtos,self).__init__()
        self.setupUi(self)

    def add_produto(self):
        pass






# instancia do Sistema
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)

            #**************BOTOES DO SISTEMA*************************
        self.bt_home.clicked.connect(lambda: self.StackedWidget.setCurrentWidget(self.home))
        self.bt_contato.clicked.connect(lambda: self.StackedWidget.setCurrentWidget(self.Contato))
        self.bt_estoque.clicked.connect(lambda: self.StackedWidget.setCurrentWidget(self.estoque))
        self.bt_cadastro.clicked.connect(lambda: self.StackedWidget.setCurrentWidget(self.cadastro))
        self.bt_clientes.clicked.connect(lambda: self.StackedWidget.setCurrentWidget(self.clientes))
        self.bt_novo_usuario.clicked.connect(lambda: self.StackedWidget.setCurrentWidget(self.Cadastro_novo_usuario))

                #BOTAO PARA CADASTRAR CLIENTE NO BANCO DE DADOS
        self.bt_cadastrar.clicked.connect(self.novo_usuario)
        self.bt_cadastrar_usuario.clicked.connect(self.check_senhas)
        self.btn_check_cep.clicked.connect(self.alimenta_cep)

        self.bt_importar.clicked.connect(self.import_produto)

    def import_produto(self):
        self.p = Produtos()
        self.p.show()






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

    def check_senhas(self):
        db = DataBase()
        db.conecta()
        if self.le_senha1.text().upper().strip() != self.le_senha2.text().upper().strip():
            self.messagebox_critical('As senhas informadas não são iguais\nPreencha os campos com as senhas iguais.')
            self.le_senha1.setText('')
            self.le_senha2.setText('')
        elif self.le_senha1.text() == '' and self.le_senha2.text() == '' and self.le_novo_usuario.text() == '':
            self.messagebox_critical('Campos vazios\nPreencha os campos com Usuario e as senhas iguais.')
            self.le_senha1.setText('')
            self.le_senha2.setText('')
        elif db.db_check_user(self.le_novo_usuario.text().upper().strip(), self.le_senha1.text().upper().strip()):
            self.messagebox_critical('Usuario e Senha ja Cadastrado\nPreencha os campos com um novo Usuario e senha')
            self.le_senha1.setText('')
            self.le_senha2.setText('')
            self.le_novo_usuario.setText('')

        else:
            db.insert_novo_usuario(self.le_novo_usuario.text().strip('').upper(),self.le_senha1.text().upper().strip(''))
            self.messagebox_accept('Senha Cadastrada com Sucesso!')
            self.le_senha1.setText('')
            self.le_novo_usuario.setText('')
            self.le_senha2.setText('')
            db.close_conecta()
                #FUNÇÃO QUE ADICIONA UM CADASTRO DE CLIENTE NO BANCO DE DADOS
    def novo_usuario(self):
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

        elif email == '':
            self.messagebox_critical('O campo "EMAIL" está vazio')

        elif '@' not in email:
            self.messagebox_critical('O campo "EMAIL" não possui @ ')

        elif endereco == '':
            self.messagebox_critical('CAMPO "ENDEREÇO" VAZIO')

        elif numero == '':
            self.messagebox_critical('O CAMPO "NUMERO" ESTA VAZIO')

        elif numero.isalpha():
            self.messagebox_critical('O CAMPO "NUMERO" DEVE SER NUMERICO')

        elif bairro == '':
            self.messagebox_critical('CAMPO "BAIRRO" VAZIO')

        elif cidade == '':
            self.messagebox_critical('CAMPO "MUNICIPIO" VAZIO')

        elif cep == '':
            self.messagebox_critical('O CAMPO "CEP" ESTA VAZIO')

        elif cep.isalpha():
            self.messagebox_critical('O CAMPO "CEP" DEVE SER NUMERICO')
            self.le_cep.setText('')

        elif len(cep) != 8:
            self.messagebox_critical('O CAMPO CEP DEVE TER 8 DIGITOS')

        elif cpf == '':
            self.messagebox_critical('O CAMPO "CPF" ESTA VAZIO')

        elif cpf.isalpha():
            self.messagebox_critical('O CAMPO "CPF" DEVE SER NUMERICO')
            self.le_cpf.setText('')

        elif len(cpf) != 11:
            self.messagebox_critical('O CAMPO CPF DEVE TER 11 DIGITOS')

        elif celular == '':
            self.messagebox_critical('O CAMPO "CELULAR" ESTA VAZIO')

        elif celular.isalpha():
            self.messagebox_critical('O CAMPO "CELULAR" DEVE SER NUMERICO')
            self.le_celular.setText('')

        elif len(celular) != 11:
            self.messagebox_critical('O CAMPO "CELULAR" DEVE TER 11 DIGITOS SENDOS OS 2 PRIMEIROS O DDD')

        else:
            db.insert_novo_cliente(nome, data, email, endereco, numero, bairro, cidade, complemento, cep, cpf,celular)
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

    def alimenta_cep(self):
        cep = self.le_cep.text().upper().strip()
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


