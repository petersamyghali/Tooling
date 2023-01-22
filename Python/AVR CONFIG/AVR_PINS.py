# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AVR_PINS_CONFIG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import datetime
from lxml import etree as ET

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1081, 912)
        Form.setMinimumSize(QSize(1081, 819))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 760, 731, 41))
        self.Generate_Button = QPushButton(Form)
        self.Generate_Button.setObjectName(u"Generate_Button")
        self.Generate_Button.setGeometry(QRect(810, 770, 93, 28))
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1021, 751))
        self.PORTA = QWidget()
        self.PORTA.setObjectName(u"PORTA")
        self.Input_Group_A1 = QGroupBox(self.PORTA)
        self.Input_Group_A1.setObjectName(u"Input_Group_A1")
        self.Input_Group_A1.setEnabled(False)
        self.Input_Group_A1.setGeometry(QRect(260, 220, 121, 81))
        self.Pull_Up_Radio_A1 = QRadioButton(self.Input_Group_A1)
        self.Pull_Up_Radio_A1.setObjectName(u"Pull_Up_Radio_A1")
        
        self.Pull_Up_Radio_A1.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_A1.setChecked(True)
        
        self.High_Imp_Radio_A1 = QRadioButton(self.Input_Group_A1)
        self.High_Imp_Radio_A1.setObjectName(u"High_Imp_Radio_A1")
        self.High_Imp_Radio_A1.setGeometry(QRect(10, 50, 95, 20))
        self.Output_Group_A3 = QGroupBox(self.PORTA)
        self.Output_Group_A3.setObjectName(u"Output_Group_A3")
        self.Output_Group_A3.setGeometry(QRect(730, 130, 121, 81))
        self.High_Radio_A3 = QRadioButton(self.Output_Group_A3)
        self.High_Radio_A3.setObjectName(u"High_Radio_A3")
        self.High_Radio_A3.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_A3.setChecked(True)
        self.Low_Radio_A3 = QRadioButton(self.Output_Group_A3)
        self.Low_Radio_A3.setObjectName(u"Low_Radio_A3")
        self.Low_Radio_A3.setGeometry(QRect(10, 60, 95, 20))
        self.Pin_0_Group_A3 = QGroupBox(self.PORTA)
        self.Pin_0_Group_A3.setObjectName(u"Pin_0_Group_A3")
        self.Pin_0_Group_A3.setGeometry(QRect(730, 30, 121, 91))
        self.Output_Radio_A3 = QRadioButton(self.Pin_0_Group_A3)
        self.Output_Radio_A3.setObjectName(u"Output_Radio_A3")
        self.Output_Radio_A3.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_A3.setChecked(True)
        self.Input_Radio_A3 = QRadioButton(self.Pin_0_Group_A3)
        self.Input_Radio_A3.setObjectName(u"Input_Radio_A3")
        self.Input_Radio_A3.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_A3.setChecked(False)
        self.Output_Group_A0 = QGroupBox(self.PORTA)
        self.Output_Group_A0.setObjectName(u"Output_Group_A0")
        self.Output_Group_A0.setGeometry(QRect(10, 130, 121, 81))
        self.High_Radio_A0 = QRadioButton(self.Output_Group_A0)
        self.High_Radio_A0.setObjectName(u"High_Radio_A0")
        self.High_Radio_A0.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_A0.setChecked(True)
        self.Low_Radio_A0 = QRadioButton(self.Output_Group_A0)
        self.Low_Radio_A0.setObjectName(u"Low_Radio_A0")
        self.Low_Radio_A0.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_A4 = QGroupBox(self.PORTA)
        self.Input_Group_A4.setObjectName(u"Input_Group_A4")
        self.Input_Group_A4.setEnabled(False)
        self.Input_Group_A4.setGeometry(QRect(30, 540, 121, 81))
        self.Pull_Up_Radio_A4 = QRadioButton(self.Input_Group_A4)
        self.Pull_Up_Radio_A4.setObjectName(u"Pull_Up_Radio_A4")
        
        self.Pull_Up_Radio_A4.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_A4.setChecked(True)
        
        self.High_Imp_Radio_A4 = QRadioButton(self.Input_Group_A4)
        self.High_Imp_Radio_A4.setObjectName(u"High_Imp_Radio_A4")
        self.High_Imp_Radio_A4.setGeometry(QRect(10, 50, 95, 20))
        self.Pin_0_Group_A1 = QGroupBox(self.PORTA)
        self.Pin_0_Group_A1.setObjectName(u"Pin_0_Group_A1")
        self.Pin_0_Group_A1.setGeometry(QRect(260, 30, 121, 91))
        self.Output_Radio_A1 = QRadioButton(self.Pin_0_Group_A1)
        self.Output_Radio_A1.setObjectName(u"Output_Radio_A1")
        self.Output_Radio_A1.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_A1.setChecked(True)
        self.Input_Radio_A1 = QRadioButton(self.Pin_0_Group_A1)
        self.Input_Radio_A1.setObjectName(u"Input_Radio_A1")
        self.Input_Radio_A1.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_A1.setChecked(False)
        self.Pin_0_Group_A5 = QGroupBox(self.PORTA)
        self.Pin_0_Group_A5.setObjectName(u"Pin_0_Group_A5")
        self.Pin_0_Group_A5.setGeometry(QRect(280, 370, 121, 91))
        self.Output_Radio_A5 = QRadioButton(self.Pin_0_Group_A5)
        self.Output_Radio_A5.setObjectName(u"Output_Radio_A5")
        self.Output_Radio_A5.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_A5.setChecked(True)
        self.Input_Radio_A5 = QRadioButton(self.Pin_0_Group_A5)
        self.Input_Radio_A5.setObjectName(u"Input_Radio_A5")
        self.Input_Radio_A5.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_A5.setChecked(False)
        self.Input_Group_A7 = QGroupBox(self.PORTA)
        self.Input_Group_A7.setObjectName(u"Input_Group_A7")
        self.Input_Group_A7.setEnabled(False)
        self.Input_Group_A7.setGeometry(QRect(740, 560, 121, 81))
        self.Pull_Up_Radio_A7 = QRadioButton(self.Input_Group_A7)
        self.Pull_Up_Radio_A7.setObjectName(u"Pull_Up_Radio_A7")
        
        self.Pull_Up_Radio_A7.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_A7.setChecked(True)
        
        self.High_Imp_Radio_A7 = QRadioButton(self.Input_Group_A7)
        self.High_Imp_Radio_A7.setObjectName(u"High_Imp_Radio_A7")
        self.High_Imp_Radio_A7.setGeometry(QRect(10, 50, 95, 20))
        self.Input_Group_A3 = QGroupBox(self.PORTA)
        self.Input_Group_A3.setObjectName(u"Input_Group_A3")
        self.Input_Group_A3.setEnabled(False)
        self.Input_Group_A3.setGeometry(QRect(730, 220, 121, 81))
        self.Pull_Up_Radio_A3 = QRadioButton(self.Input_Group_A3)
        self.Pull_Up_Radio_A3.setObjectName(u"Pull_Up_Radio_A3")
        
        self.Pull_Up_Radio_A3.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_A3.setChecked(True)
        
        self.High_Imp_Radio_A3 = QRadioButton(self.Input_Group_A3)
        self.High_Imp_Radio_A3.setObjectName(u"High_Imp_Radio_A3")
        self.High_Imp_Radio_A3.setGeometry(QRect(10, 50, 95, 20))
        self.Input_Group_A6 = QGroupBox(self.PORTA)
        self.Input_Group_A6.setObjectName(u"Input_Group_A6")
        self.Input_Group_A6.setEnabled(False)
        self.Input_Group_A6.setGeometry(QRect(500, 560, 121, 81))
        self.Pull_Up_Radio_A6 = QRadioButton(self.Input_Group_A6)
        self.Pull_Up_Radio_A6.setObjectName(u"Pull_Up_Radio_A6")
        
        self.Pull_Up_Radio_A6.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_A6.setChecked(True)
        
        self.High_Imp_Radio_A6 = QRadioButton(self.Input_Group_A6)
        self.High_Imp_Radio_A6.setObjectName(u"High_Imp_Radio_A6")
        self.High_Imp_Radio_A6.setGeometry(QRect(10, 50, 95, 20))
        self.Output_Group_A5 = QGroupBox(self.PORTA)
        self.Output_Group_A5.setObjectName(u"Output_Group_A5")
        self.Output_Group_A5.setGeometry(QRect(280, 470, 121, 81))
        self.High_Radio_A5 = QRadioButton(self.Output_Group_A5)
        self.High_Radio_A5.setObjectName(u"High_Radio_A5")
        self.High_Radio_A5.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_A5.setChecked(True)
        self.Low_Radio_A5 = QRadioButton(self.Output_Group_A5)
        self.Low_Radio_A5.setObjectName(u"Low_Radio_A5")
        self.Low_Radio_A5.setGeometry(QRect(10, 60, 95, 20))
        self.Pin_0_Group_A0 = QGroupBox(self.PORTA)
        self.Pin_0_Group_A0.setObjectName(u"Pin_0_Group_A0")
        self.Pin_0_Group_A0.setGeometry(QRect(10, 30, 121, 91))
        self.Output_Radio_A0 = QRadioButton(self.Pin_0_Group_A0)
        self.Output_Radio_A0.setObjectName(u"Output_Radio_A0")
        self.Output_Radio_A0.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_A0.setChecked(True)
        self.Input_Radio_A0 = QRadioButton(self.Pin_0_Group_A0)
        self.Input_Radio_A0.setObjectName(u"Input_Radio_A0")
        self.Input_Radio_A0.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_A0.setChecked(False)
        self.Pin_0_Group_A2 = QGroupBox(self.PORTA)
        self.Pin_0_Group_A2.setObjectName(u"Pin_0_Group_A2")
        self.Pin_0_Group_A2.setGeometry(QRect(500, 30, 121, 91))
        self.Output_Radio_A2 = QRadioButton(self.Pin_0_Group_A2)
        self.Output_Radio_A2.setObjectName(u"Output_Radio_A2")
        self.Output_Radio_A2.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_A2.setChecked(True)
        self.Input_Radio_A2 = QRadioButton(self.Pin_0_Group_A2)
        self.Input_Radio_A2.setObjectName(u"Input_Radio_A2")
        self.Input_Radio_A2.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_A2.setChecked(False)
        self.Pin_0_Group_A6 = QGroupBox(self.PORTA)
        self.Pin_0_Group_A6.setObjectName(u"Pin_0_Group_A6")
        self.Pin_0_Group_A6.setGeometry(QRect(500, 370, 121, 91))
        self.Output_Radio_A6 = QRadioButton(self.Pin_0_Group_A6)
        self.Output_Radio_A6.setObjectName(u"Output_Radio_A6")
        self.Output_Radio_A6.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_A6.setChecked(True)
        self.Input_Radio_A6 = QRadioButton(self.Pin_0_Group_A6)
        self.Input_Radio_A6.setObjectName(u"Input_Radio_A6")
        self.Input_Radio_A6.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_A6.setChecked(False)
        self.Input_Group_A2 = QGroupBox(self.PORTA)
        self.Input_Group_A2.setObjectName(u"Input_Group_A2")
        self.Input_Group_A2.setEnabled(False)
        self.Input_Group_A2.setGeometry(QRect(500, 220, 121, 81))
        self.Pull_Up_Radio_A2 = QRadioButton(self.Input_Group_A2)
        self.Pull_Up_Radio_A2.setObjectName(u"Pull_Up_Radio_A2")
        
        self.Pull_Up_Radio_A2.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_A2.setChecked(True)
        
        self.High_Imp_Radio_A2 = QRadioButton(self.Input_Group_A2)
        self.High_Imp_Radio_A2.setObjectName(u"High_Imp_Radio_A2")
        self.High_Imp_Radio_A2.setGeometry(QRect(10, 50, 95, 20))
        self.Output_Group_A2 = QGroupBox(self.PORTA)
        self.Output_Group_A2.setObjectName(u"Output_Group_A2")
        self.Output_Group_A2.setGeometry(QRect(500, 130, 121, 81))
        self.High_Radio_A2 = QRadioButton(self.Output_Group_A2)
        self.High_Radio_A2.setObjectName(u"High_Radio_A2")
        self.High_Radio_A2.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_A2.setChecked(True)
        self.Low_Radio_A2 = QRadioButton(self.Output_Group_A2)
        self.Low_Radio_A2.setObjectName(u"Low_Radio_A2")
        self.Low_Radio_A2.setGeometry(QRect(10, 60, 95, 20))
        self.Output_Group_A4 = QGroupBox(self.PORTA)
        self.Output_Group_A4.setObjectName(u"Output_Group_A4")
        self.Output_Group_A4.setGeometry(QRect(30, 450, 121, 81))
        self.High_Radio_A4 = QRadioButton(self.Output_Group_A4)
        self.High_Radio_A4.setObjectName(u"High_Radio_A4")
        self.High_Radio_A4.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_A4.setChecked(True)
        self.Low_Radio_A4 = QRadioButton(self.Output_Group_A4)
        self.Low_Radio_A4.setObjectName(u"Low_Radio_A4")
        self.Low_Radio_A4.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_A5 = QGroupBox(self.PORTA)
        self.Input_Group_A5.setObjectName(u"Input_Group_A5")
        self.Input_Group_A5.setEnabled(False)
        self.Input_Group_A5.setGeometry(QRect(280, 560, 121, 81))
        self.Pull_Up_Radio_A5 = QRadioButton(self.Input_Group_A5)
        self.Pull_Up_Radio_A5.setObjectName(u"Pull_Up_Radio_A5")
        
        self.Pull_Up_Radio_A5.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_A5.setChecked(True)
        
        self.High_Imp_Radio_A5 = QRadioButton(self.Input_Group_A5)
        self.High_Imp_Radio_A5.setObjectName(u"High_Imp_Radio_A5")
        self.High_Imp_Radio_A5.setGeometry(QRect(10, 50, 95, 20))
        self.Output_Group_A1 = QGroupBox(self.PORTA)
        self.Output_Group_A1.setObjectName(u"Output_Group_A1")
        self.Output_Group_A1.setGeometry(QRect(260, 130, 121, 81))
        self.High_Radio_A1 = QRadioButton(self.Output_Group_A1)
        self.High_Radio_A1.setObjectName(u"High_Radio_A1")
        self.High_Radio_A1.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_A1.setChecked(True)
        self.Low_Radio_A1 = QRadioButton(self.Output_Group_A1)
        self.Low_Radio_A1.setObjectName(u"Low_Radio_A1")
        self.Low_Radio_A1.setGeometry(QRect(10, 60, 95, 20))
        self.Pin_0_Group_A7 = QGroupBox(self.PORTA)
        self.Pin_0_Group_A7.setObjectName(u"Pin_0_Group_A7")
        self.Pin_0_Group_A7.setGeometry(QRect(740, 370, 121, 91))
        self.Output_Radio_A7 = QRadioButton(self.Pin_0_Group_A7)
        self.Output_Radio_A7.setObjectName(u"Output_Radio_A7")
        self.Output_Radio_A7.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_A7.setChecked(True)
        self.Input_Radio_A7 = QRadioButton(self.Pin_0_Group_A7)
        self.Input_Radio_A7.setObjectName(u"Input_Radio_A7")
        self.Input_Radio_A7.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_A7.setChecked(False)
        self.Output_Group_A6 = QGroupBox(self.PORTA)
        self.Output_Group_A6.setObjectName(u"Output_Group_A6")
        self.Output_Group_A6.setGeometry(QRect(500, 470, 121, 81))
        self.High_Radio_A6 = QRadioButton(self.Output_Group_A6)
        self.High_Radio_A6.setObjectName(u"High_Radio_A6")
        self.High_Radio_A6.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_A6.setChecked(True)
        self.Low_Radio_A6 = QRadioButton(self.Output_Group_A6)
        self.Low_Radio_A6.setObjectName(u"Low_Radio_A6")
        self.Low_Radio_A6.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_A0 = QGroupBox(self.PORTA)
        self.Input_Group_A0.setObjectName(u"Input_Group_A0")
        self.Input_Group_A0.setEnabled(False)
        self.Input_Group_A0.setGeometry(QRect(10, 220, 121, 81))
        self.Pull_Up_Radio_A0 = QRadioButton(self.Input_Group_A0)
        self.Pull_Up_Radio_A0.setObjectName(u"Pull_Up_Radio_A0")
        
        self.Pull_Up_Radio_A0.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_A0.setChecked(True)
        self.Pull_Up_Radio_A0.setAutoRepeat(False)
        self.High_Imp_Radio_A0 = QRadioButton(self.Input_Group_A0)
        self.High_Imp_Radio_A0.setObjectName(u"High_Imp_Radio_A0")
        self.High_Imp_Radio_A0.setGeometry(QRect(10, 50, 95, 20))
        self.Pin_0_Group_A4 = QGroupBox(self.PORTA)
        self.Pin_0_Group_A4.setObjectName(u"Pin_0_Group_A4")
        self.Pin_0_Group_A4.setGeometry(QRect(30, 350, 121, 91))
        self.Output_Radio_A4 = QRadioButton(self.Pin_0_Group_A4)
        self.Output_Radio_A4.setObjectName(u"Output_Radio_A4")
        self.Output_Radio_A4.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_A4.setChecked(True)
        self.Input_Radio_A4 = QRadioButton(self.Pin_0_Group_A4)
        self.Input_Radio_A4.setObjectName(u"Input_Radio_A4")
        self.Input_Radio_A4.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_A4.setChecked(False)
        self.Output_Group_A7 = QGroupBox(self.PORTA)
        self.Output_Group_A7.setObjectName(u"Output_Group_A7")
        self.Output_Group_A7.setGeometry(QRect(740, 470, 121, 81))
        self.High_Radio_A7 = QRadioButton(self.Output_Group_A7)
        self.High_Radio_A7.setObjectName(u"High_Radio_A7")
        self.High_Radio_A7.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_A7.setChecked(True)
        self.Low_Radio_A7 = QRadioButton(self.Output_Group_A7)
        self.Low_Radio_A7.setObjectName(u"Low_Radio_A7")
        self.Low_Radio_A7.setGeometry(QRect(10, 60, 95, 20))
        self.tabWidget.addTab(self.PORTA, "")
        self.PORTB = QWidget()
        self.PORTB.setObjectName(u"PORTB")
        self.Output_Group_B4 = QGroupBox(self.PORTB)
        self.Output_Group_B4.setObjectName(u"Output_Group_B4")
        self.Output_Group_B4.setGeometry(QRect(30, 440, 121, 81))
        self.High_Radio_B4 = QRadioButton(self.Output_Group_B4)
        self.High_Radio_B4.setObjectName(u"High_Radio_B4")
        self.High_Radio_B4.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_B4.setChecked(True)
        self.Low_Radio_B4 = QRadioButton(self.Output_Group_B4)
        self.Low_Radio_B4.setObjectName(u"Low_Radio_B4")
        self.Low_Radio_B4.setGeometry(QRect(10, 60, 95, 20))
        self.Output_Group_B2 = QGroupBox(self.PORTB)
        self.Output_Group_B2.setObjectName(u"Output_Group_B2")
        self.Output_Group_B2.setGeometry(QRect(500, 120, 121, 81))
        self.High_Radio_B2 = QRadioButton(self.Output_Group_B2)
        self.High_Radio_B2.setObjectName(u"High_Radio_B2")
        self.High_Radio_B2.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_B2.setChecked(True)
        self.Low_Radio_B2 = QRadioButton(self.Output_Group_B2)
        self.Low_Radio_B2.setObjectName(u"Low_Radio_B2")
        self.Low_Radio_B2.setGeometry(QRect(10, 60, 95, 20))
        self.Output_Group_B3 = QGroupBox(self.PORTB)
        self.Output_Group_B3.setObjectName(u"Output_Group_B3")
        self.Output_Group_B3.setGeometry(QRect(730, 120, 121, 81))
        self.High_Radio_B3 = QRadioButton(self.Output_Group_B3)
        self.High_Radio_B3.setObjectName(u"High_Radio_B3")
        self.High_Radio_B3.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_B3.setChecked(True)
        self.Low_Radio_B3 = QRadioButton(self.Output_Group_B3)
        self.Low_Radio_B3.setObjectName(u"Low_Radio_B3")
        self.Low_Radio_B3.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_B2 = QGroupBox(self.PORTB)
        self.Input_Group_B2.setObjectName(u"Input_Group_B2")
        self.Input_Group_B2.setEnabled(False)
        self.Input_Group_B2.setGeometry(QRect(500, 210, 121, 81))
        self.Pull_Up_Radio_B2 = QRadioButton(self.Input_Group_B2)
        self.Pull_Up_Radio_B2.setObjectName(u"Pull_Up_Radio_B2")
        
        self.Pull_Up_Radio_B2.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_B2.setChecked(True)
        
        self.High_Imp_Radio_B2 = QRadioButton(self.Input_Group_B2)
        self.High_Imp_Radio_B2.setObjectName(u"High_Imp_Radio_B2")
        self.High_Imp_Radio_B2.setGeometry(QRect(10, 50, 95, 20))
        self.Output_Group_B5 = QGroupBox(self.PORTB)
        self.Output_Group_B5.setObjectName(u"Output_Group_B5")
        self.Output_Group_B5.setGeometry(QRect(280, 460, 121, 81))
        self.High_Radio_B5 = QRadioButton(self.Output_Group_B5)
        self.High_Radio_B5.setObjectName(u"High_Radio_B5")
        self.High_Radio_B5.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_B5.setChecked(True)
        self.Low_Radio_B5 = QRadioButton(self.Output_Group_B5)
        self.Low_Radio_B5.setObjectName(u"Low_Radio_B5")
        self.Low_Radio_B5.setGeometry(QRect(10, 60, 95, 20))
        self.Pin_0_Group_B3 = QGroupBox(self.PORTB)
        self.Pin_0_Group_B3.setObjectName(u"Pin_0_Group_B3")
        self.Pin_0_Group_B3.setGeometry(QRect(730, 20, 121, 91))
        self.Output_Radio_B3 = QRadioButton(self.Pin_0_Group_B3)
        self.Output_Radio_B3.setObjectName(u"Output_Radio_B3")
        self.Output_Radio_B3.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_B3.setChecked(True)
        self.Input_Radio_B3 = QRadioButton(self.Pin_0_Group_B3)
        self.Input_Radio_B3.setObjectName(u"Input_Radio_B3")
        self.Input_Radio_B3.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_B3.setChecked(False)
        self.Input_Group_B7 = QGroupBox(self.PORTB)
        self.Input_Group_B7.setObjectName(u"Input_Group_B7")
        self.Input_Group_B7.setEnabled(False)
        self.Input_Group_B7.setGeometry(QRect(740, 550, 121, 81))
        self.Pull_Up_Radio_B7 = QRadioButton(self.Input_Group_B7)
        self.Pull_Up_Radio_B7.setObjectName(u"Pull_Up_Radio_B7")
        
        self.Pull_Up_Radio_B7.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_B7.setChecked(True)
        
        self.High_Imp_Radio_B7 = QRadioButton(self.Input_Group_B7)
        self.High_Imp_Radio_B7.setObjectName(u"High_Imp_Radio_B7")
        self.High_Imp_Radio_B7.setGeometry(QRect(10, 50, 95, 20))
        self.Pin_0_Group_B4 = QGroupBox(self.PORTB)
        self.Pin_0_Group_B4.setObjectName(u"Pin_0_Group_B4")
        self.Pin_0_Group_B4.setGeometry(QRect(30, 340, 121, 91))
        self.Output_Radio_B4 = QRadioButton(self.Pin_0_Group_B4)
        self.Output_Radio_B4.setObjectName(u"Output_Radio_B4")
        self.Output_Radio_B4.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_B4.setChecked(True)
        self.Input_Radio_B4 = QRadioButton(self.Pin_0_Group_B4)
        self.Input_Radio_B4.setObjectName(u"Input_Radio_B4")
        self.Input_Radio_B4.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_B4.setChecked(False)
        self.Input_Group_B6 = QGroupBox(self.PORTB)
        self.Input_Group_B6.setObjectName(u"Input_Group_B6")
        self.Input_Group_B6.setEnabled(False)
        self.Input_Group_B6.setGeometry(QRect(500, 550, 121, 81))
        self.Pull_Up_Radio_B6 = QRadioButton(self.Input_Group_B6)
        self.Pull_Up_Radio_B6.setObjectName(u"Pull_Up_Radio_B6")
        
        self.Pull_Up_Radio_B6.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_B6.setChecked(True)
        
        self.High_Imp_Radio_B6 = QRadioButton(self.Input_Group_B6)
        self.High_Imp_Radio_B6.setObjectName(u"High_Imp_Radio_B6")
        self.High_Imp_Radio_B6.setGeometry(QRect(10, 50, 95, 20))
        self.Pin_0_Group_B6 = QGroupBox(self.PORTB)
        self.Pin_0_Group_B6.setObjectName(u"Pin_0_Group_B6")
        self.Pin_0_Group_B6.setGeometry(QRect(500, 360, 121, 91))
        self.Output_Radio_B6 = QRadioButton(self.Pin_0_Group_B6)
        self.Output_Radio_B6.setObjectName(u"Output_Radio_B6")
        self.Output_Radio_B6.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_B6.setChecked(True)
        self.Input_Radio_B6 = QRadioButton(self.Pin_0_Group_B6)
        self.Input_Radio_B6.setObjectName(u"Input_Radio_B6")
        self.Input_Radio_B6.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_B6.setChecked(False)
        self.Pin_0_Group_B1 = QGroupBox(self.PORTB)
        self.Pin_0_Group_B1.setObjectName(u"Pin_0_Group_B1")
        self.Pin_0_Group_B1.setGeometry(QRect(260, 20, 121, 91))
        self.Output_Radio_B1 = QRadioButton(self.Pin_0_Group_B1)
        self.Output_Radio_B1.setObjectName(u"Output_Radio_B1")
        self.Output_Radio_B1.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_B1.setChecked(True)
        self.Input_Radio_B1 = QRadioButton(self.Pin_0_Group_B1)
        self.Input_Radio_B1.setObjectName(u"Input_Radio_B1")
        self.Input_Radio_B1.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_B1.setChecked(False)
        self.Pin_0_Group_B5 = QGroupBox(self.PORTB)
        self.Pin_0_Group_B5.setObjectName(u"Pin_0_Group_B5")
        self.Pin_0_Group_B5.setGeometry(QRect(280, 360, 121, 91))
        self.Output_Radio_B5 = QRadioButton(self.Pin_0_Group_B5)
        self.Output_Radio_B5.setObjectName(u"Output_Radio_B5")
        self.Output_Radio_B5.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_B5.setChecked(True)
        self.Input_Radio_B5 = QRadioButton(self.Pin_0_Group_B5)
        self.Input_Radio_B5.setObjectName(u"Input_Radio_B5")
        self.Input_Radio_B5.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_B5.setChecked(False)
        self.Input_Group_B5 = QGroupBox(self.PORTB)
        self.Input_Group_B5.setObjectName(u"Input_Group_B5")
        self.Input_Group_B5.setEnabled(False)
        self.Input_Group_B5.setGeometry(QRect(280, 550, 121, 81))
        self.Pull_Up_Radio_B5 = QRadioButton(self.Input_Group_B5)
        self.Pull_Up_Radio_B5.setObjectName(u"Pull_Up_Radio_B5")
        
        self.Pull_Up_Radio_B5.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_B5.setChecked(True)
        
        self.High_Imp_Radio_B5 = QRadioButton(self.Input_Group_B5)
        self.High_Imp_Radio_B5.setObjectName(u"High_Imp_Radio_B5")
        self.High_Imp_Radio_B5.setGeometry(QRect(10, 50, 95, 20))
        self.Output_Group_B7 = QGroupBox(self.PORTB)
        self.Output_Group_B7.setObjectName(u"Output_Group_B7")
        self.Output_Group_B7.setGeometry(QRect(740, 460, 121, 81))
        self.High_Radio_B7 = QRadioButton(self.Output_Group_B7)
        self.High_Radio_B7.setObjectName(u"High_Radio_B7")
        self.High_Radio_B7.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_B7.setChecked(True)
        self.Low_Radio_B7 = QRadioButton(self.Output_Group_B7)
        self.Low_Radio_B7.setObjectName(u"Low_Radio_B7")
        self.Low_Radio_B7.setGeometry(QRect(10, 60, 95, 20))
        self.Pin_0_Group_B2 = QGroupBox(self.PORTB)
        self.Pin_0_Group_B2.setObjectName(u"Pin_0_Group_B2")
        self.Pin_0_Group_B2.setGeometry(QRect(500, 20, 121, 91))
        self.Output_Radio_B2 = QRadioButton(self.Pin_0_Group_B2)
        self.Output_Radio_B2.setObjectName(u"Output_Radio_B2")
        self.Output_Radio_B2.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_B2.setChecked(True)
        self.Input_Radio_B2 = QRadioButton(self.Pin_0_Group_B2)
        self.Input_Radio_B2.setObjectName(u"Input_Radio_B2")
        self.Input_Radio_B2.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_B2.setChecked(False)
        self.Input_Group_B3 = QGroupBox(self.PORTB)
        self.Input_Group_B3.setObjectName(u"Input_Group_B3")
        self.Input_Group_B3.setEnabled(False)
        self.Input_Group_B3.setGeometry(QRect(730, 210, 121, 81))
        self.Pull_Up_Radio_B3 = QRadioButton(self.Input_Group_B3)
        self.Pull_Up_Radio_B3.setObjectName(u"Pull_Up_Radio_B3")
        
        self.Pull_Up_Radio_B3.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_B3.setChecked(True)
        
        self.High_Imp_Radio_B3 = QRadioButton(self.Input_Group_B3)
        self.High_Imp_Radio_B3.setObjectName(u"High_Imp_Radio_B3")
        self.High_Imp_Radio_B3.setGeometry(QRect(10, 50, 95, 20))
        self.Output_Group_B0 = QGroupBox(self.PORTB)
        self.Output_Group_B0.setObjectName(u"Output_Group_B0")
        self.Output_Group_B0.setGeometry(QRect(10, 120, 121, 81))
        self.High_Radio_B0 = QRadioButton(self.Output_Group_B0)
        self.High_Radio_B0.setObjectName(u"High_Radio_B0")
        self.High_Radio_B0.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_B0.setChecked(True)
        self.Low_Radio_B0 = QRadioButton(self.Output_Group_B0)
        self.Low_Radio_B0.setObjectName(u"Low_Radio_B0")
        self.Low_Radio_B0.setGeometry(QRect(10, 60, 95, 20))
        self.Pin_0_Group_B7 = QGroupBox(self.PORTB)
        self.Pin_0_Group_B7.setObjectName(u"Pin_0_Group_B7")
        self.Pin_0_Group_B7.setGeometry(QRect(740, 360, 121, 91))
        self.Output_Radio_B7 = QRadioButton(self.Pin_0_Group_B7)
        self.Output_Radio_B7.setObjectName(u"Output_Radio_B7")
        self.Output_Radio_B7.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_B7.setChecked(True)
        self.Input_Radio_B7 = QRadioButton(self.Pin_0_Group_B7)
        self.Input_Radio_B7.setObjectName(u"Input_Radio_B7")
        self.Input_Radio_B7.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_B7.setChecked(False)
        self.Pin_0_Group_B0 = QGroupBox(self.PORTB)
        self.Pin_0_Group_B0.setObjectName(u"Pin_0_Group_B0")
        self.Pin_0_Group_B0.setGeometry(QRect(10, 20, 121, 91))
        self.Output_Radio_B0 = QRadioButton(self.Pin_0_Group_B0)
        self.Output_Radio_B0.setObjectName(u"Output_Radio_B0")
        self.Output_Radio_B0.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_B0.setChecked(True)
        self.Input_Radio_B0 = QRadioButton(self.Pin_0_Group_B0)
        self.Input_Radio_B0.setObjectName(u"Input_Radio_B0")
        self.Input_Radio_B0.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_B0.setChecked(False)
        self.Input_Group_B0 = QGroupBox(self.PORTB)
        self.Input_Group_B0.setObjectName(u"Input_Group_B0")
        self.Input_Group_B0.setEnabled(False)
        self.Input_Group_B0.setGeometry(QRect(10, 210, 121, 81))
        self.Pull_Up_Radio_B0 = QRadioButton(self.Input_Group_B0)
        self.Pull_Up_Radio_B0.setObjectName(u"Pull_Up_Radio_B0")
        
        self.Pull_Up_Radio_B0.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_B0.setChecked(True)
        
        self.High_Imp_Radio_B0 = QRadioButton(self.Input_Group_B0)
        self.High_Imp_Radio_B0.setObjectName(u"High_Imp_Radio_B0")
        self.High_Imp_Radio_B0.setGeometry(QRect(10, 50, 95, 20))
        self.Output_Group_B6 = QGroupBox(self.PORTB)
        self.Output_Group_B6.setObjectName(u"Output_Group_B6")
        self.Output_Group_B6.setGeometry(QRect(500, 460, 121, 81))
        self.High_Radio_B6 = QRadioButton(self.Output_Group_B6)
        self.High_Radio_B6.setObjectName(u"High_Radio_B6")
        self.High_Radio_B6.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_B6.setChecked(True)
        self.Low_Radio_B6 = QRadioButton(self.Output_Group_B6)
        self.Low_Radio_B6.setObjectName(u"Low_Radio_B6")
        self.Low_Radio_B6.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_B1 = QGroupBox(self.PORTB)
        self.Input_Group_B1.setObjectName(u"Input_Group_B1")
        self.Input_Group_B1.setEnabled(False)
        self.Input_Group_B1.setGeometry(QRect(260, 210, 121, 81))
        self.Pull_Up_Radio_B1 = QRadioButton(self.Input_Group_B1)
        self.Pull_Up_Radio_B1.setObjectName(u"Pull_Up_Radio_B1")
        
        self.Pull_Up_Radio_B1.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_B1.setChecked(True)
        
        self.High_Imp_Radio_B1 = QRadioButton(self.Input_Group_B1)
        self.High_Imp_Radio_B1.setObjectName(u"High_Imp_Radio_B1")
        self.High_Imp_Radio_B1.setGeometry(QRect(10, 50, 95, 20))
        self.Output_Group_B1 = QGroupBox(self.PORTB)
        self.Output_Group_B1.setObjectName(u"Output_Group_B1")
        self.Output_Group_B1.setGeometry(QRect(260, 120, 121, 81))
        self.High_Radio_B1 = QRadioButton(self.Output_Group_B1)
        self.High_Radio_B1.setObjectName(u"High_Radio_B1")
        self.High_Radio_B1.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_B1.setChecked(True)
        self.Low_Radio_B1 = QRadioButton(self.Output_Group_B1)
        self.Low_Radio_B1.setObjectName(u"Low_Radio_B1")
        self.Low_Radio_B1.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_B4 = QGroupBox(self.PORTB)
        self.Input_Group_B4.setObjectName(u"Input_Group_B4")
        self.Input_Group_B4.setEnabled(False)
        self.Input_Group_B4.setGeometry(QRect(30, 530, 121, 81))
        self.Pull_Up_Radio_B4 = QRadioButton(self.Input_Group_B4)
        self.Pull_Up_Radio_B4.setObjectName(u"Pull_Up_Radio_B4")
        
        self.Pull_Up_Radio_B4.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_B4.setChecked(True)
        
        self.High_Imp_Radio_B4 = QRadioButton(self.Input_Group_B4)
        self.High_Imp_Radio_B4.setObjectName(u"High_Imp_Radio_B4")
        self.High_Imp_Radio_B4.setGeometry(QRect(10, 50, 95, 20))
        self.tabWidget.addTab(self.PORTB, "")
        self.PORTC = QWidget()
        self.PORTC.setObjectName(u"PORTC")
        self.Pin_0_Group_C1 = QGroupBox(self.PORTC)
        self.Pin_0_Group_C1.setObjectName(u"Pin_0_Group_C1")
        self.Pin_0_Group_C1.setGeometry(QRect(290, 30, 121, 91))
        self.Output_Radio_C1 = QRadioButton(self.Pin_0_Group_C1)
        self.Output_Radio_C1.setObjectName(u"Output_Radio_C1")
        self.Output_Radio_C1.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_C1.setChecked(True)
        self.Input_Radio_C1 = QRadioButton(self.Pin_0_Group_C1)
        self.Input_Radio_C1.setObjectName(u"Input_Radio_C1")
        self.Input_Radio_C1.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_C1.setChecked(False)
        self.Pin_0_Group_C3 = QGroupBox(self.PORTC)
        self.Pin_0_Group_C3.setObjectName(u"Pin_0_Group_C3")
        self.Pin_0_Group_C3.setGeometry(QRect(760, 30, 121, 91))
        self.Output_Radio_C3 = QRadioButton(self.Pin_0_Group_C3)
        self.Output_Radio_C3.setObjectName(u"Output_Radio_C3")
        self.Output_Radio_C3.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_C3.setChecked(True)
        self.Input_Radio_C3 = QRadioButton(self.Pin_0_Group_C3)
        self.Input_Radio_C3.setObjectName(u"Input_Radio_C3")
        self.Input_Radio_C3.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_C3.setChecked(False)
        self.Pin_0_Group_C5 = QGroupBox(self.PORTC)
        self.Pin_0_Group_C5.setObjectName(u"Pin_0_Group_C5")
        self.Pin_0_Group_C5.setGeometry(QRect(310, 370, 121, 91))
        self.Output_Radio_C5 = QRadioButton(self.Pin_0_Group_C5)
        self.Output_Radio_C5.setObjectName(u"Output_Radio_C5")
        self.Output_Radio_C5.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_C5.setChecked(True)
        self.Input_Radio_C5 = QRadioButton(self.Pin_0_Group_C5)
        self.Input_Radio_C5.setObjectName(u"Input_Radio_C5")
        self.Input_Radio_C5.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_C5.setChecked(False)
        self.Output_Group_C1 = QGroupBox(self.PORTC)
        self.Output_Group_C1.setObjectName(u"Output_Group_C1")
        self.Output_Group_C1.setGeometry(QRect(290, 130, 121, 81))
        self.High_Radio_C1 = QRadioButton(self.Output_Group_C1)
        self.High_Radio_C1.setObjectName(u"High_Radio_C1")
        self.High_Radio_C1.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_C1.setChecked(True)
        self.Low_Radio_C1 = QRadioButton(self.Output_Group_C1)
        self.Low_Radio_C1.setObjectName(u"Low_Radio_C1")
        self.Low_Radio_C1.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_C2 = QGroupBox(self.PORTC)
        self.Input_Group_C2.setObjectName(u"Input_Group_C2")
        self.Input_Group_C2.setEnabled(False)
        self.Input_Group_C2.setGeometry(QRect(530, 220, 121, 81))
        self.Pull_Up_Radio_C2 = QRadioButton(self.Input_Group_C2)
        self.Pull_Up_Radio_C2.setObjectName(u"Pull_Up_Radio_C2")
        
        self.Pull_Up_Radio_C2.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_C2.setChecked(True)
        
        self.High_Imp_Radio_C2 = QRadioButton(self.Input_Group_C2)
        self.High_Imp_Radio_C2.setObjectName(u"High_Imp_Radio_C2")
        self.High_Imp_Radio_C2.setGeometry(QRect(10, 50, 95, 20))
        self.Output_Group_C3 = QGroupBox(self.PORTC)
        self.Output_Group_C3.setObjectName(u"Output_Group_C3")
        self.Output_Group_C3.setGeometry(QRect(760, 130, 121, 81))
        self.High_Radio_C3 = QRadioButton(self.Output_Group_C3)
        self.High_Radio_C3.setObjectName(u"High_Radio_C3")
        self.High_Radio_C3.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_C3.setChecked(True)
        self.Low_Radio_C3 = QRadioButton(self.Output_Group_C3)
        self.Low_Radio_C3.setObjectName(u"Low_Radio_C3")
        self.Low_Radio_C3.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_C4 = QGroupBox(self.PORTC)
        self.Input_Group_C4.setObjectName(u"Input_Group_C4")
        self.Input_Group_C4.setEnabled(False)
        self.Input_Group_C4.setGeometry(QRect(60, 540, 121, 81))
        self.Pull_Up_Radio_C4 = QRadioButton(self.Input_Group_C4)
        self.Pull_Up_Radio_C4.setObjectName(u"Pull_Up_Radio_C4")
        
        self.Pull_Up_Radio_C4.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_C4.setChecked(True)
        
        self.High_Imp_Radio_C4 = QRadioButton(self.Input_Group_C4)
        self.High_Imp_Radio_C4.setObjectName(u"High_Imp_Radio_C4")
        self.High_Imp_Radio_C4.setGeometry(QRect(10, 50, 95, 20))
        self.PREV_Button = QPushButton(self.PORTC)
        self.PREV_Button.setObjectName(u"PREV_Button")
        self.PREV_Button.setGeometry(QRect(1040, 375, 93, 28))
        self.Input_Group_C1 = QGroupBox(self.PORTC)
        self.Input_Group_C1.setObjectName(u"Input_Group_C1")
        self.Input_Group_C1.setEnabled(False)
        self.Input_Group_C1.setGeometry(QRect(290, 220, 121, 81))
        self.Pull_Up_Radio_C1 = QRadioButton(self.Input_Group_C1)
        self.Pull_Up_Radio_C1.setObjectName(u"Pull_Up_Radio_C1")
        
        self.Pull_Up_Radio_C1.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_C1.setChecked(True)
        
        self.High_Imp_Radio_C1 = QRadioButton(self.Input_Group_C1)
        self.High_Imp_Radio_C1.setObjectName(u"High_Imp_Radio_C1")
        self.High_Imp_Radio_C1.setGeometry(QRect(10, 50, 95, 20))
        self.Input_Group_C7 = QGroupBox(self.PORTC)
        self.Input_Group_C7.setObjectName(u"Input_Group_C7")
        self.Input_Group_C7.setEnabled(False)
        self.Input_Group_C7.setGeometry(QRect(770, 560, 121, 81))
        self.Pull_Up_Radio_C7 = QRadioButton(self.Input_Group_C7)
        self.Pull_Up_Radio_C7.setObjectName(u"Pull_Up_Radio_C7")
        
        self.Pull_Up_Radio_C7.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_C7.setChecked(True)
        
        self.High_Imp_Radio_C7 = QRadioButton(self.Input_Group_C7)
        self.High_Imp_Radio_C7.setObjectName(u"High_Imp_Radio_C7")
        self.High_Imp_Radio_C7.setGeometry(QRect(10, 50, 95, 20))
        self.Output_Group_C5 = QGroupBox(self.PORTC)
        self.Output_Group_C5.setObjectName(u"Output_Group_C5")
        self.Output_Group_C5.setGeometry(QRect(310, 470, 121, 81))
        self.High_Radio_C5 = QRadioButton(self.Output_Group_C5)
        self.High_Radio_C5.setObjectName(u"High_Radio_C5")
        self.High_Radio_C5.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_C5.setChecked(True)
        self.Low_Radio_C5 = QRadioButton(self.Output_Group_C5)
        self.Low_Radio_C5.setObjectName(u"Low_Radio_C5")
        self.Low_Radio_C5.setGeometry(QRect(10, 60, 95, 20))
        self.Output_Group_C0 = QGroupBox(self.PORTC)
        self.Output_Group_C0.setObjectName(u"Output_Group_C0")
        self.Output_Group_C0.setGeometry(QRect(40, 130, 121, 81))
        self.High_Radio_C0 = QRadioButton(self.Output_Group_C0)
        self.High_Radio_C0.setObjectName(u"High_Radio_C0")
        self.High_Radio_C0.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_C0.setChecked(True)
        self.Low_Radio_C0 = QRadioButton(self.Output_Group_C0)
        self.Low_Radio_C0.setObjectName(u"Low_Radio_C0")
        self.Low_Radio_C0.setGeometry(QRect(10, 60, 95, 20))
        self.Output_Group_C6 = QGroupBox(self.PORTC)
        self.Output_Group_C6.setObjectName(u"Output_Group_C6")
        self.Output_Group_C6.setGeometry(QRect(530, 470, 121, 81))
        self.High_Radio_C6 = QRadioButton(self.Output_Group_C6)
        self.High_Radio_C6.setObjectName(u"High_Radio_C6")
        self.High_Radio_C6.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_C6.setChecked(True)
        self.Low_Radio_C6 = QRadioButton(self.Output_Group_C6)
        self.Low_Radio_C6.setObjectName(u"Low_Radio_C6")
        self.Low_Radio_C6.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_C5 = QGroupBox(self.PORTC)
        self.Input_Group_C5.setObjectName(u"Input_Group_C5")
        self.Input_Group_C5.setEnabled(False)
        self.Input_Group_C5.setGeometry(QRect(310, 560, 121, 81))
        self.Pull_Up_Radio_C5 = QRadioButton(self.Input_Group_C5)
        self.Pull_Up_Radio_C5.setObjectName(u"Pull_Up_Radio_C5")
        
        self.Pull_Up_Radio_C5.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_C5.setChecked(True)
        
        self.High_Imp_Radio_C5 = QRadioButton(self.Input_Group_C5)
        self.High_Imp_Radio_C5.setObjectName(u"High_Imp_Radio_C5")
        self.High_Imp_Radio_C5.setGeometry(QRect(10, 50, 95, 20))
        self.Input_Group_C3 = QGroupBox(self.PORTC)
        self.Input_Group_C3.setObjectName(u"Input_Group_C3")
        self.Input_Group_C3.setEnabled(False)
        self.Input_Group_C3.setGeometry(QRect(760, 220, 121, 81))
        self.Pull_Up_Radio_C3 = QRadioButton(self.Input_Group_C3)
        self.Pull_Up_Radio_C3.setObjectName(u"Pull_Up_Radio_C3")
        
        self.Pull_Up_Radio_C3.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_C3.setChecked(True)
        
        self.High_Imp_Radio_C3 = QRadioButton(self.Input_Group_C3)
        self.High_Imp_Radio_C3.setObjectName(u"High_Imp_Radio_C3")
        self.High_Imp_Radio_C3.setGeometry(QRect(10, 50, 95, 20))
        self.Pin_0_Group_C4 = QGroupBox(self.PORTC)
        self.Pin_0_Group_C4.setObjectName(u"Pin_0_Group_C4")
        self.Pin_0_Group_C4.setGeometry(QRect(60, 350, 121, 91))
        self.Output_Radio_C4 = QRadioButton(self.Pin_0_Group_C4)
        self.Output_Radio_C4.setObjectName(u"Output_Radio_C4")
        self.Output_Radio_C4.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_C4.setChecked(True)
        self.Input_Radio_C4 = QRadioButton(self.Pin_0_Group_C4)
        self.Input_Radio_C4.setObjectName(u"Input_Radio_C4")
        self.Input_Radio_C4.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_C4.setChecked(False)
        self.Pin_0_Group_C7 = QGroupBox(self.PORTC)
        self.Pin_0_Group_C7.setObjectName(u"Pin_0_Group_C7")
        self.Pin_0_Group_C7.setGeometry(QRect(770, 370, 121, 91))
        self.Output_Radio_C7 = QRadioButton(self.Pin_0_Group_C7)
        self.Output_Radio_C7.setObjectName(u"Output_Radio_C7")
        self.Output_Radio_C7.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_C7.setChecked(True)
        self.Input_Radio_C7 = QRadioButton(self.Pin_0_Group_C7)
        self.Input_Radio_C7.setObjectName(u"Input_Radio_C7")
        self.Input_Radio_C7.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_C7.setChecked(False)
        self.Output_Group_C4 = QGroupBox(self.PORTC)
        self.Output_Group_C4.setObjectName(u"Output_Group_C4")
        self.Output_Group_C4.setGeometry(QRect(60, 450, 121, 81))
        self.High_Radio_C4 = QRadioButton(self.Output_Group_C4)
        self.High_Radio_C4.setObjectName(u"High_Radio_C4")
        self.High_Radio_C4.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_C4.setChecked(True)
        self.Low_Radio_C4 = QRadioButton(self.Output_Group_C4)
        self.Low_Radio_C4.setObjectName(u"Low_Radio_C4")
        self.Low_Radio_C4.setGeometry(QRect(10, 60, 95, 20))
        self.Output_Group_C7 = QGroupBox(self.PORTC)
        self.Output_Group_C7.setObjectName(u"Output_Group_C7")
        self.Output_Group_C7.setGeometry(QRect(770, 470, 121, 81))
        self.High_Radio_C7 = QRadioButton(self.Output_Group_C7)
        self.High_Radio_C7.setObjectName(u"High_Radio_C7")
        self.High_Radio_C7.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_C7.setChecked(True)
        self.Low_Radio_C7 = QRadioButton(self.Output_Group_C7)
        self.Low_Radio_C7.setObjectName(u"Low_Radio_C7")
        self.Low_Radio_C7.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_C6 = QGroupBox(self.PORTC)
        self.Input_Group_C6.setObjectName(u"Input_Group_C6")
        self.Input_Group_C6.setEnabled(False)
        self.Input_Group_C6.setGeometry(QRect(530, 560, 121, 81))
        self.Pull_Up_Radio_C6 = QRadioButton(self.Input_Group_C6)
        self.Pull_Up_Radio_C6.setObjectName(u"Pull_Up_Radio_C6")
        
        self.Pull_Up_Radio_C6.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_C6.setChecked(True)
        
        self.High_Imp_Radio_C6 = QRadioButton(self.Input_Group_C6)
        self.High_Imp_Radio_C6.setObjectName(u"High_Imp_Radio_C6")
        self.High_Imp_Radio_C6.setGeometry(QRect(10, 50, 95, 20))
        self.Pin_0_Group_C0 = QGroupBox(self.PORTC)
        self.Pin_0_Group_C0.setObjectName(u"Pin_0_Group_C0")
        self.Pin_0_Group_C0.setGeometry(QRect(40, 30, 121, 91))
        self.Output_Radio_C0 = QRadioButton(self.Pin_0_Group_C0)
        self.Output_Radio_C0.setObjectName(u"Output_Radio_C0")
        self.Output_Radio_C0.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_C0.setChecked(True)
        self.Input_Radio_C0 = QRadioButton(self.Pin_0_Group_C0)
        self.Input_Radio_C0.setObjectName(u"Input_Radio_C0")
        self.Input_Radio_C0.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_C0.setChecked(False)
        self.Pin_0_Group_C6 = QGroupBox(self.PORTC)
        self.Pin_0_Group_C6.setObjectName(u"Pin_0_Group_C6")
        self.Pin_0_Group_C6.setGeometry(QRect(530, 370, 121, 91))
        self.Output_Radio_C6 = QRadioButton(self.Pin_0_Group_C6)
        self.Output_Radio_C6.setObjectName(u"Output_Radio_C6")
        self.Output_Radio_C6.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_C6.setChecked(True)
        self.Input_Radio_C6 = QRadioButton(self.Pin_0_Group_C6)
        self.Input_Radio_C6.setObjectName(u"Input_Radio_C6")
        self.Input_Radio_C6.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_C6.setChecked(False)
        self.Pin_0_Group_C2 = QGroupBox(self.PORTC)
        self.Pin_0_Group_C2.setObjectName(u"Pin_0_Group_C2")
        self.Pin_0_Group_C2.setGeometry(QRect(530, 30, 121, 91))
        self.Output_Radio_C2 = QRadioButton(self.Pin_0_Group_C2)
        self.Output_Radio_C2.setObjectName(u"Output_Radio_C2")
        self.Output_Radio_C2.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_C2.setChecked(True)
        self.Input_Radio_C2 = QRadioButton(self.Pin_0_Group_C2)
        self.Input_Radio_C2.setObjectName(u"Input_Radio_C2")
        self.Input_Radio_C2.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_C2.setChecked(False)
        self.Output_Group_C2 = QGroupBox(self.PORTC)
        self.Output_Group_C2.setObjectName(u"Output_Group_C2")
        self.Output_Group_C2.setGeometry(QRect(530, 130, 121, 81))
        self.High_Radio_C2 = QRadioButton(self.Output_Group_C2)
        self.High_Radio_C2.setObjectName(u"High_Radio_C2")
        self.High_Radio_C2.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_C2.setChecked(True)
        self.Low_Radio_C2 = QRadioButton(self.Output_Group_C2)
        self.Low_Radio_C2.setObjectName(u"Low_Radio_C2")
        self.Low_Radio_C2.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_C0 = QGroupBox(self.PORTC)
        self.Input_Group_C0.setObjectName(u"Input_Group_C0")
        self.Input_Group_C0.setEnabled(False)
        self.Input_Group_C0.setGeometry(QRect(40, 220, 121, 81))
        self.Pull_Up_Radio_C0 = QRadioButton(self.Input_Group_C0)
        self.Pull_Up_Radio_C0.setObjectName(u"Pull_Up_Radio_C0")
        
        self.Pull_Up_Radio_C0.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_C0.setChecked(True)
        
        self.High_Imp_Radio_C0 = QRadioButton(self.Input_Group_C0)
        self.High_Imp_Radio_C0.setObjectName(u"High_Imp_Radio_C0")
        self.High_Imp_Radio_C0.setGeometry(QRect(10, 50, 95, 20))
        self.tabWidget.addTab(self.PORTC, "")
        self.PORTD = QWidget()
        self.PORTD.setObjectName(u"PORTD")
        self.PORTS = QWidget(self.PORTD)
        self.PORTS.setObjectName(u"PORTS")
        self.PORTS.setGeometry(QRect(20, 10, 960, 722))
        self.PORTS.setMinimumSize(QSize(960, 722))
        self.Pin_0_Group_D5 = QGroupBox(self.PORTS)
        self.Pin_0_Group_D5.setObjectName(u"Pin_0_Group_D5")
        self.Pin_0_Group_D5.setGeometry(QRect(280, 360, 121, 91))
        self.Output_Radio_D5 = QRadioButton(self.Pin_0_Group_D5)
        self.Output_Radio_D5.setObjectName(u"Output_Radio_D5")
        self.Output_Radio_D5.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_D5.setChecked(True)
        self.Input_Radio_D5 = QRadioButton(self.Pin_0_Group_D5)
        self.Input_Radio_D5.setObjectName(u"Input_Radio_D5")
        self.Input_Radio_D5.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_D5.setChecked(False)
        self.Output_Group_D4 = QGroupBox(self.PORTS)
        self.Output_Group_D4.setObjectName(u"Output_Group_D4")
        self.Output_Group_D4.setGeometry(QRect(30, 440, 121, 81))
        self.High_Radio_D4 = QRadioButton(self.Output_Group_D4)
        self.High_Radio_D4.setObjectName(u"High_Radio_D4")
        self.High_Radio_D4.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_D4.setChecked(True)
        self.Low_Radio_D4 = QRadioButton(self.Output_Group_D4)
        self.Low_Radio_D4.setObjectName(u"Low_Radio_D4")
        self.Low_Radio_D4.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_D1 = QGroupBox(self.PORTS)
        self.Input_Group_D1.setObjectName(u"Input_Group_D1")
        self.Input_Group_D1.setEnabled(False)
        self.Input_Group_D1.setGeometry(QRect(260, 210, 121, 81))
        self.Pull_Up_Radio_D1 = QRadioButton(self.Input_Group_D1)
        self.Pull_Up_Radio_D1.setObjectName(u"Pull_Up_Radio_D1")
        
        self.Pull_Up_Radio_D1.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_D1.setChecked(True)
        
        self.High_Imp_Radio_D1 = QRadioButton(self.Input_Group_D1)
        self.High_Imp_Radio_D1.setObjectName(u"High_Imp_Radio_D1")
        self.High_Imp_Radio_D1.setGeometry(QRect(10, 50, 95, 20))
        self.Output_Group_D5 = QGroupBox(self.PORTS)
        self.Output_Group_D5.setObjectName(u"Output_Group_D5")
        self.Output_Group_D5.setGeometry(QRect(280, 460, 121, 81))
        self.High_Radio_D5 = QRadioButton(self.Output_Group_D5)
        self.High_Radio_D5.setObjectName(u"High_Radio_D5")
        self.High_Radio_D5.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_D5.setChecked(True)
        self.Low_Radio_D5 = QRadioButton(self.Output_Group_D5)
        self.Low_Radio_D5.setObjectName(u"Low_Radio_D5")
        self.Low_Radio_D5.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_D3 = QGroupBox(self.PORTS)
        self.Input_Group_D3.setObjectName(u"Input_Group_D3")
        self.Input_Group_D3.setEnabled(False)
        self.Input_Group_D3.setGeometry(QRect(730, 210, 121, 81))
        self.Pull_Up_Radio_D3 = QRadioButton(self.Input_Group_D3)
        self.Pull_Up_Radio_D3.setObjectName(u"Pull_Up_Radio_D3")
        
        self.Pull_Up_Radio_D3.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_D3.setChecked(True)
        
        self.High_Imp_Radio_D3 = QRadioButton(self.Input_Group_D3)
        self.High_Imp_Radio_D3.setObjectName(u"High_Imp_Radio_D3")
        self.High_Imp_Radio_D3.setGeometry(QRect(10, 50, 95, 20))
        self.Pin_0_Group_D4 = QGroupBox(self.PORTS)
        self.Pin_0_Group_D4.setObjectName(u"Pin_0_Group_D4")
        self.Pin_0_Group_D4.setGeometry(QRect(30, 340, 121, 91))
        self.Output_Radio_D4 = QRadioButton(self.Pin_0_Group_D4)
        self.Output_Radio_D4.setObjectName(u"Output_Radio_D4")
        self.Output_Radio_D4.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_D4.setChecked(True)
        self.Input_Radio_D4 = QRadioButton(self.Pin_0_Group_D4)
        self.Input_Radio_D4.setObjectName(u"Input_Radio_D4")
        self.Input_Radio_D4.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_D4.setChecked(False)
        self.Input_Group_D5 = QGroupBox(self.PORTS)
        self.Input_Group_D5.setObjectName(u"Input_Group_D5")
        self.Input_Group_D5.setEnabled(False)
        self.Input_Group_D5.setGeometry(QRect(280, 550, 121, 81))
        self.Pull_Up_Radio_DD5 = QRadioButton(self.Input_Group_D5)
        self.Pull_Up_Radio_DD5.setObjectName(u"Pull_Up_Radio_DD5")
        self.Pull_Up_Radio_DD5.setEnabled(False)
        self.Pull_Up_Radio_DD5.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_DD5.setChecked(True)
        self.Pull_Up_Radio_DD5.setAutoRepeat(False)
        self.High_Imp_Radio_D5 = QRadioButton(self.Input_Group_D5)
        self.High_Imp_Radio_D5.setObjectName(u"High_Imp_Radio_D5")
        self.High_Imp_Radio_D5.setGeometry(QRect(10, 50, 95, 20))
        self.Pin_0_Group_D7 = QGroupBox(self.PORTS)
        self.Pin_0_Group_D7.setObjectName(u"Pin_0_Group_D7")
        self.Pin_0_Group_D7.setGeometry(QRect(740, 360, 121, 91))
        self.Output_Radio_D7 = QRadioButton(self.Pin_0_Group_D7)
        self.Output_Radio_D7.setObjectName(u"Output_Radio_D7")
        self.Output_Radio_D7.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_D7.setChecked(True)
        self.Input_Radio_D7 = QRadioButton(self.Pin_0_Group_D7)
        self.Input_Radio_D7.setObjectName(u"Input_Radio_D7")
        self.Input_Radio_D7.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_D7.setChecked(False)
        self.Output_Group_D7 = QGroupBox(self.PORTS)
        self.Output_Group_D7.setObjectName(u"Output_Group_D7")
        self.Output_Group_D7.setGeometry(QRect(740, 460, 121, 81))
        self.High_Radio_D7 = QRadioButton(self.Output_Group_D7)
        self.High_Radio_D7.setObjectName(u"High_Radio_D7")
        self.High_Radio_D7.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_D7.setChecked(True)
        self.Low_Radio_D7 = QRadioButton(self.Output_Group_D7)
        self.Low_Radio_D7.setObjectName(u"Low_Radio_D7")
        self.Low_Radio_D7.setGeometry(QRect(10, 60, 95, 20))
        self.Pin_0_Group_D6 = QGroupBox(self.PORTS)
        self.Pin_0_Group_D6.setObjectName(u"Pin_0_Group_D6")
        self.Pin_0_Group_D6.setGeometry(QRect(500, 360, 121, 91))
        self.Output_Radio_D6 = QRadioButton(self.Pin_0_Group_D6)
        self.Output_Radio_D6.setObjectName(u"Output_Radio_D6")
        self.Output_Radio_D6.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_D6.setChecked(True)
        self.Input_Radio_D6 = QRadioButton(self.Pin_0_Group_D6)
        self.Input_Radio_D6.setObjectName(u"Input_Radio_D6")
        self.Input_Radio_D6.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_D6.setChecked(False)
        self.Pin_0_Group_D3 = QGroupBox(self.PORTS)
        self.Pin_0_Group_D3.setObjectName(u"Pin_0_Group_D3")
        self.Pin_0_Group_D3.setGeometry(QRect(730, 20, 121, 91))
        self.Output_Radio_D3 = QRadioButton(self.Pin_0_Group_D3)
        self.Output_Radio_D3.setObjectName(u"Output_Radio_D3")
        self.Output_Radio_D3.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_D3.setChecked(True)
        self.Input_Radio_D3 = QRadioButton(self.Pin_0_Group_D3)
        self.Input_Radio_D3.setObjectName(u"Input_Radio_D3")
        self.Input_Radio_D3.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_D3.setChecked(False)
        self.Input_Group_D2 = QGroupBox(self.PORTS)
        self.Input_Group_D2.setObjectName(u"Input_Group_D2")
        self.Input_Group_D2.setEnabled(False)
        self.Input_Group_D2.setGeometry(QRect(500, 210, 121, 81))
        self.Pull_Up_Radio_D2 = QRadioButton(self.Input_Group_D2)
        self.Pull_Up_Radio_D2.setObjectName(u"Pull_Up_Radio_D2")
        
        self.Pull_Up_Radio_D2.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_D2.setChecked(True)
        
        self.High_Imp_Radio_D2 = QRadioButton(self.Input_Group_D2)
        self.High_Imp_Radio_D2.setObjectName(u"High_Imp_Radio_D2")
        self.High_Imp_Radio_D2.setGeometry(QRect(10, 50, 95, 20))
        self.Pin_0_Group_D1 = QGroupBox(self.PORTS)
        self.Pin_0_Group_D1.setObjectName(u"Pin_0_Group_D1")
        self.Pin_0_Group_D1.setGeometry(QRect(260, 20, 121, 91))
        self.Output_Radio_D1 = QRadioButton(self.Pin_0_Group_D1)
        self.Output_Radio_D1.setObjectName(u"Output_Radio_D1")
        self.Output_Radio_D1.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_D1.setChecked(True)
        self.Input_Radio_D1 = QRadioButton(self.Pin_0_Group_D1)
        self.Input_Radio_D1.setObjectName(u"Input_Radio_D1")
        self.Input_Radio_D1.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_D1.setChecked(False)
        self.Pin_0_Group_D2 = QGroupBox(self.PORTS)
        self.Pin_0_Group_D2.setObjectName(u"Pin_0_Group_D2")
        self.Pin_0_Group_D2.setGeometry(QRect(500, 20, 121, 91))
        self.Output_Radio_D2 = QRadioButton(self.Pin_0_Group_D2)
        self.Output_Radio_D2.setObjectName(u"Output_Radio_D2")
        self.Output_Radio_D2.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_D2.setChecked(True)
        self.Input_Radio_D2 = QRadioButton(self.Pin_0_Group_D2)
        self.Input_Radio_D2.setObjectName(u"Input_Radio_D2")
        self.Input_Radio_D2.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_D2.setChecked(False)
        self.Output_Group_D2 = QGroupBox(self.PORTS)
        self.Output_Group_D2.setObjectName(u"Output_Group_D2")
        self.Output_Group_D2.setGeometry(QRect(500, 120, 121, 81))
        self.High_Radio_D2 = QRadioButton(self.Output_Group_D2)
        self.High_Radio_D2.setObjectName(u"High_Radio_D2")
        self.High_Radio_D2.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_D2.setChecked(True)
        self.Low_Radio_D2 = QRadioButton(self.Output_Group_D2)
        self.Low_Radio_D2.setObjectName(u"Low_Radio_D2")
        self.Low_Radio_D2.setGeometry(QRect(10, 60, 95, 20))
        self.Output_Group_D3 = QGroupBox(self.PORTS)
        self.Output_Group_D3.setObjectName(u"Output_Group_D3")
        self.Output_Group_D3.setGeometry(QRect(730, 120, 121, 81))
        self.High_Radio_D3 = QRadioButton(self.Output_Group_D3)
        self.High_Radio_D3.setObjectName(u"High_Radio_D3")
        self.High_Radio_D3.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_D3.setChecked(True)
        self.Low_Radio_D3 = QRadioButton(self.Output_Group_D3)
        self.Low_Radio_D3.setObjectName(u"Low_Radio_D3")
        self.Low_Radio_D3.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_D7 = QGroupBox(self.PORTS)
        self.Input_Group_D7.setObjectName(u"Input_Group_D7")
        self.Input_Group_D7.setEnabled(False)
        self.Input_Group_D7.setGeometry(QRect(740, 550, 121, 81))
        self.Pull_Up_Radio_D7 = QRadioButton(self.Input_Group_D7)
        self.Pull_Up_Radio_D7.setObjectName(u"Pull_Up_Radio_D7")
        
        self.Pull_Up_Radio_D7.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_D7.setChecked(True)
        
        self.High_Imp_Radio_D7 = QRadioButton(self.Input_Group_D7)
        self.High_Imp_Radio_D7.setObjectName(u"High_Imp_Radio_D7")
        self.High_Imp_Radio_D7.setGeometry(QRect(10, 50, 95, 20))
        self.Input_Group_D6 = QGroupBox(self.PORTS)
        self.Input_Group_D6.setObjectName(u"Input_Group_D6")
        self.Input_Group_D6.setEnabled(False)
        self.Input_Group_D6.setGeometry(QRect(500, 550, 121, 81))
        self.Pull_Up_Radio_D6 = QRadioButton(self.Input_Group_D6)
        self.Pull_Up_Radio_D6.setObjectName(u"Pull_Up_Radio_D6")
        
        self.Pull_Up_Radio_D6.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_D6.setChecked(True)
        
        self.High_Imp_Radio_D6 = QRadioButton(self.Input_Group_D6)
        self.High_Imp_Radio_D6.setObjectName(u"High_Imp_Radio_D6")
        self.High_Imp_Radio_D6.setGeometry(QRect(10, 50, 95, 20))
        self.Output_Group_D0 = QGroupBox(self.PORTS)
        self.Output_Group_D0.setObjectName(u"Output_Group_D0")
        self.Output_Group_D0.setGeometry(QRect(10, 120, 121, 81))
        self.High_Radio_D0 = QRadioButton(self.Output_Group_D0)
        self.High_Radio_D0.setObjectName(u"High_Radio_D0")
        self.High_Radio_D0.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_D0.setChecked(True)
        self.Low_Radio_D0 = QRadioButton(self.Output_Group_D0)
        self.Low_Radio_D0.setObjectName(u"Low_Radio_D0")
        self.Low_Radio_D0.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_D4 = QGroupBox(self.PORTS)
        self.Input_Group_D4.setObjectName(u"Input_Group_D4")
        self.Input_Group_D4.setEnabled(False)
        self.Input_Group_D4.setGeometry(QRect(30, 530, 121, 81))
        self.Pull_Up_Radio_D4 = QRadioButton(self.Input_Group_D4)
        self.Pull_Up_Radio_D4.setObjectName(u"Pull_Up_Radio_D4")
        
        self.Pull_Up_Radio_D4.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_D4.setChecked(True)
        
        self.High_Imp_Radio_D4 = QRadioButton(self.Input_Group_D4)
        self.High_Imp_Radio_D4.setObjectName(u"High_Imp_Radio_D4")
        self.High_Imp_Radio_D4.setGeometry(QRect(10, 50, 95, 20))
        self.Output_Group_D1 = QGroupBox(self.PORTS)
        self.Output_Group_D1.setObjectName(u"Output_Group_D1")
        self.Output_Group_D1.setGeometry(QRect(260, 120, 121, 81))
        self.High_Radio_D1 = QRadioButton(self.Output_Group_D1)
        self.High_Radio_D1.setObjectName(u"High_Radio_D1")
        self.High_Radio_D1.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_D1.setChecked(True)
        self.Low_Radio_D1 = QRadioButton(self.Output_Group_D1)
        self.Low_Radio_D1.setObjectName(u"Low_Radio_D1")
        self.Low_Radio_D1.setGeometry(QRect(10, 60, 95, 20))
        self.Input_Group_D0 = QGroupBox(self.PORTS)
        self.Input_Group_D0.setObjectName(u"Input_Group_D0")
        self.Input_Group_D0.setEnabled(False)
        self.Input_Group_D0.setGeometry(QRect(10, 210, 121, 81))
        self.Pull_Up_Radio_D0 = QRadioButton(self.Input_Group_D0)
        self.Pull_Up_Radio_D0.setObjectName(u"Pull_Up_Radio_D0")
        
        self.Pull_Up_Radio_D0.setGeometry(QRect(10, 30, 95, 20))
        self.Pull_Up_Radio_D0.setChecked(True)
        
        self.High_Imp_Radio_D0 = QRadioButton(self.Input_Group_D0)
        self.High_Imp_Radio_D0.setObjectName(u"High_Imp_Radio_D0")
        self.High_Imp_Radio_D0.setGeometry(QRect(10, 50, 95, 20))
        self.Output_Group_D6 = QGroupBox(self.PORTS)
        self.Output_Group_D6.setObjectName(u"Output_Group_D6")
        self.Output_Group_D6.setGeometry(QRect(500, 460, 121, 81))
        self.High_Radio_D6 = QRadioButton(self.Output_Group_D6)
        self.High_Radio_D6.setObjectName(u"High_Radio_D6")
        self.High_Radio_D6.setGeometry(QRect(10, 30, 95, 20))
        self.High_Radio_D6.setChecked(True)
        self.Low_Radio_D6 = QRadioButton(self.Output_Group_D6)
        self.Low_Radio_D6.setObjectName(u"Low_Radio_D6")
        self.Low_Radio_D6.setGeometry(QRect(10, 60, 95, 20))
        self.Pin_0_Group_D0 = QGroupBox(self.PORTS)
        self.Pin_0_Group_D0.setObjectName(u"Pin_0_Group_D0")
        self.Pin_0_Group_D0.setGeometry(QRect(10, 20, 121, 91))
        self.Output_Radio_D0 = QRadioButton(self.Pin_0_Group_D0)
        self.Output_Radio_D0.setObjectName(u"Output_Radio_D0")
        self.Output_Radio_D0.setGeometry(QRect(10, 30, 95, 20))
        self.Output_Radio_D0.setChecked(True)
        self.Input_Radio_D0 = QRadioButton(self.Pin_0_Group_D0)
        self.Input_Radio_D0.setObjectName(u"Input_Radio_D0")
        self.Input_Radio_D0.setGeometry(QRect(10, 70, 95, 20))
        self.Input_Radio_D0.setChecked(False)
        self.tabWidget.addTab(self.PORTD, "")
        self.Save_Button = QPushButton(Form)
        self.Save_Button.setObjectName(u"Save_Button")
        self.Save_Button.setGeometry(QRect(810, 820, 93, 28))
        self.Load_Button = QPushButton(Form)
        self.Load_Button.setObjectName(u"Load_Button")
        self.Load_Button.setGeometry(QRect(810, 880, 93, 28))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(60, 820, 731, 41))
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(50, 870, 731, 41))

        self.retranslateUi(Form)
        
        QObject.connect(self.Output_Radio_A0,SIGNAL("clicked(bool)"),self.Input_Group_A0.setDisabled)
        QObject.connect(self.Output_Radio_A0,SIGNAL("clicked(bool)"),self.Output_Group_A0.setEnabled)
        QObject.connect(self.Input_Radio_A0,SIGNAL("clicked(bool)"),self.Output_Group_A0.setDisabled)
        QObject.connect(self.Input_Radio_A0,SIGNAL("clicked(bool)"),self.Input_Group_A0.setEnabled)
        
        QObject.connect(self.Output_Radio_A1,SIGNAL("clicked(bool)"),self.Input_Group_A1.setDisabled)
        QObject.connect(self.Output_Radio_A1,SIGNAL("clicked(bool)"),self.Output_Group_A1.setEnabled)
        QObject.connect(self.Input_Radio_A1,SIGNAL("clicked(bool)"),self.Output_Group_A1.setDisabled)
        QObject.connect(self.Input_Radio_A1,SIGNAL("clicked(bool)"),self.Input_Group_A1.setEnabled)
        
        QObject.connect(self.Output_Radio_A2,SIGNAL("clicked(bool)"),self.Input_Group_A2.setDisabled)
        QObject.connect(self.Output_Radio_A2,SIGNAL("clicked(bool)"),self.Output_Group_A2.setEnabled)
        QObject.connect(self.Input_Radio_A2,SIGNAL("clicked(bool)"),self.Output_Group_A2.setDisabled)
        QObject.connect(self.Input_Radio_A2,SIGNAL("clicked(bool)"),self.Input_Group_A2.setEnabled)
        
        QObject.connect(self.Output_Radio_A3,SIGNAL("clicked(bool)"),self.Input_Group_A3.setDisabled)
        QObject.connect(self.Output_Radio_A3,SIGNAL("clicked(bool)"),self.Output_Group_A3.setEnabled)
        QObject.connect(self.Input_Radio_A3,SIGNAL("clicked(bool)"),self.Output_Group_A3.setDisabled)
        QObject.connect(self.Input_Radio_A3,SIGNAL("clicked(bool)"),self.Input_Group_A3.setEnabled)
        
        QObject.connect(self.Output_Radio_A4,SIGNAL("clicked(bool)"),self.Input_Group_A4.setDisabled)
        QObject.connect(self.Output_Radio_A4,SIGNAL("clicked(bool)"),self.Output_Group_A4.setEnabled)
        QObject.connect(self.Input_Radio_A4,SIGNAL("clicked(bool)"),self.Output_Group_A4.setDisabled)
        QObject.connect(self.Input_Radio_A4,SIGNAL("clicked(bool)"),self.Input_Group_A4.setEnabled)
        
        QObject.connect(self.Output_Radio_A5,SIGNAL("clicked(bool)"),self.Input_Group_A5.setDisabled)
        QObject.connect(self.Output_Radio_A5,SIGNAL("clicked(bool)"),self.Output_Group_A5.setEnabled)
        QObject.connect(self.Input_Radio_A5,SIGNAL("clicked(bool)"),self.Output_Group_A5.setDisabled)
        QObject.connect(self.Input_Radio_A5,SIGNAL("clicked(bool)"),self.Input_Group_A5.setEnabled)
        
        QObject.connect(self.Output_Radio_A6,SIGNAL("clicked(bool)"),self.Input_Group_A6.setDisabled)
        QObject.connect(self.Output_Radio_A6,SIGNAL("clicked(bool)"),self.Output_Group_A6.setEnabled)
        QObject.connect(self.Input_Radio_A6,SIGNAL("clicked(bool)"),self.Output_Group_A6.setDisabled)
        QObject.connect(self.Input_Radio_A6,SIGNAL("clicked(bool)"),self.Input_Group_A6.setEnabled)
        
        QObject.connect(self.Output_Radio_A7,SIGNAL("clicked(bool)"),self.Input_Group_A7.setDisabled)
        QObject.connect(self.Output_Radio_A7,SIGNAL("clicked(bool)"),self.Output_Group_A7.setEnabled)
        QObject.connect(self.Input_Radio_A7,SIGNAL("clicked(bool)"),self.Output_Group_A7.setDisabled)
        QObject.connect(self.Input_Radio_A7,SIGNAL("clicked(bool)"),self.Input_Group_A7.setEnabled)
        
        QObject.connect(self.Output_Radio_B0,SIGNAL("clicked(bool)"),self.Input_Group_B0.setDisabled)
        QObject.connect(self.Output_Radio_B0,SIGNAL("clicked(bool)"),self.Output_Group_B0.setEnabled)
        QObject.connect(self.Input_Radio_B0,SIGNAL("clicked(bool)"),self.Output_Group_B0.setDisabled)
        QObject.connect(self.Input_Radio_B0,SIGNAL("clicked(bool)"),self.Input_Group_B0.setEnabled)
        
        QObject.connect(self.Output_Radio_B1,SIGNAL("clicked(bool)"),self.Input_Group_B1.setDisabled)
        QObject.connect(self.Output_Radio_B1,SIGNAL("clicked(bool)"),self.Output_Group_B1.setEnabled)
        QObject.connect(self.Input_Radio_B1,SIGNAL("clicked(bool)"),self.Output_Group_B1.setDisabled)
        QObject.connect(self.Input_Radio_B1,SIGNAL("clicked(bool)"),self.Input_Group_B1.setEnabled)
        
        QObject.connect(self.Output_Radio_B2,SIGNAL("clicked(bool)"),self.Input_Group_B2.setDisabled)
        QObject.connect(self.Output_Radio_B2,SIGNAL("clicked(bool)"),self.Output_Group_B2.setEnabled)
        QObject.connect(self.Input_Radio_B2,SIGNAL("clicked(bool)"),self.Output_Group_B2.setDisabled)
        QObject.connect(self.Input_Radio_B2,SIGNAL("clicked(bool)"),self.Input_Group_B2.setEnabled)
        
        QObject.connect(self.Output_Radio_B3,SIGNAL("clicked(bool)"),self.Input_Group_B3.setDisabled)
        QObject.connect(self.Output_Radio_B3,SIGNAL("clicked(bool)"),self.Output_Group_B3.setEnabled)
        QObject.connect(self.Input_Radio_B3,SIGNAL("clicked(bool)"),self.Output_Group_B3.setDisabled)
        QObject.connect(self.Input_Radio_B3,SIGNAL("clicked(bool)"),self.Input_Group_B3.setEnabled)
        
        QObject.connect(self.Output_Radio_B4,SIGNAL("clicked(bool)"),self.Input_Group_B4.setDisabled)
        QObject.connect(self.Output_Radio_B4,SIGNAL("clicked(bool)"),self.Output_Group_B4.setEnabled)
        QObject.connect(self.Input_Radio_B4,SIGNAL("clicked(bool)"),self.Output_Group_B4.setDisabled)
        QObject.connect(self.Input_Radio_B4,SIGNAL("clicked(bool)"),self.Input_Group_B4.setEnabled)
        
        QObject.connect(self.Output_Radio_B5,SIGNAL("clicked(bool)"),self.Input_Group_B5.setDisabled)
        QObject.connect(self.Output_Radio_B5,SIGNAL("clicked(bool)"),self.Output_Group_B5.setEnabled)
        QObject.connect(self.Input_Radio_B5,SIGNAL("clicked(bool)"),self.Output_Group_B5.setDisabled)
        QObject.connect(self.Input_Radio_B5,SIGNAL("clicked(bool)"),self.Input_Group_B5.setEnabled)
        
        QObject.connect(self.Output_Radio_B6,SIGNAL("clicked(bool)"),self.Input_Group_B6.setDisabled)
        QObject.connect(self.Output_Radio_B6,SIGNAL("clicked(bool)"),self.Output_Group_B6.setEnabled)
        QObject.connect(self.Input_Radio_B6,SIGNAL("clicked(bool)"),self.Output_Group_B6.setDisabled)
        QObject.connect(self.Input_Radio_B6,SIGNAL("clicked(bool)"),self.Input_Group_B6.setEnabled)
        
        QObject.connect(self.Output_Radio_B7,SIGNAL("clicked(bool)"),self.Input_Group_B7.setDisabled)
        QObject.connect(self.Output_Radio_B7,SIGNAL("clicked(bool)"),self.Output_Group_B7.setEnabled)
        QObject.connect(self.Input_Radio_B7,SIGNAL("clicked(bool)"),self.Output_Group_B7.setDisabled)
        QObject.connect(self.Input_Radio_B7,SIGNAL("clicked(bool)"),self.Input_Group_B7.setEnabled)
        
        QObject.connect(self.Output_Radio_C0,SIGNAL("clicked(bool)"),self.Input_Group_C0.setDisabled)
        QObject.connect(self.Output_Radio_C0,SIGNAL("clicked(bool)"),self.Output_Group_C0.setEnabled)
        QObject.connect(self.Input_Radio_C0,SIGNAL("clicked(bool)"),self.Output_Group_C0.setDisabled)
        QObject.connect(self.Input_Radio_C0,SIGNAL("clicked(bool)"),self.Input_Group_C0.setEnabled)
        
        QObject.connect(self.Output_Radio_C1,SIGNAL("clicked(bool)"),self.Input_Group_C1.setDisabled)
        QObject.connect(self.Output_Radio_C1,SIGNAL("clicked(bool)"),self.Output_Group_C1.setEnabled)
        QObject.connect(self.Input_Radio_C1,SIGNAL("clicked(bool)"),self.Output_Group_C1.setDisabled)
        QObject.connect(self.Input_Radio_C1,SIGNAL("clicked(bool)"),self.Input_Group_C1.setEnabled)
        
        QObject.connect(self.Output_Radio_C2,SIGNAL("clicked(bool)"),self.Input_Group_C2.setDisabled)
        QObject.connect(self.Output_Radio_C2,SIGNAL("clicked(bool)"),self.Output_Group_C2.setEnabled)
        QObject.connect(self.Input_Radio_C2,SIGNAL("clicked(bool)"),self.Output_Group_C2.setDisabled)
        QObject.connect(self.Input_Radio_C2,SIGNAL("clicked(bool)"),self.Input_Group_C2.setEnabled)
        
        QObject.connect(self.Output_Radio_C3,SIGNAL("clicked(bool)"),self.Input_Group_C3.setDisabled)
        QObject.connect(self.Output_Radio_C3,SIGNAL("clicked(bool)"),self.Output_Group_C3.setEnabled)
        QObject.connect(self.Input_Radio_C3,SIGNAL("clicked(bool)"),self.Output_Group_C3.setDisabled)
        QObject.connect(self.Input_Radio_C3,SIGNAL("clicked(bool)"),self.Input_Group_C3.setEnabled)
        
        QObject.connect(self.Output_Radio_C4,SIGNAL("clicked(bool)"),self.Input_Group_C4.setDisabled)
        QObject.connect(self.Output_Radio_C4,SIGNAL("clicked(bool)"),self.Output_Group_C4.setEnabled)
        QObject.connect(self.Input_Radio_C4,SIGNAL("clicked(bool)"),self.Output_Group_C4.setDisabled)
        QObject.connect(self.Input_Radio_C4,SIGNAL("clicked(bool)"),self.Input_Group_C4.setEnabled)
        
        QObject.connect(self.Output_Radio_C5,SIGNAL("clicked(bool)"),self.Input_Group_C5.setDisabled)
        QObject.connect(self.Output_Radio_C5,SIGNAL("clicked(bool)"),self.Output_Group_C5.setEnabled)
        QObject.connect(self.Input_Radio_C5,SIGNAL("clicked(bool)"),self.Output_Group_C5.setDisabled)
        QObject.connect(self.Input_Radio_C5,SIGNAL("clicked(bool)"),self.Input_Group_C5.setEnabled)
        
        QObject.connect(self.Output_Radio_C6,SIGNAL("clicked(bool)"),self.Input_Group_C6.setDisabled)
        QObject.connect(self.Output_Radio_C6,SIGNAL("clicked(bool)"),self.Output_Group_C6.setEnabled)
        QObject.connect(self.Input_Radio_C6,SIGNAL("clicked(bool)"),self.Output_Group_C6.setDisabled)
        QObject.connect(self.Input_Radio_C6,SIGNAL("clicked(bool)"),self.Input_Group_C6.setEnabled)
        
        QObject.connect(self.Output_Radio_C7,SIGNAL("clicked(bool)"),self.Input_Group_C7.setDisabled)
        QObject.connect(self.Output_Radio_C7,SIGNAL("clicked(bool)"),self.Output_Group_C7.setEnabled)
        QObject.connect(self.Input_Radio_C7,SIGNAL("clicked(bool)"),self.Output_Group_C7.setDisabled)
        QObject.connect(self.Input_Radio_C7,SIGNAL("clicked(bool)"),self.Input_Group_C7.setEnabled)
        
        QObject.connect(self.Output_Radio_D0,SIGNAL("clicked(bool)"),self.Input_Group_D0.setDisabled)
        QObject.connect(self.Output_Radio_D0,SIGNAL("clicked(bool)"),self.Output_Group_D0.setEnabled)
        QObject.connect(self.Input_Radio_D0,SIGNAL("clicked(bool)"),self.Output_Group_D0.setDisabled)
        QObject.connect(self.Input_Radio_D0,SIGNAL("clicked(bool)"),self.Input_Group_D0.setEnabled)
        
        QObject.connect(self.Output_Radio_D1,SIGNAL("clicked(bool)"),self.Input_Group_D1.setDisabled)
        QObject.connect(self.Output_Radio_D1,SIGNAL("clicked(bool)"),self.Output_Group_D1.setEnabled)
        QObject.connect(self.Input_Radio_D1,SIGNAL("clicked(bool)"),self.Output_Group_D1.setDisabled)
        QObject.connect(self.Input_Radio_D1,SIGNAL("clicked(bool)"),self.Input_Group_D1.setEnabled)
        
        QObject.connect(self.Output_Radio_D2,SIGNAL("clicked(bool)"),self.Input_Group_D2.setDisabled)
        QObject.connect(self.Output_Radio_D2,SIGNAL("clicked(bool)"),self.Output_Group_D2.setEnabled)
        QObject.connect(self.Input_Radio_D2,SIGNAL("clicked(bool)"),self.Output_Group_D2.setDisabled)
        QObject.connect(self.Input_Radio_D2,SIGNAL("clicked(bool)"),self.Input_Group_D2.setEnabled)
        
        QObject.connect(self.Output_Radio_D3,SIGNAL("clicked(bool)"),self.Input_Group_D3.setDisabled)
        QObject.connect(self.Output_Radio_D3,SIGNAL("clicked(bool)"),self.Output_Group_D3.setEnabled)
        QObject.connect(self.Input_Radio_D3,SIGNAL("clicked(bool)"),self.Output_Group_D3.setDisabled)
        QObject.connect(self.Input_Radio_D3,SIGNAL("clicked(bool)"),self.Input_Group_D3.setEnabled)
        
        QObject.connect(self.Output_Radio_D4,SIGNAL("clicked(bool)"),self.Input_Group_D4.setDisabled)
        QObject.connect(self.Output_Radio_D4,SIGNAL("clicked(bool)"),self.Output_Group_D4.setEnabled)
        QObject.connect(self.Input_Radio_D4,SIGNAL("clicked(bool)"),self.Output_Group_D4.setDisabled)
        QObject.connect(self.Input_Radio_D4,SIGNAL("clicked(bool)"),self.Input_Group_D4.setEnabled)
        
        QObject.connect(self.Output_Radio_D5,SIGNAL("clicked(bool)"),self.Input_Group_D5.setDisabled)
        QObject.connect(self.Output_Radio_D5,SIGNAL("clicked(bool)"),self.Output_Group_D5.setEnabled)
        QObject.connect(self.Input_Radio_D5,SIGNAL("clicked(bool)"),self.Output_Group_D5.setDisabled)
        QObject.connect(self.Input_Radio_D5,SIGNAL("clicked(bool)"),self.Input_Group_D5.setEnabled)
        
        QObject.connect(self.Output_Radio_D6,SIGNAL("clicked(bool)"),self.Input_Group_D6.setDisabled)
        QObject.connect(self.Output_Radio_D6,SIGNAL("clicked(bool)"),self.Output_Group_D6.setEnabled)
        QObject.connect(self.Input_Radio_D6,SIGNAL("clicked(bool)"),self.Output_Group_D6.setDisabled)
        QObject.connect(self.Input_Radio_D6,SIGNAL("clicked(bool)"),self.Input_Group_D6.setEnabled)
        
        QObject.connect(self.Output_Radio_D7,SIGNAL("clicked(bool)"),self.Input_Group_D7.setDisabled)
        QObject.connect(self.Output_Radio_D7,SIGNAL("clicked(bool)"),self.Output_Group_D7.setEnabled)
        QObject.connect(self.Input_Radio_D7,SIGNAL("clicked(bool)"),self.Output_Group_D7.setDisabled)
        QObject.connect(self.Input_Radio_D7,SIGNAL("clicked(bool)"),self.Input_Group_D7.setEnabled)
        
        self.Generate_Button.clicked.connect(self.GenerateFunction)
        self.Save_Button.clicked.connect(self.SaveFunction)
        self.Load_Button.clicked.connect(self.LoadFunction)
        
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def GenerateFunction(self):
      Output_Path = self.lineEdit.text() + r'\AVR_CONFIG.h'
      current_date = str(datetime.date.today())
      File_Handler = open(Output_Path ,'w')
      File_Handler.write("/*******************************************/\n")
      File_Handler.write("/*              DIO configuration          */\n")
      File_Handler.write("/* Target: ATMEGA32                        */\n")
      File_Handler.write("/* Author: Peter Ghali                     */\n")
      File_Handler.write("/* Date:"+current_date+"                         */\n")
      File_Handler.write("/*******************************************/\n")
      File_Handler.write("\n")
      File_Handler.write("#ifndef _DIO_CONFIG_H\n")
      File_Handler.write("#define _DIO_CONFIG_H\n")
      File_Handler.write("\n")
      File_Handler.write("\n")
      if self.Output_Radio_A0.isChecked() :
        if self.High_Radio_A0.isChecked():
          File_Handler.write("#define   DIO_PIN_A0_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_A0_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_A0.isChecked():
          File_Handler.write("#define   DIO_PIN_A0_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_A0_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_A1.isChecked() :
        if self.High_Radio_A1.isChecked():
          File_Handler.write("#define   DIO_PIN_A1_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_A1_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_A1.isChecked():
          File_Handler.write("#define   DIO_PIN_A1_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_A1_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_A2.isChecked() :
        if self.High_Radio_A2.isChecked():
          File_Handler.write("#define   DIO_PIN_A2_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_A2_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_A2.isChecked():
          File_Handler.write("#define   DIO_PIN_A2_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_A2_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_A3.isChecked() :
        if self.High_Radio_A3.isChecked():
          File_Handler.write("#define   DIO_PIN_A3_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_A3_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_A3.isChecked():
          File_Handler.write("#define   DIO_PIN_A3_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_A3_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_A4.isChecked() :
        if self.High_Radio_A4.isChecked():
          File_Handler.write("#define   DIO_PIN_A4_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_A4_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_A4.isChecked():
          File_Handler.write("#define   DIO_PIN_A4_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_A4_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_A5.isChecked() :
        if self.High_Radio_A5.isChecked():
          File_Handler.write("#define   DIO_PIN_A5_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_A5_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_A5.isChecked():
          File_Handler.write("#define   DIO_PIN_A5_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_A5_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_A6.isChecked() :
        if self.High_Radio_A6.isChecked():
          File_Handler.write("#define   DIO_PIN_A6_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_A6_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_A6.isChecked():
          File_Handler.write("#define   DIO_PIN_A6_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_A6_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_A7.isChecked() :
        if self.High_Radio_A7.isChecked():
          File_Handler.write("#define   DIO_PIN_A7_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_A7_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_A7.isChecked():
          File_Handler.write("#define   DIO_PIN_A7_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_A7_MODE  DIO_INPUT_HIGH_IMP\n")
      File_Handler.write("\n")
       
      if self.Output_Radio_B0.isChecked() :
        if self.High_Radio_B0.isChecked():
          File_Handler.write("#define   DIO_PIN_B0_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_B0_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_B0.isChecked():
          File_Handler.write("#define   DIO_PIN_B0_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_B0_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_B1.isChecked() :
        if self.High_Radio_B1.isChecked():
          File_Handler.write("#define   DIO_PIN_B1_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_B1_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_B1.isChecked():
          File_Handler.write("#define   DIO_PIN_B1_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_B1_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_B2.isChecked() :
        if self.High_Radio_B2.isChecked():
          File_Handler.write("#define   DIO_PIN_B2_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_B2_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_B2.isChecked():
          File_Handler.write("#define   DIO_PIN_B2_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_B2_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_B3.isChecked() :
        if self.High_Radio_B3.isChecked():
          File_Handler.write("#define   DIO_PIN_B3_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_B3_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_B3.isChecked():
          File_Handler.write("#define   DIO_PIN_B3_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_B3_MODE  DIO_INPUT_HIGH_IMP\n")
          
          
      if self.Output_Radio_B4.isChecked() :
        if self.High_Radio_B4.isChecked():
          File_Handler.write("#define   DIO_PIN_B4_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_B4_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_B4.isChecked():
          File_Handler.write("#define   DIO_PIN_B4_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_B4_MODE  DIO_INPUT_HIGH_IMP\n")
      
      if self.Output_Radio_B5.isChecked() :
        if self.High_Radio_B5.isChecked():
          File_Handler.write("#define   DIO_PIN_B5_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_B5_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_B5.isChecked():
          File_Handler.write("#define   DIO_PIN_B5_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_B5_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_B6.isChecked() :
        if self.High_Radio_B6.isChecked():
          File_Handler.write("#define   DIO_PIN_B6_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_B6_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_B6.isChecked():
          File_Handler.write("#define   DIO_PIN_B6_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_B6_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_B7.isChecked() :
        if self.High_Radio_B7.isChecked():
          File_Handler.write("#define   DIO_PIN_B7_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_B7_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_B7.isChecked():
          File_Handler.write("#define   DIO_PIN_B7_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_B7_MODE  DIO_INPUT_HIGH_IMP\n")
      File_Handler.write("\n")    
      if self.Output_Radio_C0.isChecked() :
        if self.High_Radio_C0.isChecked():
          File_Handler.write("#define   DIO_PIN_C0_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_C0_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_C0.isChecked():
          File_Handler.write("#define   DIO_PIN_C0_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_C0_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_C1.isChecked() :
        if self.High_Radio_C1.isChecked():
          File_Handler.write("#define   DIO_PIN_C1_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_C1_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_C1.isChecked():
          File_Handler.write("#define   DIO_PIN_C1_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_C1_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_C2.isChecked() :
        if self.High_Radio_C2.isChecked():
          File_Handler.write("#define   DIO_PIN_C2_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_C2_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_C2.isChecked():
          File_Handler.write("#define   DIO_PIN_C2_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_C2_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_C3.isChecked() :
        if self.High_Radio_C3.isChecked():
          File_Handler.write("#define   DIO_PIN_C3_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_C3_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_C3.isChecked():
          File_Handler.write("#define   DIO_PIN_C3_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_C3_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_C4.isChecked() :
        if self.High_Radio_C4.isChecked():
          File_Handler.write("#define   DIO_PIN_C4_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_C4_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_C4.isChecked():
          File_Handler.write("#define   DIO_PIN_C4_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_C4_MODE  DIO_INPUT_HIGH_IMP\n")
      if self.Output_Radio_C5.isChecked() :
        if self.High_Radio_C5.isChecked():
          File_Handler.write("#define   DIO_PIN_C5_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_C5_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_C5.isChecked():
          File_Handler.write("#define   DIO_PIN_C5_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_C5_MODE  DIO_INPUT_HIGH_IMP\n")
      if self.Output_Radio_C6.isChecked() :
        if self.High_Radio_C6.isChecked():
          File_Handler.write("#define   DIO_PIN_C6_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_C6_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_C6.isChecked():
          File_Handler.write("#define   DIO_PIN_C6_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_C6_MODE  DIO_INPUT_HIGH_IMP\n")
      if self.Output_Radio_C7.isChecked() :
        if self.High_Radio_C7.isChecked():
          File_Handler.write("#define   DIO_PIN_C7_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_C7_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_C7.isChecked():
          File_Handler.write("#define   DIO_PIN_C7_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_C7_MODE  DIO_INPUT_HIGH_IMP\n")
      File_Handler.write("\n")
      
      if self.Output_Radio_D0.isChecked() :
        if self.High_Radio_D0.isChecked():
          File_Handler.write("#define   DIO_PIN_D0_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_D0_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_D0.isChecked():
          File_Handler.write("#define   DIO_PIN_D0_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_D0_MODE  DIO_INPUT_HIGH_IMP\n")
      if self.Output_Radio_D1.isChecked() :
        if self.High_Radio_D1.isChecked():
          File_Handler.write("#define   DIO_PIN_D1_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_D1_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_D1.isChecked():
          File_Handler.write("#define   DIO_PIN_D1_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_D1_MODE  DIO_INPUT_HIGH_IMP\n")
      if self.Output_Radio_D2.isChecked() :
        if self.High_Radio_D2.isChecked():
          File_Handler.write("#define   DIO_PIN_D2_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_D2_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_D2.isChecked():
          File_Handler.write("#define   DIO_PIN_D2_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_D2_MODE  DIO_INPUT_HIGH_IMP\n")
      if self.Output_Radio_D3.isChecked() :
        if self.High_Radio_D3.isChecked():
          File_Handler.write("#define   DIO_PIN_D3_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_D3_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_D3.isChecked():
          File_Handler.write("#define   DIO_PIN_D3_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_D3_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_D4.isChecked() :
        if self.High_Radio_D4.isChecked():
          File_Handler.write("#define   DIO_PIN_D4_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_D4_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_D4.isChecked():
          File_Handler.write("#define   DIO_PIN_D4_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_D4_MODE  DIO_INPUT_HIGH_IMP\n")
          
      if self.Output_Radio_D5.isChecked() :
        if self.High_Radio_D5.isChecked():
          File_Handler.write("#define   DIO_PIN_D5_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_D5_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_D5.isChecked():
          File_Handler.write("#define   DIO_PIN_D5_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_D5_MODE  DIO_INPUT_HIGH_IMP\n")
      
      if self.Output_Radio_D6.isChecked() :
        if self.High_Radio_D6.isChecked():
          File_Handler.write("#define   DIO_PIN_D6_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_D6_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_D6.isChecked():
          File_Handler.write("#define   DIO_PIN_D6_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_D6_MODE  DIO_INPUT_HIGH_IMP\n")
         
      if self.Output_Radio_D7.isChecked() :
        if self.High_Radio_D7.isChecked():
          File_Handler.write("#define   DIO_PIN_D7_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_D7_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.Pull_Up_Radio_D7.isChecked():
          File_Handler.write("#define   DIO_PIN_D7_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_D7_MODE  DIO_INPUT_HIGH_IMP\n")
          
      File_Handler.write("\n")   
      File_Handler.write("#endif /*_AVR_CONFIG_H*/\n")
      
    def SaveFunction(self):
      
        DIO = ET.Element("DIO")
      
        PORTA = ET.Element("PORTA")
        PORTA_PIN0 = ET.Element("PIN0")
        PORTA_PIN1 = ET.Element("PIN1")
        PORTA_PIN2 = ET.Element("PIN2")
        PORTA_PIN3 = ET.Element("PIN3")
        PORTA_PIN4 = ET.Element("PIN4")
        PORTA_PIN5 = ET.Element("PIN5")
        PORTA_PIN6 = ET.Element("PIN6")
        PORTA_PIN7 = ET.Element("PIN7")
        
        PORTA_PIN0_DIR = ET.Element("DIR")
        PORTA_PIN0_CONFIG = ET.Element("CONFIG")
        PORTA_PIN1_DIR = ET.Element("DIR")
        PORTA_PIN1_CONFIG = ET.Element("CONFIG")
        PORTA_PIN2_DIR = ET.Element("DIR")
        PORTA_PIN2_CONFIG = ET.Element("CONFIG")
        PORTA_PIN3_DIR = ET.Element("DIR")
        PORTA_PIN3_CONFIG = ET.Element("CONFIG")
        PORTA_PIN4_DIR = ET.Element("DIR")
        PORTA_PIN4_CONFIG = ET.Element("CONFIG")
        PORTA_PIN5_DIR = ET.Element("DIR")
        PORTA_PIN5_CONFIG = ET.Element("CONFIG")
        PORTA_PIN6_DIR = ET.Element("DIR")
        PORTA_PIN6_CONFIG = ET.Element("CONFIG")
        PORTA_PIN7_DIR = ET.Element("DIR")
        PORTA_PIN7_CONFIG = ET.Element("CONFIG")
        
        if self.Input_Radio_A0.isChecked():
              PORTA_PIN0_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_A0.isChecked():
                  PORTA_PIN0_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_A0.isChecked():
                  PORTA_PIN0_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_A0.isChecked():
              PORTA_PIN0_DIR.text = 'OUTPUT'
              if self.High_Radio_A0.isChecked():
                  PORTA_PIN0_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_A0.isChecked():
                  PORTA_PIN0_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_A1.isChecked():
              PORTA_PIN0_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_A1.isChecked():
                  PORTA_PIN1_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_A1.isChecked():
                  PORTA_PIN1_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_A1.isChecked():
              PORTA_PIN1_DIR.text = 'OUTPUT'
              if self.High_Radio_A1.isChecked():
                  PORTA_PIN1_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_A1.isChecked():
                  PORTA_PIN1_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_A2.isChecked():
              PORTA_PIN2_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_A2.isChecked():
                  PORTA_PIN2_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_A2.isChecked():
                  PORTA_PIN2_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_A2.isChecked():
              PORTA_PIN2_DIR.text = 'OUTPUT'
              if self.High_Radio_A2.isChecked():
                  PORTA_PIN2_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_A2.isChecked():
                  PORTA_PIN2_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_A3.isChecked():
              PORTA_PIN3_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_A3.isChecked():
                  PORTA_PIN3_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_A3.isChecked():
                  PORTA_PIN3_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_A3.isChecked():
              PORTA_PIN3_DIR.text = 'OUTPUT'
              if self.High_Radio_A3.isChecked():
                  PORTA_PIN3_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_A3.isChecked():
                  PORTA_PIN3_CONFIG.text = 'OutputLow'
  
        if self.Input_Radio_A4.isChecked():
              PORTA_PIN4_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_A4.isChecked():
                  PORTA_PIN4_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_A4.isChecked():
                  PORTA_PIN4_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_A4.isChecked():
              PORTA_PIN4_DIR.text = 'OUTPUT'
              if self.High_Radio_A4.isChecked():
                  PORTA_PIN4_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_A4.isChecked():
                  PORTA_PIN4_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_A5.isChecked():
              PORTA_PIN5_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_A5.isChecked():
                  PORTA_PIN5_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_A5.isChecked():
                  PORTA_PIN5_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_A5.isChecked():
              PORTA_PIN5_DIR.text = 'OUTPUT'
              if self.High_Radio_A5.isChecked():
                  PORTA_PIN5_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_A5.isChecked():
                  PORTA_PIN5_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_A6.isChecked():
              PORTA_PIN6_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_A6.isChecked():
                  PORTA_PIN6_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_A6.isChecked():
                  PORTA_PIN6_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_A6.isChecked():
              PORTA_PIN6_DIR.text = 'OUTPUT'
              if self.High_Radio_A6.isChecked():
                  PORTA_PIN6_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_A6.isChecked():
                  PORTA_PIN6_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_A7.isChecked():
              PORTA_PIN7_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_A7.isChecked():
                  PORTA_PIN7_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_A7.isChecked():
                  PORTA_PIN7_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_A7.isChecked():
              PORTA_PIN7_DIR.text = 'OUTPUT'
              if self.High_Radio_A7.isChecked():
                  PORTA_PIN7_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_A7.isChecked():
                  PORTA_PIN7_CONFIG.text = 'OutputLow'
          
        DIO.append(PORTA)
          
        PORTA.append(PORTA_PIN0)
        PORTA_PIN0.append(PORTA_PIN0_DIR)
        PORTA_PIN0.append(PORTA_PIN0_CONFIG)
        PORTA.append(PORTA_PIN1)
        PORTA_PIN1.append(PORTA_PIN1_DIR)
        PORTA_PIN1.append(PORTA_PIN1_CONFIG)
        PORTA.append(PORTA_PIN2)
        PORTA_PIN2.append(PORTA_PIN2_DIR)
        PORTA_PIN2.append(PORTA_PIN2_CONFIG)
        PORTA.append(PORTA_PIN3)
        PORTA_PIN3.append(PORTA_PIN3_DIR)
        PORTA_PIN3.append(PORTA_PIN3_CONFIG)
        PORTA.append(PORTA_PIN4)
        PORTA_PIN4.append(PORTA_PIN4_DIR)
        PORTA_PIN4.append(PORTA_PIN4_CONFIG)
        PORTA.append(PORTA_PIN5)
        PORTA_PIN5.append(PORTA_PIN5_DIR)
        PORTA_PIN5.append(PORTA_PIN5_CONFIG)
        PORTA.append(PORTA_PIN6)
        PORTA_PIN6.append(PORTA_PIN6_DIR)
        PORTA_PIN6.append(PORTA_PIN6_CONFIG)
        PORTA.append(PORTA_PIN7)
        PORTA_PIN7.append(PORTA_PIN7_DIR)
        PORTA_PIN7.append(PORTA_PIN7_CONFIG)
        
 #********************************************************************       
        
        PORTB = ET.Element("PORTB")
        PORTB_PIN0 = ET.Element("PIN0")
        PORTB_PIN1 = ET.Element("PIN1")
        PORTB_PIN2 = ET.Element("PIN2")
        PORTB_PIN3 = ET.Element("PIN3")
        PORTB_PIN4 = ET.Element("PIN4")
        PORTB_PIN5 = ET.Element("PIN5")
        PORTB_PIN6 = ET.Element("PIN6")
        PORTB_PIN7 = ET.Element("PIN7")
        
        PORTB_PIN0_DIR = ET.Element("DIR")
        PORTB_PIN0_CONFIG = ET.Element("CONFIG")
        PORTB_PIN1_DIR = ET.Element("DIR")
        PORTB_PIN1_CONFIG = ET.Element("CONFIG")
        PORTB_PIN2_DIR = ET.Element("DIR")
        PORTB_PIN2_CONFIG = ET.Element("CONFIG")
        PORTB_PIN3_DIR = ET.Element("DIR")
        PORTB_PIN3_CONFIG = ET.Element("CONFIG")
        PORTB_PIN4_DIR = ET.Element("DIR")
        PORTB_PIN4_CONFIG = ET.Element("CONFIG")
        PORTB_PIN5_DIR = ET.Element("DIR")
        PORTB_PIN5_CONFIG = ET.Element("CONFIG")
        PORTB_PIN6_DIR = ET.Element("DIR")
        PORTB_PIN6_CONFIG = ET.Element("CONFIG")
        PORTB_PIN7_DIR = ET.Element("DIR")
        PORTB_PIN7_CONFIG = ET.Element("CONFIG")
        
        if self.Input_Radio_B0.isChecked():
              PORTB_PIN0_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_B0.isChecked():
                  PORTB_PIN0_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_B0.isChecked():
                  PORTB_PIN0_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_B0.isChecked():
              PORTB_PIN0_DIR.text = 'OUTPUT'
              if self.High_Radio_B0.isChecked():
                  PORTB_PIN0_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_B0.isChecked():
                  PORTB_PIN0_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_B1.isChecked():
              PORTB_PIN1_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_B1.isChecked():
                  PORTB_PIN1_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_B1.isChecked():
                  PORTB_PIN1_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_B1.isChecked():
              PORTB_PIN1_DIR.text = 'OUTPUT'
              if self.High_Radio_B1.isChecked():
                  PORTB_PIN1_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_B1.isChecked():
                  PORTB_PIN1_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_B2.isChecked():
              PORTB_PIN2_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_B2.isChecked():
                  PORTB_PIN2_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_B2.isChecked():
                  PORTB_PIN2_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_B2.isChecked():
              PORTB_PIN2_DIR.text = 'OUTPUT'
              if self.High_Radio_B2.isChecked():
                  PORTB_PIN2_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_B2.isChecked():
                  PORTB_PIN2_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_B3.isChecked():
              PORTB_PIN3_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_B3.isChecked():
                  PORTB_PIN3_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_B3.isChecked():
                  PORTB_PIN3_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_B3.isChecked():
              PORTB_PIN3_DIR.text = 'OUTPUT'
              if self.High_Radio_B3.isChecked():
                  PORTB_PIN3_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_B3.isChecked():
                  PORTB_PIN3_CONFIG.text = 'OutputLow'
  
        if self.Input_Radio_B4.isChecked():
              PORTB_PIN4_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_B4.isChecked():
                  PORTB_PIN4_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_B4.isChecked():
                  PORTB_PIN4_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_B4.isChecked():
              PORTB_PIN4_DIR.text = 'OUTPUT'
              if self.High_Radio_B4.isChecked():
                  PORTB_PIN4_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_B4.isChecked():
                  PORTB_PIN4_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_B5.isChecked():
              PORTB_PIN5_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_B5.isChecked():
                  PORTB_PIN5_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_B5.isChecked():
                  PORTB_PIN5_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_B5.isChecked():
              PORTB_PIN5_DIR.text = 'OUTPUT'
              if self.High_Radio_B5.isChecked():
                  PORTB_PIN5_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_B5.isChecked():
                  PORTB_PIN5_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_B6.isChecked():
              PORTB_PIN6_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_B6.isChecked():
                  PORTB_PIN6_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_B6.isChecked():
                  PORTB_PIN6_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_B6.isChecked():
              PORTB_PIN6_DIR.text = 'OUTPUT'
              if self.High_Radio_B6.isChecked():
                  PORTB_PIN6_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_B6.isChecked():
                  PORTB_PIN6_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_B7.isChecked():
              PORTB_PIN7_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_B7.isChecked():
                  PORTB_PIN7_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_B7.isChecked():
                  PORTB_PIN7_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_B7.isChecked():
              PORTB_PIN7_DIR.text = 'OUTPUT'
              if self.High_Radio_B7.isChecked():
                  PORTB_PIN7_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_B7.isChecked():
                  PORTB_PIN7_CONFIG.text = 'OutputLow'
                  
                  
                  
                  
        DIO.append(PORTB)
          
        PORTB.append(PORTB_PIN0)
        PORTB_PIN0.append(PORTB_PIN0_DIR)
        PORTB_PIN0.append(PORTB_PIN0_CONFIG)
        PORTB.append(PORTB_PIN1)
        PORTB_PIN1.append(PORTB_PIN1_DIR)
        PORTB_PIN1.append(PORTB_PIN1_CONFIG)
        PORTB.append(PORTB_PIN2)
        PORTB_PIN2.append(PORTB_PIN2_DIR)
        PORTB_PIN2.append(PORTB_PIN2_CONFIG)
        PORTB.append(PORTB_PIN3)
        PORTB_PIN3.append(PORTB_PIN3_DIR)
        PORTB_PIN3.append(PORTB_PIN3_CONFIG)
        PORTB.append(PORTB_PIN4)
        PORTB_PIN4.append(PORTB_PIN4_DIR)
        PORTB_PIN4.append(PORTB_PIN4_CONFIG)
        PORTB.append(PORTB_PIN5)
        PORTB_PIN5.append(PORTB_PIN5_DIR)
        PORTB_PIN5.append(PORTB_PIN5_CONFIG)
        PORTB.append(PORTB_PIN6)
        PORTB_PIN6.append(PORTB_PIN6_DIR)
        PORTB_PIN6.append(PORTB_PIN6_CONFIG)
        PORTB.append(PORTB_PIN7)
        PORTB_PIN7.append(PORTB_PIN7_DIR)
        PORTB_PIN7.append(PORTB_PIN7_CONFIG)
        
#****************************************************************        

        PORTC = ET.Element("PORTC")
        PORTC_PIN0 = ET.Element("PIN0")
        PORTC_PIN1 = ET.Element("PIN1")
        PORTC_PIN2 = ET.Element("PIN2")
        PORTC_PIN3 = ET.Element("PIN3")
        PORTC_PIN4 = ET.Element("PIN4")
        PORTC_PIN5 = ET.Element("PIN5")
        PORTC_PIN6 = ET.Element("PIN6")
        PORTC_PIN7 = ET.Element("PIN7")
        
        PORTC_PIN0_DIR = ET.Element("DIR")
        PORTC_PIN0_CONFIG = ET.Element("CONFIG")
        PORTC_PIN1_DIR = ET.Element("DIR")
        PORTC_PIN1_CONFIG = ET.Element("CONFIG")
        PORTC_PIN2_DIR = ET.Element("DIR")
        PORTC_PIN2_CONFIG = ET.Element("CONFIG")
        PORTC_PIN3_DIR = ET.Element("DIR")
        PORTC_PIN3_CONFIG = ET.Element("CONFIG")
        PORTC_PIN4_DIR = ET.Element("DIR")
        PORTC_PIN4_CONFIG = ET.Element("CONFIG")
        PORTC_PIN5_DIR = ET.Element("DIR")
        PORTC_PIN5_CONFIG = ET.Element("CONFIG")
        PORTC_PIN6_DIR = ET.Element("DIR")
        PORTC_PIN6_CONFIG = ET.Element("CONFIG")
        PORTC_PIN7_DIR = ET.Element("DIR")
        PORTC_PIN7_CONFIG = ET.Element("CONFIG")
        
        if self.Input_Radio_C0.isChecked():
              PORTC_PIN0_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_C0.isChecked():
                  PORTC_PIN0_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_C0.isChecked():
                  PORTC_PIN0_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_C0.isChecked():
              PORTC_PIN0_DIR.text = 'OUTPUT'
              if self.High_Radio_C0.isChecked():
                  PORTC_PIN0_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_C0.isChecked():
                  PORTC_PIN0_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_C1.isChecked():
              PORTC_PIN1_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_C1.isChecked():
                  PORTC_PIN1_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_C1.isChecked():
                  PORTC_PIN1_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_C1.isChecked():
              PORTC_PIN1_DIR.text = 'OUTPUT'
              if self.High_Radio_C1.isChecked():
                  PORTC_PIN1_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_C1.isChecked():
                  PORTC_PIN1_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_C2.isChecked():
              PORTC_PIN2_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_C2.isChecked():
                  PORTC_PIN2_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_C2.isChecked():
                  PORTC_PIN2_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_C2.isChecked():
              PORTC_PIN2_DIR.text = 'OUTPUT'
              if self.High_Radio_C2.isChecked():
                  PORTC_PIN2_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_C2.isChecked():
                  PORTC_PIN2_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_C3.isChecked():
              PORTC_PIN3_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_C3.isChecked():
                  PORTC_PIN3_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_C3.isChecked():
                  PORTC_PIN3_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_C3.isChecked():
              PORTC_PIN3_DIR.text = 'OUTPUT'
              if self.High_Radio_C3.isChecked():
                  PORTC_PIN3_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_C3.isChecked():
                  PORTC_PIN3_CONFIG.text = 'OutputLow'
  
        if self.Input_Radio_C4.isChecked():
              PORTC_PIN4_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_C4.isChecked():
                  PORTC_PIN4_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_C4.isChecked():
                  PORTC_PIN4_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_C4.isChecked():
              PORTC_PIN4_DIR.text = 'OUTPUT'
              if self.High_Radio_C4.isChecked():
                  PORTC_PIN4_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_C4.isChecked():
                  PORTC_PIN4_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_C5.isChecked():
              PORTC_PIN5_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_C5.isChecked():
                  PORTC_PIN5_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_C5.isChecked():
                  PORTC_PIN5_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_C5.isChecked():
              PORTC_PIN5_DIR.text = 'OUTPUT'
              if self.High_Radio_C5.isChecked():
                  PORTC_PIN5_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_C5.isChecked():
                  PORTC_PIN5_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_C6.isChecked():
              PORTC_PIN6_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_C6.isChecked():
                  PORTC_PIN6_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_C6.isChecked():
                  PORTC_PIN6_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_C6.isChecked():
              PORTC_PIN6_DIR.text = 'OUTPUT'
              if self.High_Radio_C6.isChecked():
                  PORTC_PIN6_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_C6.isChecked():
                  PORTC_PIN6_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_C7.isChecked():
              PORTC_PIN7_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_C7.isChecked():
                  PORTC_PIN7_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_C7.isChecked():
                  PORTC_PIN7_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_C7.isChecked():
              PORTC_PIN7_DIR.text = 'OUTPUT'
              if self.High_Radio_C7.isChecked():
                  PORTC_PIN7_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_C7.isChecked():
                  PORTC_PIN7_CONFIG.text = 'OutputLow'
                  
                  
                  
                  
        DIO.append(PORTC)
          
        PORTC.append(PORTC_PIN0)
        PORTC_PIN0.append(PORTC_PIN0_DIR)
        PORTC_PIN0.append(PORTC_PIN0_CONFIG)
        PORTC.append(PORTC_PIN1)
        PORTC_PIN1.append(PORTC_PIN1_DIR)
        PORTC_PIN1.append(PORTC_PIN1_CONFIG)
        PORTC.append(PORTC_PIN2)
        PORTC_PIN2.append(PORTC_PIN2_DIR)
        PORTC_PIN2.append(PORTC_PIN2_CONFIG)
        PORTC.append(PORTC_PIN3)
        PORTC_PIN3.append(PORTC_PIN3_DIR)
        PORTC_PIN3.append(PORTC_PIN3_CONFIG)
        PORTC.append(PORTC_PIN4)
        PORTC_PIN4.append(PORTC_PIN4_DIR)
        PORTC_PIN4.append(PORTC_PIN4_CONFIG)
        PORTC.append(PORTC_PIN5)
        PORTC_PIN5.append(PORTC_PIN5_DIR)
        PORTC_PIN5.append(PORTC_PIN5_CONFIG)
        PORTC.append(PORTC_PIN6)
        PORTC_PIN6.append(PORTC_PIN6_DIR)
        PORTC_PIN6.append(PORTC_PIN6_CONFIG)
        PORTC.append(PORTC_PIN7)
        PORTC_PIN7.append(PORTC_PIN7_DIR)
        PORTC_PIN7.append(PORTC_PIN7_CONFIG)

#***************************************************************************

        PORTD = ET.Element("PORTD")
        PORTD_PIN0 = ET.Element("PIN0")
        PORTD_PIN1 = ET.Element("PIN1")
        PORTD_PIN2 = ET.Element("PIN2")
        PORTD_PIN3 = ET.Element("PIN3")
        PORTD_PIN4 = ET.Element("PIN4")
        PORTD_PIN5 = ET.Element("PIN5")
        PORTD_PIN6 = ET.Element("PIN6")
        PORTD_PIN7 = ET.Element("PIN7")
        
        PORTD_PIN0_DIR = ET.Element("DIR")
        PORTD_PIN0_CONFIG = ET.Element("CONFIG")
        PORTD_PIN1_DIR = ET.Element("DIR")
        PORTD_PIN1_CONFIG = ET.Element("CONFIG")
        PORTD_PIN2_DIR = ET.Element("DIR")
        PORTD_PIN2_CONFIG = ET.Element("CONFIG")
        PORTD_PIN3_DIR = ET.Element("DIR")
        PORTD_PIN3_CONFIG = ET.Element("CONFIG")
        PORTD_PIN4_DIR = ET.Element("DIR")
        PORTD_PIN4_CONFIG = ET.Element("CONFIG")
        PORTD_PIN5_DIR = ET.Element("DIR")
        PORTD_PIN5_CONFIG = ET.Element("CONFIG")
        PORTD_PIN6_DIR = ET.Element("DIR")
        PORTD_PIN6_CONFIG = ET.Element("CONFIG")
        PORTD_PIN7_DIR = ET.Element("DIR")
        PORTD_PIN7_CONFIG = ET.Element("CONFIG")
        
        if self.Input_Radio_D0.isChecked():
              PORTD_PIN0_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_D0.isChecked():
                  PORTD_PIN0_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_D0.isChecked():
                  PORTD_PIN0_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_D0.isChecked():
              PORTD_PIN0_DIR.text = 'OUTPUT'
              if self.High_Radio_D0.isChecked():
                  PORTD_PIN0_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_D0.isChecked():
                  PORTD_PIN0_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_D1.isChecked():
              PORTD_PIN1_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_D1.isChecked():
                  PORTD_PIN1_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_D1.isChecked():
                  PORTD_PIN1_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_D1.isChecked():
              PORTD_PIN1_DIR.text = 'OUTPUT'
              if self.High_Radio_D1.isChecked():
                  PORTD_PIN1_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_D1.isChecked():
                  PORTD_PIN1_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_D2.isChecked():
              PORTD_PIN2_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_D2.isChecked():
                  PORTD_PIN2_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_D2.isChecked():
                  PORTD_PIN2_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_D2.isChecked():
              PORTD_PIN2_DIR.text = 'OUTPUT'
              if self.High_Radio_D2.isChecked():
                  PORTD_PIN2_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_D2.isChecked():
                  PORTD_PIN2_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_D3.isChecked():
              PORTD_PIN3_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_D3.isChecked():
                  PORTD_PIN3_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_D3.isChecked():
                  PORTD_PIN3_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_D3.isChecked():
              PORTD_PIN3_DIR.text = 'OUTPUT'
              if self.High_Radio_D3.isChecked():
                  PORTD_PIN3_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_D3.isChecked():
                  PORTD_PIN3_CONFIG.text = 'OutputLow'
  
        if self.Input_Radio_D4.isChecked():
              PORTD_PIN4_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_D4.isChecked():
                  PORTD_PIN4_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_D4.isChecked():
                  PORTD_PIN4_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_D4.isChecked():
              PORTD_PIN4_DIR.text = 'OUTPUT'
              if self.High_Radio_D4.isChecked():
                  PORTD_PIN4_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_D4.isChecked():
                  PORTD_PIN4_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_D5.isChecked():
              PORTD_PIN5_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_D5.isChecked():
                  PORTD_PIN5_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_D5.isChecked():
                  PORTD_PIN5_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_D5.isChecked():
              PORTD_PIN5_DIR.text = 'OUTPUT'
              if self.High_Radio_D5.isChecked():
                  PORTD_PIN5_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_D5.isChecked():
                  PORTD_PIN5_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_D6.isChecked():
              PORTD_PIN6_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_D6.isChecked():
                  PORTD_PIN6_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_D6.isChecked():
                  PORTD_PIN6_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_D6.isChecked():
              PORTD_PIN6_DIR.text = 'OUTPUT'
              if self.High_Radio_D6.isChecked():
                  PORTD_PIN6_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_D6.isChecked():
                  PORTD_PIN6_CONFIG.text = 'OutputLow'
                  
        if self.Input_Radio_D7.isChecked():
              PORTD_PIN7_DIR.text = 'INPUT'
              if self.Pull_Up_Radio_D7.isChecked():
                  PORTD_PIN7_CONFIG.text = 'PullUP'
              elif self.High_Imp_Radio_D7.isChecked():
                  PORTD_PIN7_CONFIG.text = 'InputHigh'
        elif self.Output_Radio_D7.isChecked():
              PORTD_PIN7_DIR.text = 'OUTPUT'
              if self.High_Radio_D7.isChecked():
                  PORTD_PIN7_CONFIG.text = 'OutputHigh'
              elif self.Low_Radio_D7.isChecked():
                  PORTD_PIN7_CONFIG.text = 'OutputLow'
                  
                  
                  
                  
        DIO.append(PORTD)
          
        PORTD.append(PORTD_PIN0)
        PORTD_PIN0.append(PORTD_PIN0_DIR)
        PORTD_PIN0.append(PORTD_PIN0_CONFIG)
        PORTD.append(PORTD_PIN1)
        PORTD_PIN1.append(PORTD_PIN1_DIR)
        PORTD_PIN1.append(PORTD_PIN1_CONFIG)
        PORTD.append(PORTD_PIN2)
        PORTD_PIN2.append(PORTD_PIN2_DIR)
        PORTD_PIN2.append(PORTD_PIN2_CONFIG)
        PORTD.append(PORTD_PIN3)
        PORTD_PIN3.append(PORTD_PIN3_DIR)
        PORTD_PIN3.append(PORTD_PIN3_CONFIG)
        PORTD.append(PORTD_PIN4)
        PORTD_PIN4.append(PORTD_PIN4_DIR)
        PORTD_PIN4.append(PORTD_PIN4_CONFIG)
        PORTD.append(PORTD_PIN5)
        PORTD_PIN5.append(PORTD_PIN5_DIR)
        PORTD_PIN5.append(PORTD_PIN5_CONFIG)
        PORTD.append(PORTD_PIN6)
        PORTD_PIN6.append(PORTD_PIN6_DIR)
        PORTD_PIN6.append(PORTD_PIN6_CONFIG)
        PORTD.append(PORTD_PIN7)
        PORTD_PIN7.append(PORTD_PIN7_DIR)
        PORTD_PIN7.append(PORTD_PIN7_CONFIG)
                        
        path = self.lineEdit_2.text()+r'\DIO_Cfg.xml'
        f=open(path,'w')
        f.write(ET.tostring(DIO, pretty_print=True).decode())
        f.close()
        
    def LoadFunction(self):
        path = self.lineEdit_3.text()+r'\DIO_Cfg.xml'
        
        tree = ET.parse(path)
        DIO=tree.getroot()
        
        PORT=DIO.find('PORTA')
        
        PIN0=PORT.find('PIN0')
        DIR = PIN0.find('DIR').text
        CONF = PIN0.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_A0.setChecked(True)
            self.Output_Group_A0.setDisabled(True)
            self.Input_Group_A0.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_A0.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_A0.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_A0.setChecked(True)
            self.Input_Group_A0.setDisabled(True)
            self.Output_Group_A0.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_A0.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_A0.setChecked(True)
                
        PIN1=PORT.find('PIN1')
        DIR = PIN1.find('DIR').text
        CONF = PIN1.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_A1.setChecked(True)
            self.Output_Group_A1.setDisabled(True)
            self.Input_Group_A1.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_A1.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_A1.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_A1.setChecked(True)
            self.Input_Group_A1.setDisabled(True)
            self.Output_Group_A1.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_A1.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_A1.setChecked(True)
                                
        PIN2=PORT.find('PIN2')
        DIR = PIN2.find('DIR').text
        CONF = PIN2.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_A2.setChecked(True)
            self.Output_Group_A2.setDisabled(True)
            self.Input_Group_A2.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_A2.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_A2.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_A2.setChecked(True)
            self.Input_Group_A2.setDisabled(True)
            self.Output_Group_A2.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_A2.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_A2.setChecked(True)
                
                                
        PIN3=PORT.find('PIN3')
        DIR = PIN3.find('DIR').text
        CONF = PIN3.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_A3.setChecked(True)
            self.Output_Group_A3.setDisabled(True)
            self.Input_Group_A3.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_A3.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_A3.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_A3.setChecked(True)
            self.Input_Group_A3.setDisabled(True)
            self.Output_Group_A3.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_A3.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_A3.setChecked(True)
                
                                
        PIN4=PORT.find('PIN4')
        DIR = PIN4.find('DIR').text
        CONF = PIN4.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_A4.setChecked(True)
            self.Output_Group_A4.setDisabled(True)
            self.Input_Group_A4.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_A4.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_A4.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_A4.setChecked(True)
            self.Input_Group_A4.setDisabled(True)
            self.Output_Group_A4.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_A4.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_A4.setChecked(True)
                
                                
        PIN5=PORT.find('PIN5')
        DIR = PIN5.find('DIR').text
        CONF = PIN5.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_A5.setChecked(True)
            self.Output_Group_A5.setDisabled(True)
            self.Input_Group_A5.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_A5.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_A5.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_A5.setChecked(True)
            self.Input_Group_A5.setDisabled(True)
            self.Output_Group_A5.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_A5.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_A5.setChecked(True)
                
                                
        PIN6=PORT.find('PIN6')
        DIR = PIN6.find('DIR').text
        CONF = PIN6.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_A6.setChecked(True)
            self.Output_Group_A6.setDisabled(True)
            self.Input_Group_A6.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_A6.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_A6.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_A6.setChecked(True)
            self.Input_Group_A6.setDisabled(True)
            self.Output_Group_A6.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_A6.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_A6.setChecked(True)
                
        PIN7=PORT.find('PIN7')
        DIR = PIN6.find('DIR').text
        CONF = PIN6.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_A7.setChecked(True)
            self.Output_Group_A7.setDisabled(True)
            self.Input_Group_A7.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_A7.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_A7.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_A7.setChecked(True)
            self.Input_Group_A7.setDisabled(True)
            self.Output_Group_A7.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_A7.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_A7.setChecked(True)
                        
 
 #*****************************************
        PORT=DIO.find('PORTB')
        PIN0=PORT.find('PIN0')
        DIR = PIN0.find('DIR').text
        CONF = PIN0.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_B0.setChecked(True)
            self.Output_Group_B0.setDisabled(True)
            self.Input_Group_B0.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_B0.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_B0.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_B0.setChecked(True)
            self.Input_Group_B0.setDisabled(True)
            self.Output_Group_B0.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_B0.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_B0.setChecked(True)
                
        PIN1=PORT.find('PIN1')
        DIR = PIN1.find('DIR').text
        CONF = PIN1.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_B1.setChecked(True)
            self.Output_Group_B1.setDisabled(True)
            self.Input_Group_B1.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_B1.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_B1.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_B1.setChecked(True)
            self.Input_Group_B1.setDisabled(True)
            self.Output_Group_B1.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_B1.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_B1.setChecked(True)
                                
        PIN2=PORT.find('PIN2')
        DIR = PIN2.find('DIR').text
        CONF = PIN2.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_B2.setChecked(True)
            self.Output_Group_B2.setDisabled(True)
            self.Input_Group_B2.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_B2.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_B2.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_B2.setChecked(True)
            self.Input_Group_B2.setDisabled(True)
            self.Output_Group_B2.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_B2.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_B2.setChecked(True)
                
                                
        PIN3=PORT.find('PIN3')
        DIR = PIN3.find('DIR').text
        CONF = PIN3.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_B3.setChecked(True)
            self.Output_Group_B3.setDisabled(True)
            self.Input_Group_B3.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_B3.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_B3.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_B3.setChecked(True)
            self.Input_Group_B3.setDisabled(True)
            self.Output_Group_B3.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_B3.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_B3.setChecked(True)
                
                                
        PIN4=PORT.find('PIN4')
        DIR = PIN4.find('DIR').text
        CONF = PIN4.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_B4.setChecked(True)
            self.Output_Group_B4.setDisabled(True)
            self.Input_Group_B4.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_B4.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_B4.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_B4.setChecked(True)
            self.Input_Group_B4.setDisabled(True)
            self.Output_Group_B4.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_B4.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_B4.setChecked(True)
                
                                
        PIN5=PORT.find('PIN5')
        DIR = PIN5.find('DIR').text
        CONF = PIN5.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_B5.setChecked(True)
            self.Output_Group_B5.setDisabled(True)
            self.Input_Group_B5.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_B5.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_B5.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_B5.setChecked(True)
            self.Input_Group_B5.setDisabled(True)
            self.Output_Group_B5.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_B5.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_B5.setChecked(True)
                
                                
        PIN6=PORT.find('PIN6')
        DIR = PIN6.find('DIR').text
        CONF = PIN6.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_B6.setChecked(True)
            self.Output_Group_B6.setDisabled(True)
            self.Input_Group_B6.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_B6.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_B6.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_B6.setChecked(True)
            self.Input_Group_B6.setDisabled(True)
            self.Output_Group_B6.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_B6.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_B6.setChecked(True)
                
        PIN7=PORT.find('PIN7')
        DIR = PIN6.find('DIR').text
        CONF = PIN6.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_B7.setChecked(True)
            self.Output_Group_B7.setDisabled(True)
            self.Input_Group_B7.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_B7.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_B7.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_B7.setChecked(True)
            self.Input_Group_B7.setDisabled(True)
            self.Output_Group_B7.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_B7.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_B7.setChecked(True)
                
                #***************************************************
                
        PORT=DIO.find('PORTC')
        
        PIN0=PORT.find('PIN0')
        DIR = PIN0.find('DIR').text
        CONF = PIN0.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_C0.setChecked(True)
            self.Output_Group_C0.setDisabled(True)
            self.Input_Group_C0.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_C0.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_C0.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_C0.setChecked(True)
            self.Input_Group_C0.setDisabled(True)
            self.Output_Group_C0.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_C0.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_C0.setChecked(True)
                
        PIN1=PORT.find('PIN1')
        DIR = PIN1.find('DIR').text
        CONF = PIN1.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_C1.setChecked(True)
            self.Output_Group_C1.setDisabled(True)
            self.Input_Group_C1.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_C1.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_C1.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_C1.setChecked(True)
            self.Input_Group_C1.setDisabled(True)
            self.Output_Group_C1.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_C1.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_C1.setChecked(True)
                                
        PIN2=PORT.find('PIN2')
        DIR = PIN2.find('DIR').text
        CONF = PIN2.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_C2.setChecked(True)
            self.Output_Group_C2.setDisabled(True)
            self.Input_Group_C2.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_C2.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_C2.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_C2.setChecked(True)
            self.Input_Group_C2.setDisabled(True)
            self.Output_Group_C2.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_C2.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_C2.setChecked(True)
                
                                
        PIN3=PORT.find('PIN3')
        DIR = PIN3.find('DIR').text
        CONF = PIN3.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_C3.setChecked(True)
            self.Output_Group_C3.setDisabled(True)
            self.Input_Group_C3.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_C3.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_C3.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_C3.setChecked(True)
            self.Input_Group_C3.setDisabled(True)
            self.Output_Group_C3.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_C3.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_C3.setChecked(True)
                
                                
        PIN4=PORT.find('PIN4')
        DIR = PIN4.find('DIR').text
        CONF = PIN4.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_C4.setChecked(True)
            self.Output_Group_C4.setDisabled(True)
            self.Input_Group_C4.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_C4.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_C4.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_C4.setChecked(True)
            self.Input_Group_C4.setDisabled(True)
            self.Output_Group_C4.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_C4.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_C4.setChecked(True)
                
                                
        PIN5=PORT.find('PIN5')
        DIR = PIN5.find('DIR').text
        CONF = PIN5.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_C5.setChecked(True)
            self.Output_Group_C5.setDisabled(True)
            self.Input_Group_C5.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_C5.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_C5.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_C5.setChecked(True)
            self.Input_Group_C5.setDisabled(True)
            self.Output_Group_C5.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_C5.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_C5.setChecked(True)
                
                                
        PIN6=PORT.find('PIN6')
        DIR = PIN6.find('DIR').text
        CONF = PIN6.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_C6.setChecked(True)
            self.Output_Group_C6.setDisabled(True)
            self.Input_Group_C6.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_C6.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_C6.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_C6.setChecked(True)
            self.Input_Group_C6.setDisabled(True)
            self.Output_Group_C6.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_C6.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_C6.setChecked(True)
                
        PIN7=PORT.find('PIN7')
        DIR = PIN6.find('DIR').text
        CONF = PIN6.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_C7.setChecked(True)
            self.Output_Group_C7.setDisabled(True)
            self.Input_Group_C7.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_C7.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_C7.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_C7.setChecked(True)
            self.Input_Group_C7.setDisabled(True)
            self.Output_Group_C7.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_C7.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_C7.setChecked(True)
                #***************************************************************
                
        PORT=DIO.find('PORTD')
        
        PIN0=PORT.find('PIN0')
        DIR = PIN0.find('DIR').text
        CONF = PIN0.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_D0.setChecked(True)
            self.Output_Group_D0.setDisabled(True)
            self.Input_Group_D0.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_D0.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_D0.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_D0.setChecked(True)
            self.Input_Group_D0.setDisabled(True)
            self.Output_Group_D0.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_D0.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_D0.setChecked(True)
                
        PIN1=PORT.find('PIN1')
        DIR = PIN1.find('DIR').text
        CONF = PIN1.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_D1.setChecked(True)
            self.Output_Group_D1.setDisabled(True)
            self.Input_Group_D1.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_D1.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_D1.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_D1.setChecked(True)
            self.Input_Group_D1.setDisabled(True)
            self.Output_Group_D1.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_D1.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_D1.setChecked(True)
                                
        PIN2=PORT.find('PIN2')
        DIR = PIN2.find('DIR').text
        CONF = PIN2.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_D2.setChecked(True)
            self.Output_Group_D2.setDisabled(True)
            self.Input_Group_D2.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_D2.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_D2.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_D2.setChecked(True)
            self.Input_Group_D2.setDisabled(True)
            self.Output_Group_D2.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_D2.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_D2.setChecked(True)
                
                                
        PIN3=PORT.find('PIN3')
        DIR = PIN3.find('DIR').text
        CONF = PIN3.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_D3.setChecked(True)
            self.Output_Group_D3.setDisabled(True)
            self.Input_Group_D3.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_D3.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_D3.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_D3.setChecked(True)
            self.Input_Group_D3.setDisabled(True)
            self.Output_Group_D3.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_D3.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_D3.setChecked(True)
                
                                
        PIN4=PORT.find('PIN4')
        DIR = PIN4.find('DIR').text
        CONF = PIN4.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_D4.setChecked(True)
            self.Output_Group_D4.setDisabled(True)
            self.Input_Group_D4.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_D4.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_D4.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_D4.setChecked(True)
            self.Input_Group_D4.setDisabled(True)
            self.Output_Group_D4.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_D4.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_D4.setChecked(True)
                
                                
        PIN5=PORT.find('PIN5')
        DIR = PIN5.find('DIR').text
        CONF = PIN5.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_D5.setChecked(True)
            self.Output_Group_D5.setDisabled(True)
            self.Input_Group_D5.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_D5.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_D5.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_D5.setChecked(True)
            self.Input_Group_D5.setDisabled(True)
            self.Output_Group_D5.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_D5.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_D5.setChecked(True)
                
                                
        PIN6=PORT.find('PIN6')
        DIR = PIN6.find('DIR').text
        CONF = PIN6.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_D6.setChecked(True)
            self.Output_Group_D6.setDisabled(True)
            self.Input_Group_D6.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_D6.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_D6.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_D6.setChecked(True)
            self.Input_Group_D6.setDisabled(True)
            self.Output_Group_D6.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_D6.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_D6.setChecked(True)
                
        PIN7=PORT.find('PIN7')
        DIR = PIN6.find('DIR').text
        CONF = PIN6.find('CONFIG').text
        if DIR   == "INPUT":
            self.Input_Radio_D7.setChecked(True)
            self.Output_Group_D7.setDisabled(True)
            self.Input_Group_D7.setEnabled(True)
            if CONF == "PullUP":
                self.Pull_Up_Radio_D7.setChecked(True)
            elif CONF == "InputHigh":
                self.High_Imp_Radio_D7.setChecked(True)
        elif DIR == "OUTPUT":
            self.Output_Radio_D7.setChecked(True)
            self.Input_Group_D7.setDisabled(True)
            self.Output_Group_D7.setEnabled(True)
            if CONF == "OutputLow":
                self.Low_Radio_D7.setChecked(True)
            elif CONF == "OutputHigh":
                self.High_Radio_D7.setChecked(True)
    
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Generate_Button.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.Input_Group_A1.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_A1.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_A1.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Group_A3.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_A3.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_A3.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Pin_0_Group_A3.setTitle(QCoreApplication.translate("Form", u"Pin 3 Direction", None))
        self.Output_Radio_A3.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_A3.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Output_Group_A0.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_A0.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_A0.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_A4.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_A4.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_A4.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Pin_0_Group_A1.setTitle(QCoreApplication.translate("Form", u"Pin 1 Direction", None))
        self.Output_Radio_A1.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_A1.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Pin_0_Group_A5.setTitle(QCoreApplication.translate("Form", u"Pin 5 Direction", None))
        self.Output_Radio_A5.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_A5.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Input_Group_A7.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_A7.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_A7.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Input_Group_A3.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_A3.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_A3.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Input_Group_A6.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_A6.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_A6.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Group_A5.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_A5.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_A5.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Pin_0_Group_A0.setTitle(QCoreApplication.translate("Form", u"Pin 0 Direction", None))
        self.Output_Radio_A0.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_A0.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Pin_0_Group_A2.setTitle(QCoreApplication.translate("Form", u"Pin 2 Direction", None))
        self.Output_Radio_A2.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_A2.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Pin_0_Group_A6.setTitle(QCoreApplication.translate("Form", u"Pin 6 Direction", None))
        self.Output_Radio_A6.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_A6.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Input_Group_A2.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_A2.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_A2.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Group_A2.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_A2.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_A2.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Output_Group_A4.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_A4.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_A4.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_A5.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_A5.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_A5.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Group_A1.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_A1.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_A1.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Pin_0_Group_A7.setTitle(QCoreApplication.translate("Form", u"Pin 7 Direction", None))
        self.Output_Radio_A7.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_A7.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Output_Group_A6.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_A6.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_A6.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_A0.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_A0.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_A0.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Pin_0_Group_A4.setTitle(QCoreApplication.translate("Form", u"Pin 4 Direction", None))
        self.Output_Radio_A4.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_A4.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Output_Group_A7.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_A7.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_A7.setText(QCoreApplication.translate("Form", u"Low", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PORTA), QCoreApplication.translate("Form", u"PORTA", None))
        self.Output_Group_B4.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_B4.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_B4.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Output_Group_B2.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_B2.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_B2.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Output_Group_B3.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_B3.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_B3.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_B2.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_B2.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_B2.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Group_B5.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_B5.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_B5.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Pin_0_Group_B3.setTitle(QCoreApplication.translate("Form", u"Pin 3 Direction", None))
        self.Output_Radio_B3.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_B3.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Input_Group_B7.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_B7.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_B7.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Pin_0_Group_B4.setTitle(QCoreApplication.translate("Form", u"Pin 4 Direction", None))
        self.Output_Radio_B4.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_B4.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Input_Group_B6.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_B6.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_B6.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Pin_0_Group_B6.setTitle(QCoreApplication.translate("Form", u"Pin 6 Direction", None))
        self.Output_Radio_B6.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_B6.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Pin_0_Group_B1.setTitle(QCoreApplication.translate("Form", u"Pin 1 Direction", None))
        self.Output_Radio_B1.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_B1.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Pin_0_Group_B5.setTitle(QCoreApplication.translate("Form", u"Pin 5 Direction", None))
        self.Output_Radio_B5.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_B5.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Input_Group_B5.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_B5.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_B5.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Group_B7.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_B7.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_B7.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Pin_0_Group_B2.setTitle(QCoreApplication.translate("Form", u"Pin 2 Direction", None))
        self.Output_Radio_B2.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_B2.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Input_Group_B3.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_B3.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_B3.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Group_B0.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_B0.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_B0.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Pin_0_Group_B7.setTitle(QCoreApplication.translate("Form", u"Pin 7 Direction", None))
        self.Output_Radio_B7.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_B7.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Pin_0_Group_B0.setTitle(QCoreApplication.translate("Form", u"Pin 0 Direction", None))
        self.Output_Radio_B0.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_B0.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Input_Group_B0.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_B0.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_B0.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Group_B6.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_B6.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_B6.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_B1.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_B1.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_B1.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Group_B1.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_B1.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_B1.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_B4.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_B4.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_B4.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PORTB), QCoreApplication.translate("Form", u"PORTB", None))
        self.Pin_0_Group_C1.setTitle(QCoreApplication.translate("Form", u"Pin 1 Direction", None))
        self.Output_Radio_C1.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_C1.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Pin_0_Group_C3.setTitle(QCoreApplication.translate("Form", u"Pin 3 Direction", None))
        self.Output_Radio_C3.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_C3.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Pin_0_Group_C5.setTitle(QCoreApplication.translate("Form", u"Pin 5 Direction", None))
        self.Output_Radio_C5.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_C5.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Output_Group_C1.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_C1.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_C1.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_C2.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_C2.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_C2.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Group_C3.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_C3.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_C3.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_C4.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_C4.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_C4.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.PREV_Button.setText(QCoreApplication.translate("Form", u"Prev. PORT", None))
        self.Input_Group_C1.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_C1.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_C1.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Input_Group_C7.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_C7.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_C7.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Group_C5.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_C5.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_C5.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Output_Group_C0.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_C0.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_C0.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Output_Group_C6.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_C6.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_C6.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_C5.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_C5.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_C5.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Input_Group_C3.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_C3.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_C3.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Pin_0_Group_C4.setTitle(QCoreApplication.translate("Form", u"Pin 4 Direction", None))
        self.Output_Radio_C4.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_C4.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Pin_0_Group_C7.setTitle(QCoreApplication.translate("Form", u"Pin 7 Direction", None))
        self.Output_Radio_C7.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_C7.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Output_Group_C4.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_C4.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_C4.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Output_Group_C7.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_C7.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_C7.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_C6.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_C6.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_C6.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Pin_0_Group_C0.setTitle(QCoreApplication.translate("Form", u"Pin 0 Direction", None))
        self.Output_Radio_C0.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_C0.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Pin_0_Group_C6.setTitle(QCoreApplication.translate("Form", u"Pin 6 Direction", None))
        self.Output_Radio_C6.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_C6.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Pin_0_Group_C2.setTitle(QCoreApplication.translate("Form", u"Pin 2 Direction", None))
        self.Output_Radio_C2.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_C2.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Output_Group_C2.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_C2.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_C2.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_C0.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_C0.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_C0.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PORTC), QCoreApplication.translate("Form", u"PORTC", None))
        self.Pin_0_Group_D5.setTitle(QCoreApplication.translate("Form", u"Pin 5 Direction", None))
        self.Output_Radio_D5.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_D5.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Output_Group_D4.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_D4.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_D4.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_D1.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_D1.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_D1.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Group_D5.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_D5.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_D5.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_D3.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_D3.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_D3.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Pin_0_Group_D4.setTitle(QCoreApplication.translate("Form", u"Pin 4 Direction", None))
        self.Output_Radio_D4.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_D4.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Input_Group_D5.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_DD5.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_D5.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Pin_0_Group_D7.setTitle(QCoreApplication.translate("Form", u"Pin 7 Direction", None))
        self.Output_Radio_D7.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_D7.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Output_Group_D7.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_D7.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_D7.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Pin_0_Group_D6.setTitle(QCoreApplication.translate("Form", u"Pin 6 Direction", None))
        self.Output_Radio_D6.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_D6.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Pin_0_Group_D3.setTitle(QCoreApplication.translate("Form", u"Pin 3 Direction", None))
        self.Output_Radio_D3.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_D3.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Input_Group_D2.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_D2.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_D2.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Pin_0_Group_D1.setTitle(QCoreApplication.translate("Form", u"Pin 1 Direction", None))
        self.Output_Radio_D1.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_D1.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Pin_0_Group_D2.setTitle(QCoreApplication.translate("Form", u"Pin 2 Direction", None))
        self.Output_Radio_D2.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_D2.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Output_Group_D2.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_D2.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_D2.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Output_Group_D3.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_D3.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_D3.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_D7.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_D7.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_D7.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Input_Group_D6.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_D6.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_D6.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Group_D0.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_D0.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_D0.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_D4.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_D4.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_D4.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Group_D1.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_D1.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_D1.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group_D0.setTitle(QCoreApplication.translate("Form", u"Input Configration", None))
        self.Pull_Up_Radio_D0.setText(QCoreApplication.translate("Form", u"Pull_Up", None))
        self.High_Imp_Radio_D0.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Group_D6.setTitle(QCoreApplication.translate("Form", u"Output Configration", None))
        self.High_Radio_D6.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_Radio_D6.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Pin_0_Group_D0.setTitle(QCoreApplication.translate("Form", u"Pin 0 Direction", None))
        self.Output_Radio_D0.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_Radio_D0.setText(QCoreApplication.translate("Form", u"Input", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PORTD), QCoreApplication.translate("Form", u"PORTD", None))
        self.Save_Button.setText(QCoreApplication.translate("Form", u"Save", None))
        self.Load_Button.setText(QCoreApplication.translate("Form", u"Load", None))
    # retranslateUi

app=QApplication(sys.argv)
Widget=QWidget()
Form=Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())