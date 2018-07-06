# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\WELLL\Documents\Eric\ConfigGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(788, 405)
        self.btn_usrname = QtWidgets.QLineEdit(Form)
        self.btn_usrname.setGeometry(QtCore.QRect(500, 190, 113, 20))
        self.btn_usrname.setObjectName("btn_usrname")
        self.btn_psw = QtWidgets.QLineEdit(Form)
        self.btn_psw.setGeometry(QtCore.QRect(500, 240, 113, 20))
        self.btn_psw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btn_psw.setObjectName("btn_psw")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(650, 230, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 280, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(470, 190, 54, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(470, 240, 54, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(500, 290, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(460, 290, 54, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 371, 261))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./images/1.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 40, 351, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("./images/2.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(400, 110, 411, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(430, 40, 54, 12))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(410, 130, 54, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(470, 70, 291, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(650, 390, 141, 16))
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录信息设置Demo beta 1.0"))
        self.pushButton.setText(_translate("Form", "更改配置信息"))
        self.pushButton_2.setText(_translate("Form", "查询当前配置信息"))
        self.label.setText(_translate("Form", "学号"))
        self.label_2.setText(_translate("Form", "密码"))
        self.comboBox.setCurrentText(_translate("Form", "校园网"))
        self.comboBox.setItemText(0, _translate("Form", "校园网"))
        self.comboBox.setItemText(1, _translate("Form", "中国电信"))
        self.comboBox.setItemText(2, _translate("Form", "中国联通"))
        self.comboBox.setItemText(3, _translate("Form", "中国移动"))
        self.label_3.setText(_translate("Form", "运营商"))
        self.label_7.setText(_translate("Form", "功能区"))
        self.label_8.setText(_translate("Form", "请在功能区内填写您的配置信息"))
        self.label_9.setText(_translate("Form", "Author:WellLee"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

