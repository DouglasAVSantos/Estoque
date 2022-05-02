# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(469, 605)
        Login.setMinimumSize(QSize(469, 605))
        Login.setMaximumSize(QSize(469, 605))
        icon = QIcon()
        icon.addFile(u"logo2.png", QSize(), QIcon.Normal, QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.label_4 = QLabel(Login)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 0, 301, 271))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(301, 271))
        self.label_4.setMaximumSize(QSize(301, 271))
        self.label_4.setPixmap(QPixmap(u"logo2.png"))
        self.label_4.setScaledContents(True)
        self.pb_login = QPushButton(Login)
        self.pb_login.setObjectName(u"pb_login")
        self.pb_login.setGeometry(QRect(120, 420, 239, 33))
        font = QFont()
        font.setPointSize(15)
        self.pb_login.setFont(font)
        self.pb_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_login.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(220, 57, 62);\n"
"	\n"
"	color: rgb(77, 11, 17);\n"
"	border-radius: 15px\n"
"\n"
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
        self.lineEdit_senha = QLineEdit(Login)
        self.lineEdit_senha.setObjectName(u"lineEdit_senha")
        self.lineEdit_senha.setGeometry(QRect(140, 350, 201, 20))
        font1 = QFont()
        font1.setPointSize(11)
        self.lineEdit_senha.setFont(font1)
        self.lineEdit_senha.setEchoMode(QLineEdit.Password)
        self.lineEdit_senha.setAlignment(Qt.AlignCenter)
        self.lineEdit_usuario = QLineEdit(Login)
        self.lineEdit_usuario.setObjectName(u"lineEdit_usuario")
        self.lineEdit_usuario.setGeometry(QRect(140, 280, 201, 20))
        self.lineEdit_usuario.setFont(font1)
        self.lineEdit_usuario.setMaxLength(32767)
        self.lineEdit_usuario.setAlignment(Qt.AlignCenter)
        self.lineEdit_usuario.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_usuario.setClearButtonEnabled(False)
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 230, 301, 301))
        self.label.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: rgb(0, 0, 0,0.1);\n"
"	border-radius: 20px\n"
"\n"
"\n"
"\n"
"}")
        self.label_4.raise_()
        self.label.raise_()
        self.label.raise_()
        self.label.raise_()
        self.pb_login.raise_()
        self.lineEdit_senha.raise_()
        self.lineEdit_usuario.raise_()

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Muladhara Login", None))
        self.label_4.setText("")
        self.pb_login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.lineEdit_senha.setInputMask("")
        self.lineEdit_senha.setText("")
        self.lineEdit_senha.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.lineEdit_usuario.setInputMask("")
        self.lineEdit_usuario.setPlaceholderText(QCoreApplication.translate("Login", u"Usuario", None))
        self.label.setText("")
    # retranslateUi

