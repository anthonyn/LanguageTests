# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btnGrid_1 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_1.setGeometry(QtCore.QRect(100, 210, 40, 40))
        self.btnGrid_1.setText("")
        self.btnGrid_1.setCheckable(True)
        self.btnGrid_1.setObjectName("btnGrid_1")
        self.btnGrid_2 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_2.setGeometry(QtCore.QRect(100, 160, 40, 40))
        self.btnGrid_2.setText("")
        self.btnGrid_2.setCheckable(True)
        self.btnGrid_2.setObjectName("btnGrid_2")
        self.btnGrid_3 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_3.setGeometry(QtCore.QRect(100, 110, 40, 40))
        self.btnGrid_3.setText("")
        self.btnGrid_3.setCheckable(True)
        self.btnGrid_3.setObjectName("btnGrid_3")
        self.btnGrid_4 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_4.setGeometry(QtCore.QRect(100, 60, 40, 40))
        self.btnGrid_4.setText("")
        self.btnGrid_4.setCheckable(True)
        self.btnGrid_4.setObjectName("btnGrid_4")
        self.btnGrid_5 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_5.setGeometry(QtCore.QRect(150, 210, 40, 40))
        self.btnGrid_5.setText("")
        self.btnGrid_5.setCheckable(True)
        self.btnGrid_5.setObjectName("btnGrid_5")
        self.btnGrid_6 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_6.setGeometry(QtCore.QRect(150, 160, 40, 40))
        self.btnGrid_6.setText("")
        self.btnGrid_6.setCheckable(True)
        self.btnGrid_6.setObjectName("btnGrid_6")
        self.btnGrid_7 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_7.setGeometry(QtCore.QRect(150, 110, 40, 40))
        self.btnGrid_7.setText("")
        self.btnGrid_7.setCheckable(True)
        self.btnGrid_7.setObjectName("btnGrid_7")
        self.btnGrid_8 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_8.setGeometry(QtCore.QRect(150, 60, 40, 40))
        self.btnGrid_8.setText("")
        self.btnGrid_8.setCheckable(True)
        self.btnGrid_8.setObjectName("btnGrid_8")
        self.btnGrid_10 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_10.setGeometry(QtCore.QRect(200, 160, 40, 40))
        self.btnGrid_10.setText("")
        self.btnGrid_10.setCheckable(True)
        self.btnGrid_10.setObjectName("btnGrid_10")
        self.btnGrid_11 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_11.setGeometry(QtCore.QRect(200, 110, 40, 40))
        self.btnGrid_11.setText("")
        self.btnGrid_11.setCheckable(True)
        self.btnGrid_11.setObjectName("btnGrid_11")
        self.btnGrid_12 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_12.setGeometry(QtCore.QRect(200, 60, 40, 40))
        self.btnGrid_12.setText("")
        self.btnGrid_12.setCheckable(True)
        self.btnGrid_12.setObjectName("btnGrid_12")
        self.btnGrid_13 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_13.setGeometry(QtCore.QRect(250, 210, 40, 40))
        self.btnGrid_13.setText("")
        self.btnGrid_13.setCheckable(True)
        self.btnGrid_13.setObjectName("btnGrid_13")
        self.btnGrid_14 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_14.setGeometry(QtCore.QRect(250, 160, 40, 40))
        self.btnGrid_14.setText("")
        self.btnGrid_14.setCheckable(True)
        self.btnGrid_14.setObjectName("btnGrid_14")
        self.btnGrid_15 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_15.setGeometry(QtCore.QRect(250, 110, 40, 40))
        self.btnGrid_15.setText("")
        self.btnGrid_15.setCheckable(True)
        self.btnGrid_15.setObjectName("btnGrid_15")
        self.btnGrid_16 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_16.setGeometry(QtCore.QRect(250, 60, 40, 40))
        self.btnGrid_16.setText("")
        self.btnGrid_16.setCheckable(True)
        self.btnGrid_16.setObjectName("btnGrid_16")
        self.verticalSliderRed = QtWidgets.QSlider(self.centralWidget)
        self.verticalSliderRed.setGeometry(QtCore.QRect(550, 70, 81, 231))
        self.verticalSliderRed.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.verticalSliderRed.setFocusPolicy(QtCore.Qt.NoFocus)
        self.verticalSliderRed.setMaximum(255)
        self.verticalSliderRed.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderRed.setObjectName("verticalSliderRed")
        self.verticalSliderBlue = QtWidgets.QSlider(self.centralWidget)
        self.verticalSliderBlue.setGeometry(QtCore.QRect(600, 70, 81, 231))
        self.verticalSliderBlue.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.verticalSliderBlue.setFocusPolicy(QtCore.Qt.NoFocus)
        self.verticalSliderBlue.setMaximum(255)
        self.verticalSliderBlue.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderBlue.setObjectName("verticalSliderBlue")
        self.verticalSliderGreen = QtWidgets.QSlider(self.centralWidget)
        self.verticalSliderGreen.setGeometry(QtCore.QRect(650, 70, 81, 231))
        self.verticalSliderGreen.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.verticalSliderGreen.setFocusPolicy(QtCore.Qt.NoFocus)
        self.verticalSliderGreen.setMaximum(255)
        self.verticalSliderGreen.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderGreen.setObjectName("verticalSliderGreen")
        self.btnGrid_9 = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrid_9.setGeometry(QtCore.QRect(200, 210, 40, 40))
        self.btnGrid_9.setText("")
        self.btnGrid_9.setCheckable(True)
        self.btnGrid_9.setObjectName("btnGrid_9")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
