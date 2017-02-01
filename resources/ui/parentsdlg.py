# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parentsdlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ParentsDlg(object):
    def setupUi(self, ParentsDlg):
        ParentsDlg.setObjectName("ParentsDlg")
        ParentsDlg.resize(315, 225)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ParentsDlg.sizePolicy().hasHeightForWidth())
        ParentsDlg.setSizePolicy(sizePolicy)
        self.finishBtn = QtWidgets.QPushButton(ParentsDlg)
        self.finishBtn.setGeometry(QtCore.QRect(230, 190, 81, 24))
        self.finishBtn.setObjectName("finishBtn")
        self.prevBtn = QtWidgets.QPushButton(ParentsDlg)
        self.prevBtn.setGeometry(QtCore.QRect(0, 190, 81, 24))
        self.prevBtn.setObjectName("prevBtn")
        self.whoLbl = QtWidgets.QLabel(ParentsDlg)
        self.whoLbl.setGeometry(QtCore.QRect(80, 10, 150, 15))
        self.whoLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.whoLbl.setObjectName("whoLbl")
        self.fatherNameLbl = QtWidgets.QLabel(ParentsDlg)
        self.fatherNameLbl.setGeometry(QtCore.QRect(10, 64, 90, 16))
        self.fatherNameLbl.setObjectName("fatherNameLbl")
        self.motherNameLbl = QtWidgets.QLabel(ParentsDlg)
        self.motherNameLbl.setGeometry(QtCore.QRect(9, 124, 90, 16))
        self.motherNameLbl.setObjectName("motherNameLbl")
        self.fatherNameTxt = QtWidgets.QTextEdit(ParentsDlg)
        self.fatherNameTxt.setGeometry(QtCore.QRect(100, 60, 141, 26))
        self.fatherNameTxt.setObjectName("fatherNameTxt")
        self.motherNameTxt = QtWidgets.QTextEdit(ParentsDlg)
        self.motherNameTxt.setGeometry(QtCore.QRect(100, 120, 141, 26))
        self.motherNameTxt.setObjectName("motherNameTxt")

        self.retranslateUi(ParentsDlg)
        QtCore.QMetaObject.connectSlotsByName(ParentsDlg)

    def retranslateUi(self, ParentsDlg):
        _translate = QtCore.QCoreApplication.translate
        ParentsDlg.setWindowTitle(_translate("ParentsDlg", "Setup"))
        self.finishBtn.setText(_translate("ParentsDlg", "Finish"))
        self.prevBtn.setText(_translate("ParentsDlg", "< Prev"))
        self.whoLbl.setText(_translate("ParentsDlg", "Pick your Parents"))
        self.fatherNameLbl.setText(_translate("ParentsDlg", "Father\'s name"))
        self.motherNameLbl.setText(_translate("ParentsDlg", "Mother\'s name"))

