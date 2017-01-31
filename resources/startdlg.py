# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startdlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StartDlg(object):
    def setupUi(self, StartDlg):
        StartDlg.setObjectName("StartDlg")
        StartDlg.resize(315, 225)
        self.startBtn = QtWidgets.QPushButton(StartDlg)
        self.startBtn.setGeometry(QtCore.QRect(130, 180, 81, 24))
        self.startBtn.setObjectName("startBtn")
        self.nameLbl = QtWidgets.QLabel(StartDlg)
        self.nameLbl.setGeometry(QtCore.QRect(50, 40, 60, 16))
        self.nameLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nameLbl.setObjectName("nameLbl")
        self.sexLbl = QtWidgets.QLabel(StartDlg)
        self.sexLbl.setGeometry(QtCore.QRect(50, 70, 60, 16))
        self.sexLbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sexLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sexLbl.setObjectName("sexLbl")
        self.birthdateLbl = QtWidgets.QLabel(StartDlg)
        self.birthdateLbl.setGeometry(QtCore.QRect(50, 100, 60, 16))
        self.birthdateLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.birthdateLbl.setObjectName("birthdateLbl")
        self.sexCombo = QtWidgets.QComboBox(StartDlg)
        self.sexCombo.setGeometry(QtCore.QRect(130, 70, 79, 21))
        self.sexCombo.setObjectName("sexCombo")
        self.traitLbl = QtWidgets.QLabel(StartDlg)
        self.traitLbl.setGeometry(QtCore.QRect(19, 130, 91, 20))
        self.traitLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.traitLbl.setObjectName("traitLbl")
        self.traitCombo = QtWidgets.QComboBox(StartDlg)
        self.traitCombo.setGeometry(QtCore.QRect(120, 130, 111, 21))
        self.traitCombo.setObjectName("traitCombo")
        self.nameTxt = QtWidgets.QTextEdit(StartDlg)
        self.nameTxt.setGeometry(QtCore.QRect(130, 30, 131, 31))
        self.nameTxt.setObjectName("nameTxt")
        self.monthCombo = QtWidgets.QComboBox(StartDlg)
        self.monthCombo.setGeometry(QtCore.QRect(130, 100, 51, 21))
        self.monthCombo.setObjectName("monthCombo")
        self.dayCombo = QtWidgets.QComboBox(StartDlg)
        self.dayCombo.setGeometry(QtCore.QRect(190, 100, 41, 21))
        self.dayCombo.setObjectName("dayCombo")
        self.yearCombo = QtWidgets.QComboBox(StartDlg)
        self.yearCombo.setGeometry(QtCore.QRect(240, 100, 51, 21))
        self.yearCombo.setObjectName("yearCombo")

        self.retranslateUi(StartDlg)
        QtCore.QMetaObject.connectSlotsByName(StartDlg)

    def retranslateUi(self, StartDlg):
        _translate = QtCore.QCoreApplication.translate
        StartDlg.setWindowTitle(_translate("StartDlg", "Start Page"))
        self.startBtn.setText(_translate("StartDlg", "Start"))
        self.nameLbl.setText(_translate("StartDlg", "Name"))
        self.sexLbl.setText(_translate("StartDlg", "Sex"))
        self.birthdateLbl.setText(_translate("StartDlg", "Birthdate"))
        self.traitLbl.setText(_translate("StartDlg", "Select a Trait:"))

