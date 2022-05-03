# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindown.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1225, 710)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"logo2.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"alternate-background-color: rgb(225, 225, 225);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_12 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius:15px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_home = QPushButton(self.frame)
        self.bt_home.setObjectName(u"bt_home")
        font1 = QFont()
        font1.setFamily(u"Courier")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.bt_home.setFont(font1)
        self.bt_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_home.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.bt_home)

        self.bt_clientes = QPushButton(self.frame)
        self.bt_clientes.setObjectName(u"bt_clientes")
        self.bt_clientes.setFont(font1)
        self.bt_clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_clientes.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.bt_clientes)

        self.bt_estoque = QPushButton(self.frame)
        self.bt_estoque.setObjectName(u"bt_estoque")
        self.bt_estoque.setFont(font1)
        self.bt_estoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_estoque.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.bt_estoque.setAutoDefault(True)

        self.horizontalLayout.addWidget(self.bt_estoque)

        self.bt_cadastro = QPushButton(self.frame)
        self.bt_cadastro.setObjectName(u"bt_cadastro")
        self.bt_cadastro.setFont(font1)
        self.bt_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_cadastro.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.bt_cadastro)

        self.bt_contato = QPushButton(self.frame)
        self.bt_contato.setObjectName(u"bt_contato")
        font2 = QFont()
        font2.setFamily(u"Courier")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        self.bt_contato.setFont(font2)
        self.bt_contato.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_contato.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.bt_contato)


        self.verticalLayout_12.addWidget(self.frame)

        self.StackedWidget = QStackedWidget(self.centralwidget)
        self.StackedWidget.setObjectName(u"StackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_31 = QVBoxLayout(self.home)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label = QLabel(self.home)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"logo2.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_15 = QLabel(self.home)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_2.addWidget(self.label_15)

        self.bt_novo_usuario = QPushButton(self.home)
        self.bt_novo_usuario.setObjectName(u"bt_novo_usuario")
        self.bt_novo_usuario.setMinimumSize(QSize(131, 41))
        self.bt_novo_usuario.setMaximumSize(QSize(131, 41))
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.bt_novo_usuario.setFont(font3)
        self.bt_novo_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_novo_usuario.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.bt_novo_usuario)

        self.label_16 = QLabel(self.home)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_2.addWidget(self.label_16)


        self.verticalLayout_30.addLayout(self.horizontalLayout_2)


        self.verticalLayout_31.addLayout(self.verticalLayout_30)

        self.StackedWidget.addWidget(self.home)
        self.clientes = QWidget()
        self.clientes.setObjectName(u"clientes")
        self.verticalLayout_7 = QVBoxLayout(self.clientes)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_22 = QLabel(self.clientes)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(91, 21))
        self.label_22.setMaximumSize(QSize(91, 21))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_22.setFont(font4)
        self.label_22.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_22)

        self.le_filtro_clientes = QLineEdit(self.clientes)
        self.le_filtro_clientes.setObjectName(u"le_filtro_clientes")
        self.le_filtro_clientes.setStyleSheet(u"border-radius: 8px;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")

        self.horizontalLayout_3.addWidget(self.le_filtro_clientes)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_14 = QLabel(self.clientes)
        self.label_14.setObjectName(u"label_14")
        font5 = QFont()
        font5.setPointSize(15)
        self.label_14.setFont(font5)
        self.label_14.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_14)

        self.tv_clientes = QTableView(self.clientes)
        self.tv_clientes.setObjectName(u"tv_clientes")
        self.tv_clientes.setStyleSheet(u"border-radius: 8px;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")

        self.verticalLayout_27.addWidget(self.tv_clientes)


        self.horizontalLayout_14.addLayout(self.verticalLayout_27)

        self.frame_10 = QFrame(self.clientes)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_10)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.bt_modifica_clientes = QPushButton(self.frame_10)
        self.bt_modifica_clientes.setObjectName(u"bt_modifica_clientes")
        self.bt_modifica_clientes.setMinimumSize(QSize(121, 31))
        self.bt_modifica_clientes.setMaximumSize(QSize(121, 31))
        self.bt_modifica_clientes.setFont(font)
        self.bt_modifica_clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_modifica_clientes.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.verticalLayout_26.addWidget(self.bt_modifica_clientes)

        self.bt_exclui_clientes = QPushButton(self.frame_10)
        self.bt_exclui_clientes.setObjectName(u"bt_exclui_clientes")
        self.bt_exclui_clientes.setMinimumSize(QSize(121, 31))
        self.bt_exclui_clientes.setMaximumSize(QSize(121, 31))
        self.bt_exclui_clientes.setFont(font)
        self.bt_exclui_clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_exclui_clientes.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.verticalLayout_26.addWidget(self.bt_exclui_clientes)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_2)


        self.horizontalLayout_14.addWidget(self.frame_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.StackedWidget.addWidget(self.clientes)
        self.estoque = QWidget()
        self.estoque.setObjectName(u"estoque")
        self.verticalLayout_28 = QVBoxLayout(self.estoque)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_40 = QLabel(self.estoque)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font4)
        self.label_40.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_40)

        self.le_filtro_produtos = QLineEdit(self.estoque)
        self.le_filtro_produtos.setObjectName(u"le_filtro_produtos")
        self.le_filtro_produtos.setMinimumSize(QSize(0, 21))
        self.le_filtro_produtos.setStyleSheet(u"border-radius: 8px;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")

        self.horizontalLayout_13.addWidget(self.le_filtro_produtos)


        self.verticalLayout_20.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.estoque)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.tv_estoque = QTableView(self.estoque)
        self.tv_estoque.setObjectName(u"tv_estoque")
        self.tv_estoque.setStyleSheet(u"border-radius: 8px;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")

        self.verticalLayout_5.addWidget(self.tv_estoque)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.estoque)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.tv_saida = QTableView(self.estoque)
        self.tv_saida.setObjectName(u"tv_saida")
        self.tv_saida.setStyleSheet(u"border-radius: 8px;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")

        self.verticalLayout_4.addWidget(self.tv_saida)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.frame_2 = QFrame(self.estoque)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.bt_importar = QPushButton(self.frame_2)
        self.bt_importar.setObjectName(u"bt_importar")
        self.bt_importar.setMinimumSize(QSize(121, 31))
        self.bt_importar.setMaximumSize(QSize(121, 31))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setWeight(50)
        self.bt_importar.setFont(font6)
        self.bt_importar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_importar.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.bt_importar)

        self.bt_gerar_saida = QPushButton(self.frame_2)
        self.bt_gerar_saida.setObjectName(u"bt_gerar_saida")
        self.bt_gerar_saida.setMinimumSize(QSize(121, 31))
        self.bt_gerar_saida.setMaximumSize(QSize(121, 31))
        self.bt_gerar_saida.setFont(font)
        self.bt_gerar_saida.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_gerar_saida.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.bt_gerar_saida)

        self.bt_extorno = QPushButton(self.frame_2)
        self.bt_extorno.setObjectName(u"bt_extorno")
        self.bt_extorno.setMinimumSize(QSize(121, 31))
        self.bt_extorno.setMaximumSize(QSize(121, 31))
        self.bt_extorno.setFont(font)
        self.bt_extorno.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_extorno.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.bt_extorno)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_20.addLayout(self.horizontalLayout_4)


        self.verticalLayout_28.addLayout(self.verticalLayout_20)

        self.StackedWidget.addWidget(self.estoque)
        self.cadastro = QWidget()
        self.cadastro.setObjectName(u"cadastro")
        self.verticalLayout_16 = QVBoxLayout(self.cadastro)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_4 = QFrame(self.cadastro)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(291, 291))
        self.label_5.setMaximumSize(QSize(291, 291))
        self.label_5.setPixmap(QPixmap(u"logo2.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 111))
        self.label_4.setPixmap(QPixmap(u"NOVO_CLIENTE.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_4)


        self.verticalLayout_16.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.cadastro)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_17)

        self.le_nome = QLineEdit(self.frame_3)
        self.le_nome.setObjectName(u"le_nome")
        self.le_nome.setMinimumSize(QSize(309, 21))
        self.le_nome.setFont(font)
        self.le_nome.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.le_nome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.le_nome)


        self.horizontalLayout_5.addLayout(self.verticalLayout_15)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_18)

        self.le_nascimento = QDateEdit(self.frame_3)
        self.le_nascimento.setObjectName(u"le_nascimento")
        self.le_nascimento.setFont(font)
        self.le_nascimento.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.le_nascimento.setAlignment(Qt.AlignCenter)
        self.le_nascimento.setCalendarPopup(True)

        self.verticalLayout_8.addWidget(self.le_nascimento)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_19)

        self.le_email = QLineEdit(self.frame_3)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setMinimumSize(QSize(289, 21))
        self.le_email.setFont(font)
        self.le_email.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.le_email.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.le_email)


        self.horizontalLayout_5.addLayout(self.verticalLayout_17)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_30 = QLabel(self.frame_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_30)

        self.le_cep = QLineEdit(self.frame_3)
        self.le_cep.setObjectName(u"le_cep")
        self.le_cep.setMinimumSize(QSize(140, 21))
        self.le_cep.setFont(font)
        self.le_cep.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.le_cep.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.le_cep)


        self.horizontalLayout_6.addLayout(self.verticalLayout_10)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_20)

        self.le_endereo = QLineEdit(self.frame_3)
        self.le_endereo.setObjectName(u"le_endereo")
        self.le_endereo.setMinimumSize(QSize(309, 21))
        self.le_endereo.setFont(font)
        self.le_endereo.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.le_endereo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.le_endereo)


        self.horizontalLayout_6.addLayout(self.verticalLayout_18)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(81, 23))
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_23)

        self.le_numero = QLineEdit(self.frame_3)
        self.le_numero.setObjectName(u"le_numero")
        self.le_numero.setMinimumSize(QSize(81, 25))
        self.le_numero.setFont(font)
        self.le_numero.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.le_numero.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.le_numero)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_27 = QLabel(self.frame_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_27)

        self.le_bairro = QLineEdit(self.frame_3)
        self.le_bairro.setObjectName(u"le_bairro")
        self.le_bairro.setMinimumSize(QSize(239, 21))
        self.le_bairro.setFont(font)
        self.le_bairro.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.le_bairro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.le_bairro)


        self.horizontalLayout_6.addLayout(self.verticalLayout_25)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_25 = QLabel(self.frame_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_25)

        self.le_complemento = QLineEdit(self.frame_3)
        self.le_complemento.setObjectName(u"le_complemento")
        self.le_complemento.setMinimumSize(QSize(239, 21))
        self.le_complemento.setFont(font)
        self.le_complemento.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.le_complemento.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.le_complemento)


        self.horizontalLayout_8.addLayout(self.verticalLayout_22)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_21)

        self.le_municipio = QLineEdit(self.frame_3)
        self.le_municipio.setObjectName(u"le_municipio")
        self.le_municipio.setMinimumSize(QSize(140, 21))
        self.le_municipio.setFont(font)
        self.le_municipio.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.le_municipio.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.le_municipio)


        self.horizontalLayout_8.addLayout(self.verticalLayout_19)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_26 = QLabel(self.frame_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_26)

        self.le_cpf = QLineEdit(self.frame_3)
        self.le_cpf.setObjectName(u"le_cpf")
        self.le_cpf.setMinimumSize(QSize(140, 21))
        self.le_cpf.setFont(font)
        self.le_cpf.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.le_cpf.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.le_cpf)


        self.horizontalLayout_8.addLayout(self.verticalLayout_24)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_24 = QLabel(self.frame_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_24)

        self.le_celular = QLineEdit(self.frame_3)
        self.le_celular.setObjectName(u"le_celular")
        self.le_celular.setMinimumSize(QSize(140, 21))
        self.le_celular.setFont(font)
        self.le_celular.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.le_celular.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.le_celular)


        self.horizontalLayout_8.addLayout(self.verticalLayout_21)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)


        self.verticalLayout_16.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.cadastro)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.bt_cadastrar = QPushButton(self.frame_5)
        self.bt_cadastrar.setObjectName(u"bt_cadastrar")
        self.bt_cadastrar.setMinimumSize(QSize(151, 31))
        self.bt_cadastrar.setMaximumSize(QSize(151, 31))
        self.bt_cadastrar.setFont(font1)
        self.bt_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_cadastrar.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.horizontalLayout_9.addWidget(self.bt_cadastrar)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)


        self.verticalLayout_16.addWidget(self.frame_5)

        self.StackedWidget.addWidget(self.cadastro)
        self.Contato = QWidget()
        self.Contato.setObjectName(u"Contato")
        self.verticalLayout_23 = QVBoxLayout(self.Contato)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_6 = QFrame(self.Contato)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_14.addWidget(self.label_10)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        font7 = QFont()
        font7.setPointSize(28)
        self.label_9.setFont(font7)
        self.label_9.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)

        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_14.addWidget(self.label_13)


        self.horizontalLayout_11.addLayout(self.verticalLayout_14)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)


        self.verticalLayout_13.addWidget(self.frame_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_7 = QFrame(self.Contato)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_7)

        self.label_6 = QLabel(self.Contato)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(471, 241))
        self.label_6.setMaximumSize(QSize(471, 241))
        self.label_6.setSizeIncrement(QSize(0, 0))
        self.label_6.setBaseSize(QSize(271, 471))
        self.label_6.setPixmap(QPixmap(u"CONTATO_LOJA.jpeg"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_6)

        self.frame_8 = QFrame(self.Contato)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_8)


        self.verticalLayout_13.addLayout(self.horizontalLayout_10)

        self.frame_9 = QFrame(self.Contato)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.frame_9)


        self.verticalLayout_23.addLayout(self.verticalLayout_13)

        self.StackedWidget.addWidget(self.Contato)
        self.Cadastro_novo_usuario = QWidget()
        self.Cadastro_novo_usuario.setObjectName(u"Cadastro_novo_usuario")
        self.verticalLayout_32 = QVBoxLayout(self.Cadastro_novo_usuario)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_11 = QFrame(self.Cadastro_novo_usuario)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_35 = QLabel(self.frame_11)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(391, 371))
        self.label_35.setMaximumSize(QSize(391, 371))
        self.label_35.setPixmap(QPixmap(u"logo2.png"))
        self.label_35.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_11)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(481, 101))
        self.label_36.setMaximumSize(QSize(481, 101))
        font8 = QFont()
        font8.setFamily(u"Century")
        font8.setPointSize(42)
        self.label_36.setFont(font8)
        self.label_36.setPixmap(QPixmap(u"novo_usuario.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_36)


        self.verticalLayout_32.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.Cadastro_novo_usuario)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_28 = QLabel(self.frame_12)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_15.addWidget(self.label_28)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy2)
        self.frame_13.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_13)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.le_novo_login = QLineEdit(self.frame_13)
        self.le_novo_login.setObjectName(u"le_novo_login")
        self.le_novo_login.setMinimumSize(QSize(151, 20))
        self.le_novo_login.setMaximumSize(QSize(151, 20))
        self.le_novo_login.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.le_novo_login)

        self.le_novo_usuario = QLineEdit(self.frame_13)
        self.le_novo_usuario.setObjectName(u"le_novo_usuario")
        self.le_novo_usuario.setMinimumSize(QSize(151, 20))
        self.le_novo_usuario.setMaximumSize(QSize(151, 20))
        self.le_novo_usuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.le_novo_usuario)

        self.le_senha1 = QLineEdit(self.frame_13)
        self.le_senha1.setObjectName(u"le_senha1")
        self.le_senha1.setMinimumSize(QSize(151, 20))
        self.le_senha1.setMaximumSize(QSize(151, 20))
        self.le_senha1.setEchoMode(QLineEdit.Password)
        self.le_senha1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.le_senha1)

        self.le_senha2 = QLineEdit(self.frame_13)
        self.le_senha2.setObjectName(u"le_senha2")
        self.le_senha2.setMinimumSize(QSize(151, 21))
        self.le_senha2.setMaximumSize(QSize(151, 21))
        self.le_senha2.setEchoMode(QLineEdit.Password)
        self.le_senha2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.le_senha2)

        self.cb_users = QComboBox(self.frame_13)
        self.cb_users.addItem("")
        self.cb_users.addItem("")
        self.cb_users.setObjectName(u"cb_users")
        self.cb_users.setMinimumSize(QSize(151, 20))
        self.cb_users.setMaximumSize(QSize(151, 20))
        self.cb_users.setFont(font)

        self.verticalLayout_33.addWidget(self.cb_users)

        self.bt_cadastrar_usuario = QPushButton(self.frame_13)
        self.bt_cadastrar_usuario.setObjectName(u"bt_cadastrar_usuario")
        self.bt_cadastrar_usuario.setMinimumSize(QSize(151, 31))
        self.bt_cadastrar_usuario.setMaximumSize(QSize(151, 31))
        self.bt_cadastrar_usuario.setFont(font1)
        self.bt_cadastrar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_cadastrar_usuario.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.verticalLayout_33.addWidget(self.bt_cadastrar_usuario)


        self.horizontalLayout_15.addWidget(self.frame_13)

        self.label_29 = QLabel(self.frame_12)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_15.addWidget(self.label_29)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy2.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy2)
        self.frame_14.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_14)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.le_usuario_deletar = QLineEdit(self.frame_14)
        self.le_usuario_deletar.setObjectName(u"le_usuario_deletar")
        self.le_usuario_deletar.setMinimumSize(QSize(151, 20))
        self.le_usuario_deletar.setMaximumSize(QSize(151, 20))
        self.le_usuario_deletar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.le_usuario_deletar)

        self.le_senha_deletar = QLineEdit(self.frame_14)
        self.le_senha_deletar.setObjectName(u"le_senha_deletar")
        self.le_senha_deletar.setMinimumSize(QSize(151, 20))
        self.le_senha_deletar.setMaximumSize(QSize(151, 20))
        self.le_senha_deletar.setEchoMode(QLineEdit.Password)
        self.le_senha_deletar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.le_senha_deletar)

        self.bt_deletar_usuario = QPushButton(self.frame_14)
        self.bt_deletar_usuario.setObjectName(u"bt_deletar_usuario")
        self.bt_deletar_usuario.setMinimumSize(QSize(151, 31))
        self.bt_deletar_usuario.setMaximumSize(QSize(151, 31))
        self.bt_deletar_usuario.setFont(font1)
        self.bt_deletar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_deletar_usuario.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.verticalLayout_29.addWidget(self.bt_deletar_usuario)


        self.horizontalLayout_15.addWidget(self.frame_14)

        self.label_37 = QLabel(self.frame_12)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_15.addWidget(self.label_37)


        self.verticalLayout_32.addWidget(self.frame_12)

        self.StackedWidget.addWidget(self.Cadastro_novo_usuario)

        self.verticalLayout_12.addWidget(self.StackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.StackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Muladhara Store", None))
        self.bt_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.bt_clientes.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.bt_estoque.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        self.bt_cadastro.setText(QCoreApplication.translate("MainWindow", u"CADASTRO", None))
        self.bt_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.label.setText("")
        self.label_15.setText("")
        self.bt_novo_usuario.setText(QCoreApplication.translate("MainWindow", u"NOVO USUARIO", None))
        self.label_16.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Filtro Nome", None))
        self.le_filtro_clientes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"digite o nome para pesquisar...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.bt_modifica_clientes.setText(QCoreApplication.translate("MainWindow", u"MODIFICAR", None))
        self.bt_exclui_clientes.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"FILTRO PRODUTO", None))
        self.le_filtro_produtos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"digite o produto para pesquisar...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SA\u00cdDA", None))
        self.bt_importar.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.bt_gerar_saida.setText(QCoreApplication.translate("MainWindow", u"GERAR SA\u00cdDA", None))
        self.bt_extorno.setText(QCoreApplication.translate("MainWindow", u"EXTORNO", None))
        self.label_5.setText("")
        self.label_4.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.le_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Data de Nascimento", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.le_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.le_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.le_endereo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"N\u00ba", None))
        self.le_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.le_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.le_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Municipio", None))
        self.le_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.le_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Celular", None))
        self.le_celular.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_7.setText("")
        self.bt_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_8.setText("")
        self.label_11.setText("")
        self.label_10.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.label_13.setText("")
        self.label_12.setText("")
        self.label_6.setText("")
        self.label_35.setText("")
        self.label_36.setText("")
        self.label_28.setText("")
        self.le_novo_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.le_novo_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DE USUARIO", None))
        self.le_senha1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.le_senha2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repetir Senha", None))
        self.cb_users.setItemText(0, QCoreApplication.translate("MainWindow", u"user", None))
        self.cb_users.setItemText(1, QCoreApplication.translate("MainWindow", u"admin", None))

        self.bt_cadastrar_usuario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_29.setText("")
        self.le_usuario_deletar.setText("")
        self.le_usuario_deletar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DE USUARIO", None))
        self.le_senha_deletar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha admin", None))
        self.bt_deletar_usuario.setText(QCoreApplication.translate("MainWindow", u"DELETAR", None))
        self.label_37.setText("")
    # retranslateUi

