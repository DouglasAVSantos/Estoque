# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Produtos.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Produtos(object):
    def setupUi(self, Produtos):
        if not Produtos.objectName():
            Produtos.setObjectName(u"Produtos")
        Produtos.resize(895, 587)
        icon = QIcon()
        icon.addFile(u"logo2.png", QSize(), QIcon.Normal, QIcon.Off)
        Produtos.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Produtos)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Produtos)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 161))
        self.frame.setMaximumSize(QSize(16777215, 161))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(201, 181))
        self.label.setMaximumSize(QSize(201, 181))
        self.label.setPixmap(QPixmap(u"logo2.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(633, 91))
        self.label_2.setMaximumSize(QSize(633, 91))
        self.label_2.setPixmap(QPixmap(u"importar_produto.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Produtos)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(151, 23))
        self.label_17.setMaximumSize(QSize(151, 23))
        font = QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_17)

        self.le_produto = QLineEdit(self.frame_2)
        self.le_produto.setObjectName(u"le_produto")
        self.le_produto.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")

        self.horizontalLayout_4.addWidget(self.le_produto)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(151, 23))
        self.label_18.setMaximumSize(QSize(151, 23))
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_18)

        self.comboBox_quantidade = QComboBox(self.frame_2)
        self.comboBox_quantidade.addItem("")
        self.comboBox_quantidade.addItem("")
        self.comboBox_quantidade.addItem("")
        self.comboBox_quantidade.setObjectName(u"comboBox_quantidade")
        self.comboBox_quantidade.setMinimumSize(QSize(69, 22))
        self.comboBox_quantidade.setMaximumSize(QSize(69, 22))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.comboBox_quantidade.setFont(font1)
        self.comboBox_quantidade.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_quantidade.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")

        self.horizontalLayout_3.addWidget(self.comboBox_quantidade)

        self.le_quantidade = QLineEdit(self.frame_2)
        self.le_quantidade.setObjectName(u"le_quantidade")
        self.le_quantidade.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")

        self.horizontalLayout_3.addWidget(self.le_quantidade)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(151, 23))
        self.label_19.setMaximumSize(QSize(151, 23))
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"background-color: rgb(166, 23, 38);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_19)

        self.le_valor = QLineEdit(self.frame_2)
        self.le_valor.setObjectName(u"le_valor")
        self.le_valor.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.le_valor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.le_valor)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Produtos)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 71))
        self.frame_3.setMaximumSize(QSize(16777215, 71))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.bt_novo_produto = QPushButton(self.frame_3)
        self.bt_novo_produto.setObjectName(u"bt_novo_produto")
        self.bt_novo_produto.setMinimumSize(QSize(151, 31))
        self.bt_novo_produto.setMaximumSize(QSize(151, 31))
        font2 = QFont()
        font2.setFamily(u"Courier")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.bt_novo_produto.setFont(font2)
        self.bt_novo_produto.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_novo_produto.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.bt_novo_produto)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Produtos)

        QMetaObject.connectSlotsByName(Produtos)
    # setupUi

    def retranslateUi(self, Produtos):
        Produtos.setWindowTitle(QCoreApplication.translate("Produtos", u"CADASTRO DE PRODUTOS", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_17.setText(QCoreApplication.translate("Produtos", u"PRODUTO", None))
        self.le_produto.setPlaceholderText(QCoreApplication.translate("Produtos", u"produto", None))
        self.label_18.setText(QCoreApplication.translate("Produtos", u"QUANTIDADE", None))
        self.comboBox_quantidade.setItemText(0, QCoreApplication.translate("Produtos", u"KG", None))
        self.comboBox_quantidade.setItemText(1, QCoreApplication.translate("Produtos", u"UN", None))
        self.comboBox_quantidade.setItemText(2, QCoreApplication.translate("Produtos", u"G", None))

        self.le_quantidade.setPlaceholderText(QCoreApplication.translate("Produtos", u"quantidade", None))
        self.label_19.setText(QCoreApplication.translate("Produtos", u"VALOR", None))
        self.le_valor.setPlaceholderText(QCoreApplication.translate("Produtos", u"valor", None))
        self.label_4.setText("")
        self.bt_novo_produto.setText(QCoreApplication.translate("Produtos", u"NOVO PRODUTO", None))
    # retranslateUi

