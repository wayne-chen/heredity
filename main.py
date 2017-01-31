#!/usr/bin/python3

from resources.mainwindow import Ui_MainWindow
from resources.startdlg import Ui_StartDlg
from resources.errordlg import Ui_ErrorDlg
from PyQt5 import QtCore, QtGui, QtWidgets

import sys

from game import *
# from traits.enumTraits import *

class StartDlg(QtWidgets.QDialog, Ui_StartDlg):
    def __init__(self, parent = None):
        super(StartDlg, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True) 
        self._bUpdatedForm = False 
        self._sexArr = ["Male", "Female"]
        self._monthsArr = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self._monthsArrShortened = [month[:3] for month in self._monthsArr]
        self._yearsArr = []
        [self._yearsArr.append(str(year)) for year in range(1920, 2011)]
        self.monthCombo.currentIndexChanged.connect(self.UpdateDayCombo)
        self.dayCombo.currentIndexChanged.connect(self.UpdateYearCombo)
        self.nameTxt.textChanged.connect(self.UpdateForm)
        self.sexCombo.addItem("")
        self.monthCombo.addItem("")
        self.dayCombo.addItem("")
        self.yearCombo.addItem("")
        self.traitCombo.addItem("")
        
    def UpdateDayCombo(self):
        if self.monthCombo.currentText() in self._monthsArrShortened:
            idx = self._monthsArrShortened.index(self.monthCombo.currentText()) + 1
            if (idx < 8 and idx % 2) or (idx > 7 and not idx % 2):
                self._daysArr = [str(day) for day in range(1, 31 + 1)]  # 31 days in these months
            elif idx != 2:
                self._daysArr = [str(day) for day in range(1, 30 + 1)]  # 30 days in these months
            elif self.yearCombo.currentText() in self._yearsArr and (not self.yearCombo.currentText() % 4):
                self._daysArr = [str(day) for day in range(1, 29 + 1)]  # 29 days in Feb's leap year
            else:
                self._daysArr = [str(day) for day in range(1, 28 + 1)]  # 28 days in Feb's non leap years
            self.dayCombo.clear()
            self.dayCombo.addItem("")
            self.dayCombo.addItems(self._daysArr)

    def UpdateYearCombo(self):
        if self.monthCombo.currentText() in self._monthsArrShortened:
            if self.dayCombo.currentText() in self._daysArr:
                self.yearCombo.clear()
                self.yearCombo.addItems(self._yearsArr)
    
    def UpdateForm(self):
        # updates parts of the form
        if not self._bUpdatedForm:
            self.sexCombo.addItems(self._sexArr)
            self.monthCombo.addItems(self._monthsArrShortened)
            self._bUpdatedForm = True

    def AllFieldsValid(self):
        # make sure everything is filled out properly
        return (self.nameTxt.currentText() != "") and (self.sexCombo.currentText() in self._sexArr) and \
                (self.monthCombo.currentText() in self._monthsArrShortened) and (self.dayCombo.currentText() in self._daysArr) and (self.yearCombo.currentText() in self._yearsArr) and \
                (self.traitCombo.currentText() in self._traitsArr)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

class Manager:
    def __init__(self, args):
        # UI related things.
        self.app = QtWidgets.QApplication(args)
        self.startDlg = StartDlg()
        self.mainWindow = MainWindow()
        self.startDlg.startBtn.clicked.connect(self.LoadMain)
        self._offspringArr = []
        self._player = Player()

    def LoadMain(self):
        if self.startDlg.AllFieldsValid():
            self.startDlg.close()
            self.mainWindow.show()
        else:
            errorDlg = ErrorDlg(self)
            self.errorDlg.setText("Please set all fields properly before continuing.")

    def Start(self):
        # starts the game
        self._turn = 0 

        # UI related.
        self.startDlg.show()

        # execute the UI.
        self.app.exec_()

    def OppositesAttract(self):
        #lets start the nasty
        for offspring in self._offspringArr:
            if offspring.Sex() != self._player._sex:
                return offspring
        return False

    def GetItOn(self, primeMate):
        # algorithm to do the nasty
        # male and female fertility based on ASRM
        # https://www.asrm.org/uploadedFiles/ASRM_Content/Resources/Patient_Resources/Fact_Sheets_and_Info_Booklets/agefertility.pdf
        if primeMate.Sex() == "Female":
            pass 
        else:
            pass
    
    def NewTurn(self):
        self._turn += 1
        # what does a new turn entail?
        # new offspring spawn conditional?
        mate = self.OppositesAttract()
        if mate != False:
            if self.GetItOn(mate):
                pass

class ErrorDlg(QtWidgets.QDialog, Ui_ErrorDlg):
    def __init__(self, parent = None):
        super(ErrorDlg, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.okBtn.clicked.connect(self.close) 

# def main_future():
   # game = Game() 
   # game.Start()

def main():

    mgr = Manager(sys.argv)
    mgr.Start()

if __name__ == "__main__":
    main()
