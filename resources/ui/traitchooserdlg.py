# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'traitchooserdlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_traitSelectorDlg(object):
    def setupUi(self, traitSelectorDlg):
        traitSelectorDlg.setObjectName("traitSelectorDlg")
        traitSelectorDlg.resize(400, 300)
        self.traitLbl = QtWidgets.QLabel(traitSelectorDlg)
        self.traitLbl.setGeometry(QtCore.QRect(89, 120, 91, 20))
        self.traitLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.traitLbl.setObjectName("traitLbl")
        self.traitCombo = QtWidgets.QComboBox(traitSelectorDlg)
        self.traitCombo.setGeometry(QtCore.QRect(190, 120, 111, 21))
        self.traitCombo.setObjectName("traitCombo")
        self.doneBtn = QtWidgets.QPushButton(traitSelectorDlg)
        self.doneBtn.setGeometry(QtCore.QRect(150, 210, 80, 24))
        self.doneBtn.setObjectName("doneBtn")

        self.retranslateUi(traitSelectorDlg)
        QtCore.QMetaObject.connectSlotsByName(traitSelectorDlg)

    def retranslateUi(self, traitSelectorDlg):
        _translate = QtCore.QCoreApplication.translate
        traitSelectorDlg.setWindowTitle(_translate("traitSelectorDlg", "New Trait"))
        self.traitLbl.setText(_translate("traitSelectorDlg", "Select a Trait:"))
        self.doneBtn.setText(_translate("traitSelectorDlg", "Done"))

