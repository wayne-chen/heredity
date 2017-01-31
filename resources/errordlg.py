# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errordlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ErrorDlg(object):
    def setupUi(self, ErrorDlg):
        ErrorDlg.setObjectName("ErrorDlg")
        ErrorDlg.resize(370, 71)
        self.okBtn = QtWidgets.QPushButton(ErrorDlg)
        self.okBtn.setGeometry(QtCore.QRect(160, 40, 51, 24))
        self.okBtn.setObjectName("okBtn")
        self.errorLbl = QtWidgets.QLabel(ErrorDlg)
        self.errorLbl.setGeometry(QtCore.QRect(10, 20, 341, 20))
        self.errorLbl.setText("")
        self.errorLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLbl.setObjectName("errorLbl")

        self.retranslateUi(ErrorDlg)
        QtCore.QMetaObject.connectSlotsByName(ErrorDlg)

    def retranslateUi(self, ErrorDlg):
        _translate = QtCore.QCoreApplication.translate
        ErrorDlg.setWindowTitle(_translate("ErrorDlg", "Error"))
        self.okBtn.setText(_translate("ErrorDlg", "OK"))

