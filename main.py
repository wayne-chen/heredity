#!/usr/local/bin/python3

from resources.ui.mainwindow import Ui_MainWindow
from resources.ui.startdlg import Ui_StartDlg
from resources.ui.parentsdlg import Ui_ParentsDlg
from resources.ui.errordlg import Ui_ErrorDlg
from PyQt5 import QtCore, QtGui, QtWidgets

import sys

from game import *

def GetMentalPhysicalTraits():
    import json, os
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "/resources/", "traits.json")
    f = open(filename, "r") 
    data = json.loads("".join(f.readlines()))['traits']
    f.close()
    traitsArr = [] 

    for datumId in data:
        if datumId in ["physical", "mental"]:
            for item in data[datumId]:
                traitsArr += [trait for trait in data[datumId][item]]

    return traitsArr

class StartDlg(QtWidgets.QDialog, Ui_StartDlg):
    def __init__(self, parent = None):
        super(StartDlg, self).__init__(parent)
        self.setupUi(self)
        self._bUpdatedForm = False 
        self._sexArr = ["Male", "Female"]
        self._monthsArr = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self._monthsArrShortened = [month[:3] for month in self._monthsArr]
        self._yearsArr = []
        [self._yearsArr.append(str(year)) for year in range(1920, 2011)]
        self._traitsArr = GetMentalPhysicalTraits()
        print(self._traitsArr)
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
            self.traitCombo.addItems(self._traitsArr) 
            self._bUpdatedForm = True

    def AllFieldsValid(self):
        # make sure everything is filled out properly
        return (self.nameTxt.toPlainText() != "") and (self.sexCombo.currentText() in self._sexArr) and \
                (self.monthCombo.currentText() in self._monthsArrShortened) and (self.dayCombo.currentText() in self._daysArr) and (self.yearCombo.currentText() in self._yearsArr) and \
                (self.traitCombo.currentText() in self._traitsArr)

class ParentsDlg(QtWidgets.QDialog, Ui_ParentsDlg):
    def __init__(self, parent = None):
        super(ParentsDlg, self).__init__(parent)
        self.setupUi(self)

    def AllFieldsValid(self):
        return (self.fatherNameTxt.toPlainText() != "") and (self.motherNameTxt.toPlainText() != "")
         
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

class ErrorDlg(QtWidgets.QDialog, Ui_ErrorDlg):
    def __init__(self, parent = None):
        super(ErrorDlg, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.okBtn.clicked.connect(self.close) 

class Manager:
    def __init__(self, args):
        # UI related things.
        self.app = QtWidgets.QApplication(args)
        self.mainWindow = MainWindow()
        self.startDlg = StartDlg(self.mainWindow)
        self.startDlg.nextBtn.clicked.connect(self.LoadParentsDlg)
        self.parentsDlg = ParentsDlg(self.mainWindow)
        self.parentsDlg.prevBtn.clicked.connect(self.RevertStartDlg)
        self.parentsDlg.finishBtn.clicked.connect(self.LoadMainWindow)
        self._offspringArr = []

    def RevertStartDlg(self):
        self.parentsDlg.hide()
        self.startDlg.show()

    def LoadParentsDlg(self):
        self.startDlg.hide()
        self.parentsDlg.show()

    def LoadMainWindow(self):
        if self.startDlg.AllFieldsValid and self.parentsDlg.AllFieldsValid():
            self.startDlg.close()
            self.parentsDlg.close()
            self.mainWindow.show()
            father = Human(name=self.parentsDlg.fatherNameTxt.toPlainText(), sex="male")
            mother = Human(name=self.parentsDlg.motherNameTxt.toPlainText())
            # should the player start at their current age or be born???
            self._player = Player(name=self.startDlg.nameTxt.toPlainText(),sex=self.startDlg.sexCombo.currentText(),parents=[father, mother])
        else:
            errorDlg = ErrorDlg(self)
            errorDlg.setText("Please set all fields properly before continuing.")

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

# def main_future():
   # game = Game() 
   # game.Start()

def main():

    mgr = Manager(sys.argv)
    mgr.Start()

if __name__ == "__main__":
    main()
