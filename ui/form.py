# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/markusehrlich/Python-Entwicklung/Steuerzentrale2/ui/form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_qtWindow(object):
    def setupUi(self, qtWindow):
        qtWindow.setObjectName("qtWindow")
        qtWindow.setEnabled(True)
        qtWindow.resize(1107, 618)
        self.groupBox_infotext = QtWidgets.QGroupBox(qtWindow)
        self.groupBox_infotext.setGeometry(QtCore.QRect(290, 20, 801, 521))
        self.groupBox_infotext.setObjectName("groupBox_infotext")
        self.infotext = QtWidgets.QTextEdit(self.groupBox_infotext)
        self.infotext.setEnabled(True)
        self.infotext.setGeometry(QtCore.QRect(10, 60, 771, 411))
        self.infotext.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.infotext.setAcceptRichText(True)
        self.infotext.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.infotext.setObjectName("infotext")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_infotext)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 771, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fettschrift = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fettschrift.setFont(font)
        self.fettschrift.setCheckable(True)
        self.fettschrift.setObjectName("fettschrift")
        self.horizontalLayout.addWidget(self.fettschrift)
        self.kursivschrift = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.kursivschrift.setEnabled(True)
        font = QtGui.QFont()
        font.setItalic(True)
        self.kursivschrift.setFont(font)
        self.kursivschrift.setCheckable(True)
        self.kursivschrift.setChecked(False)
        self.kursivschrift.setAutoExclusive(False)
        self.kursivschrift.setAutoDefault(False)
        self.kursivschrift.setDefault(False)
        self.kursivschrift.setObjectName("kursivschrift")
        self.horizontalLayout.addWidget(self.kursivschrift)
        self.unterstreichen = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.unterstreichen.setFont(font)
        self.unterstreichen.setCheckable(True)
        self.unterstreichen.setObjectName("unterstreichen")
        self.horizontalLayout.addWidget(self.unterstreichen)
        self.rot = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.rot.setCheckable(True)
        self.rot.setObjectName("rot")
        self.horizontalLayout.addWidget(self.rot)
        self.gruen = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.gruen.setCheckable(True)
        self.gruen.setObjectName("gruen")
        self.horizontalLayout.addWidget(self.gruen)
        self.datum = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.datum.setObjectName("datum")
        self.horizontalLayout.addWidget(self.datum)
        self.normal = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.normal.setObjectName("normal")
        self.horizontalLayout.addWidget(self.normal)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_infotext)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 470, 771, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.alle_stationen_speichern = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.alle_stationen_speichern.setChecked(True)
        self.alle_stationen_speichern.setObjectName("alle_stationen_speichern")
        self.horizontalLayout_2.addWidget(self.alle_stationen_speichern)
        self.eine_stationen_speichern = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.eine_stationen_speichern.setObjectName("eine_stationen_speichern")
        self.horizontalLayout_2.addWidget(self.eine_stationen_speichern)
        self.speichern_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.speichern_button.setFont(font)
        self.speichern_button.setObjectName("speichern_button")
        self.horizontalLayout_2.addWidget(self.speichern_button)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.drucken_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.drucken_button.setObjectName("drucken_button")
        self.horizontalLayout_2.addWidget(self.drucken_button)
        self.beenden_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.beenden_button.setObjectName("beenden_button")
        self.horizontalLayout_2.addWidget(self.beenden_button)
        self.groupBox_modus = QtWidgets.QGroupBox(qtWindow)
        self.groupBox_modus.setGeometry(QtCore.QRect(20, 20, 261, 121))
        self.groupBox_modus.setObjectName("groupBox_modus")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_modus)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 251, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.modus_infotexte = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.modus_infotexte.setFont(font)
        self.modus_infotexte.setChecked(True)
        self.modus_infotexte.setObjectName("modus_infotexte")
        self.verticalLayout.addWidget(self.modus_infotexte)
        self.modus_freitext = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.modus_freitext.setFont(font)
        self.modus_freitext.setObjectName("modus_freitext")
        self.verticalLayout.addWidget(self.modus_freitext)
        self.modus_bestellhistorie = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.modus_bestellhistorie.setFont(font)
        self.modus_bestellhistorie.setObjectName("modus_bestellhistorie")
        self.verticalLayout.addWidget(self.modus_bestellhistorie)
        self.modus_bestellhistorie_alle = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.modus_bestellhistorie_alle.setFont(font)
        self.modus_bestellhistorie_alle.setObjectName("modus_bestellhistorie_alle")
        self.verticalLayout.addWidget(self.modus_bestellhistorie_alle)
        self.groupBox_2 = QtWidgets.QGroupBox(qtWindow)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 160, 251, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.kliniken = QtWidgets.QComboBox(self.groupBox_2)
        self.kliniken.setGeometry(QtCore.QRect(10, 20, 221, 32))
        self.kliniken.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.kliniken.setObjectName("kliniken")
        self.groupBox_3 = QtWidgets.QGroupBox(qtWindow)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 240, 251, 301))
        self.groupBox_3.setObjectName("groupBox_3")
        self.stationsauswahl = QtWidgets.QListWidget(self.groupBox_3)
        self.stationsauswahl.setGeometry(QtCore.QRect(10, 30, 231, 261))
        self.stationsauswahl.setObjectName("stationsauswahl")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(qtWindow)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 550, 1031, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.nutzerverwaltung_link = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.nutzerverwaltung_link.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.nutzerverwaltung_link.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nutzerverwaltung_link.setAlignment(QtCore.Qt.AlignCenter)
        self.nutzerverwaltung_link.setObjectName("nutzerverwaltung_link")
        self.horizontalLayout_3.addWidget(self.nutzerverwaltung_link)
        self.khonline_link = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.khonline_link.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.khonline_link.setFrameShadow(QtWidgets.QFrame.Raised)
        self.khonline_link.setAlignment(QtCore.Qt.AlignCenter)
        self.khonline_link.setObjectName("khonline_link")
        self.horizontalLayout_3.addWidget(self.khonline_link)

        self.retranslateUi(qtWindow)
        QtCore.QMetaObject.connectSlotsByName(qtWindow)

    def retranslateUi(self, qtWindow):
        _translate = QtCore.QCoreApplication.translate
        qtWindow.setWindowTitle(_translate("qtWindow", "qtWindow"))
        self.groupBox_infotext.setTitle(_translate("qtWindow", "Info-Texte bearbeiten"))
        self.infotext.setHtml(_translate("qtWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.fettschrift.setText(_translate("qtWindow", "fett"))
        self.kursivschrift.setText(_translate("qtWindow", "kursiv"))
        self.unterstreichen.setText(_translate("qtWindow", "unterstreichen"))
        self.rot.setText(_translate("qtWindow", "rot"))
        self.gruen.setText(_translate("qtWindow", "gr??n"))
        self.datum.setText(_translate("qtWindow", "Datum einf??gen"))
        self.normal.setText(_translate("qtWindow", "normal"))
        self.alle_stationen_speichern.setText(_translate("qtWindow", "alle Stationen dieser Klinik ..."))
        self.eine_stationen_speichern.setText(_translate("qtWindow", "nur diese Station..."))
        self.speichern_button.setText(_translate("qtWindow", "speichern"))
        self.drucken_button.setText(_translate("qtWindow", "drucken"))
        self.beenden_button.setText(_translate("qtWindow", "beenden"))
        self.groupBox_modus.setTitle(_translate("qtWindow", "Arbeitsmodus"))
        self.modus_infotexte.setText(_translate("qtWindow", "Info-Texte"))
        self.modus_freitext.setText(_translate("qtWindow", "aktuelle Freitext-Bestellungen"))
        self.modus_bestellhistorie.setText(_translate("qtWindow", "Bestellhistorie Klinik-> Stationen"))
        self.modus_bestellhistorie_alle.setText(_translate("qtWindow", "Bestellhistorie alle Kliniken"))
        self.groupBox_2.setTitle(_translate("qtWindow", "Klinik"))
        self.groupBox_3.setTitle(_translate("qtWindow", "Stationen"))
        self.nutzerverwaltung_link.setText(_translate("qtWindow", "Nutzerverwaltung ??ffnen"))
        self.khonline_link.setText(_translate("qtWindow", "KH-Online ??ffnen"))
