# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Driver_Files_Creator.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(466, 528)
        self.Generate_pushButton = QPushButton(Form)
        self.Generate_pushButton.setObjectName(u"Generate_pushButton")
        self.Generate_pushButton.setGeometry(QRect(210, 360, 93, 28))
        self.Path_lineEdit = QLineEdit(Form)
        self.Path_lineEdit.setObjectName(u"Path_lineEdit")
        self.Path_lineEdit.setGeometry(QRect(20, 50, 401, 31))
        self.Periperal_lineEdit = QLineEdit(Form)
        self.Periperal_lineEdit.setObjectName(u"Periperal_lineEdit")
        self.Periperal_lineEdit.setGeometry(QRect(20, 140, 401, 31))
        self.Author_lineEdit = QLineEdit(Form)
        self.Author_lineEdit.setObjectName(u"Author_lineEdit")
        self.Author_lineEdit.setGeometry(QRect(20, 220, 391, 31))
        self.Path_label = QLabel(Form)
        self.Path_label.setObjectName(u"Path_label")
        self.Path_label.setGeometry(QRect(20, 20, 101, 21))
        font = QFont()
        font.setPointSize(10)
        self.Path_label.setFont(font)
        self.peripheral_label_ = QLabel(Form)
        self.peripheral_label_.setObjectName(u"peripheral_label_")
        self.peripheral_label_.setGeometry(QRect(20, 100, 131, 31))
        self.peripheral_label_.setFont(font)
        self.Author_label = QLabel(Form)
        self.Author_label.setObjectName(u"Author_label")
        self.Author_label.setGeometry(QRect(20, 190, 55, 16))
        self.Author_label.setFont(font)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 270, 101, 61))
        self.CFG_radioButton = QRadioButton(self.groupBox)
        self.CFG_radioButton.setObjectName(u"CFG_radioButton")
        self.CFG_radioButton.setGeometry(QRect(30, 30, 95, 20))
        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 330, 101, 51))
        self.H_radioButton = QRadioButton(self.groupBox_4)
        self.H_radioButton.setObjectName(u"H_radioButton")
        self.H_radioButton.setGeometry(QRect(30, 20, 95, 20))
        self.groupBox_5 = QGroupBox(Form)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 380, 101, 51))
        self.C_radioButto = QRadioButton(self.groupBox_5)
        self.C_radioButto.setObjectName(u"C_radioButto")
        self.C_radioButto.setGeometry(QRect(30, 20, 95, 20))
        self.groupBox_6 = QGroupBox(Form)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(20, 440, 101, 51))
        self.PRV_radioButton = QRadioButton(self.groupBox_6)
        self.PRV_radioButton.setObjectName(u"PRV_radioButton")
        self.PRV_radioButton.setGeometry(QRect(30, 10, 95, 20))

        self.retranslateUi(Form)
        
        self.Generate_pushButton.clicked.connect(self.GenerateFunction)
        
        QMetaObject.connectSlotsByName(Form)
        
    # setupUi
    def GenerateFunction(self):
      current_date = str(datetime.date.today())
      
      if self.C_radioButto.isChecked() :
        Output_Path =  self.Path_lineEdit.text() + r'\\'+self.Periperal_lineEdit.text() +  '.c'
        File_Handler = open(Output_Path ,'w')
        File_Handler.write("/*******************************************/\n")
        File_Handler.write("/*" +  self.Periperal_lineEdit.text() + " Driver\n")
        File_Handler.write( "Target: ATMEGA32\n")
        File_Handler.write("Author :"+self.Author_lineEdit.text()+ "\n"        )
        File_Handler.write(" Date:" + current_date +  " */ \n")
        File_Handler.write("/*******************************************/\n")
        File_Handler.close()
        
      if self.H_radioButton.isChecked() :
        Output_Path =  self.Path_lineEdit.text() + r'\\'+ self.Periperal_lineEdit.text() +  '.h'
        File_Handler = open(Output_Path ,'w')
        File_Handler.write("/*******************************************/\n")
        File_Handler.write("/*" +  self.Periperal_lineEdit.text() + " Driver\n")
        File_Handler.write( "Target: ATMEGA32\n")
        File_Handler.write("Author :"+self.Author_lineEdit.text()+ "\n"        )
        File_Handler.write(" Date:"+current_date + "*/\n")
        File_Handler.write("/*******************************************/\n")
        
        File_Handler.write("#ifndef _"+ self.Periperal_lineEdit.text()+"_H\n")
        File_Handler.write("#define _"+ self.Periperal_lineEdit.text() +"_H\n")
        File_Handler.write("\n")
        File_Handler.write("\n")
        File_Handler.write("#endif /*" + self.Periperal_lineEdit.text() +"_H*/\n")
        File_Handler.close()
        
      if self.CFG_radioButton.isChecked() :
        Output_Path =  self.Path_lineEdit.text() + r'\\'+ self.Periperal_lineEdit.text() +  '_Cfg.h'
        File_Handler = open(Output_Path ,'w')
        File_Handler.write("/*******************************************/\n")
        File_Handler.write("/*" +  self.Periperal_lineEdit.text() + " Driver\n")
        File_Handler.write( "Target: ATMEGA32\n")
        File_Handler.write("Author :"+self.Author_lineEdit.text()+ "\n"        )
        File_Handler.write(" Date:"+current_date + "*/\n")
        File_Handler.write("/*******************************************/\n")
        
        File_Handler.write("#ifndef _"+ self.Periperal_lineEdit.text()+"_CFG_H\n")
        File_Handler.write("#define _"+ self.Periperal_lineEdit.text() +"_CFG_H\n")
        File_Handler.write("\n")
        File_Handler.write("\n")
        File_Handler.write("#endif /*" + self.Periperal_lineEdit.text() +"_CFG_H*/\n")
        File_Handler.close()
        
      if self.PRV_radioButton.isChecked() :
        Output_Path =  self.Path_lineEdit.text() + r'\\'+ self.Periperal_lineEdit.text() +  '_Prv.h'
        File_Handler = open(Output_Path ,'w')
        File_Handler.write("/*******************************************/\n")
        File_Handler.write("/*" +  self.Periperal_lineEdit.text() + " Driver\n")
        File_Handler.write( "Target: ATMEGA32\n")
        File_Handler.write("Author :"+self.Author_lineEdit.text()+ "\n"        )
        File_Handler.write(" Date:"+current_date + "*/\n")
        File_Handler.write("/*******************************************/\n")
    
        File_Handler.write("\n")
        File_Handler.write("#ifndef _"+ self.Periperal_lineEdit.text()+"_PRV_H\n")
        File_Handler.write("#define _"+ self.Periperal_lineEdit.text() +"_PRV_H\n")
        File_Handler.write("\n")
        File_Handler.write("\n")
        File_Handler.write("#endif /*" + self.Periperal_lineEdit.text() +"_PRV_H*/\n")
        File_Handler.close()
        
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Generate_pushButton.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.Path_label.setText(QCoreApplication.translate("Form", u"Output Path", None))
        self.peripheral_label_.setText(QCoreApplication.translate("Form", u"Peripheral Name", None))
        self.Author_label.setText(QCoreApplication.translate("Form", u"Author", None))
        self.groupBox.setTitle("")
        self.CFG_radioButton.setText(QCoreApplication.translate("Form", u"cfg", None))
        self.groupBox_4.setTitle("")
        self.H_radioButton.setText(QCoreApplication.translate("Form", u".h", None))
        self.groupBox_5.setTitle("")
        self.C_radioButto.setText(QCoreApplication.translate("Form", u".c", None))
        self.groupBox_6.setTitle("")
        self.PRV_radioButton.setText(QCoreApplication.translate("Form", u"prv", None))
    # retranslateUi
app=QApplication(sys.argv)
Widget=QWidget()
Form=Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())
