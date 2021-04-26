# KH-Online Steuerzentrale 2
# Dient zur Bearbeitung der Info-Texte für die Startseite von KH-Online, der Anzeige von aktuellen
# Freitextanforderungen und bietet Zugriff auf die Bestellhistorie der Stationen.
#
# Das Programm bietet durch die Qt5-Library eine graphische Benutzeroberfläche, die Plattform unabhängig ist.
# Die GUI wurde mit Qt Creator ( https://www.qt.io ) erstellt. Das Design wird als XML-Datei gespeichert (*.ui)
# Qt5 bietet ein Tool, das aus dem XML-File ein Python-File übersetzt: uic
# from PyQt5 import uic
# uic.compileUiDir("ui")  <--- übersetzt alle ui-Files im Ordner ui zu *.py files
# Das *.py File (hier form.py) enthält die Beschreibung der Design-Elemente der GUI als Python-Code und wird über
# from ui.form import Ui_qtWindow
# eingebunden (s.u.)
# Parameter wie Pfadnamen sind in der steuerzentrale.ini Datei hinterlegt und werden über den ConfigParser eingelesen
#
# Um eine Standalone-Lösung für die verschiedenen Plattformen zu generieren wird die Bibliothek cx_freeze benötigt
# ( https://pypi.org/project/cx-Freeze/ ) das auf der Zielplattform (z.B. Windows 10 in einer VM) ausgeführt wird.
# python set_up_exe.py build (s. setup-Script in diesem Ordner) erzeugt eine *.exe + DLLs
# Die Windowsinstallation muss für den Compilierungsvorgang natürlich alle Bibiotheken (Python >3.5, Qt5) bereitstellen
# 
# Bis auf Qt5 werden nur Standardbibliotheken verwendet
# (c) Dr. Markus Ehrlich, dona GmbH&CoKG
#
# Version 0.5, 04.10.20
# Version 0.6, 07.10.20: Speichern der Info-Texte wird mit Messagebox bestätigt.
# Version 0.7, 15.10.20: Link-Button Nutzerverwaltung und KH-Online
# Version 0.8, 17.04.21: Button "grün" für Info-Textgestaltung hinzugefügt, Versionsnummer in Window-Title
# Version 0.81, 23.04.21: Config-File wird relativ zum Working-Dir ("Path") eingelesen
# Version 0.9, 23.04.21: Arbeitsmodus "Bestellhistorie alle Kliniken" hinzugefügt um alle Bestellungen aller
#                        Kliniken anzuzeigen.

import sys
import os
from datetime import date
from PyQt5 import QtWidgets, QtGui, QtPrintSupport
from ui.form import Ui_qtWindow #aus den Unterordner ui wird form.py mit den Design-Beschreibungen eingebunden
from configparser import ConfigParser
from pathlib import Path

version = "v0.9"

# *
# Es folgen die Funktionen, die den verschiedenen Push-Buttons für das Anklicken zugeordnet sind
# *

def infotext_normal():
    # Button <normal>: Stellt alle Schrift-Attribute auf Standard-Schrift
    ui.infotext.setFontWeight(50)
    ui.infotext.setTextColor(QtGui.QColor(0, 0, 0))
    ui.infotext.setFontUnderline(False)
    ui.infotext.setFontItalic(False)

    # Falls Buttons für Schrift-Attribute angewählt waren, diese deselektieren
    ui.rot.setChecked(False)
    ui.fettschrift.setChecked(False)
    ui.kursivschrift.setChecked(False)
    ui.unterstreichen.setChecked(False)

    ui.infotext.setFont(QtGui.QFont('Arial', 12))
    ui.infotext.setFontPointSize(12)

    ui.infotext.repaint()


def beenden():
    # Button <beenden>: Programm wird geschlossen
    window.close()


def drucken():
    # ruft Qt5 Druckdialog auf und übergibt Inhalt des Info-Text Bereiches (QTextEdit Objekt infotext) an den Drucker
    dialog = QtPrintSupport.QPrintDialog()
    if dialog.exec_() == QtWidgets.QDialog.Accepted:
        ui.infotext.document().print_(dialog.printer())


def infotext_datum():
    # Button <Datum einfügen>: fügt das aktuelle Datum an der Cursorposition ein
    heute = date.today()
    ui.infotext.insertPlainText(str(heute.strftime("%d.%m.%Y ")))
    ui.infotext.repaint()


def infotext_fett():
    # Button <fett>: stellt die Schrift auf fett um
    if ui.fettschrift.isChecked():
        ui.infotext.setFontWeight(200)
    else:
        ui.infotext.setFontWeight(50)

    # prüft ob ein Textblock selektiert wurde und führt ggf ein repaint aus, um den Textblock auf fett umzustellen
    schreibmarke = ui.infotext.textCursor()
    if len(schreibmarke.selectedText()) > 0:
        ui.fettschrift.setChecked(False)
        ui.fettschrift.repaint()


def infotext_rot():
    # Button <rot>: stellt die Schrift auf Farbe Rot um
    if ui.rot.isChecked():
        ui.infotext.setTextColor(QtGui.QColor(255,0,0))
    else:
        ui.infotext.setTextColor(QtGui.QColor(0,0,0))

    # prüft ob ein Textblock selektiert wurde und führt ggf ein repaint aus, um den Textblock auf rot umzustellen
    schreibmarke = ui.infotext.textCursor()
    if len(schreibmarke.selectedText()) > 0:
        ui.rot.setChecked(False)
        ui.unterstreichen.repaint()

def infotext_gruen():
    # Button <rot>: stellt die Schrift auf Farbe Rot um
    if ui.gruen.isChecked():
        ui.infotext.setTextColor(QtGui.QColor(0,204,0))
    else:
        ui.infotext.setTextColor(QtGui.QColor(0,0,0))

    # prüft ob ein Textblock selektiert wurde und führt ggf ein repaint aus, um den Textblock auf rot umzustellen
    schreibmarke = ui.infotext.textCursor()
    if len(schreibmarke.selectedText()) > 0:
        ui.gruen.setChecked(False)
        ui.unterstreichen.repaint()

def infotext_unterstreichen():
    # Button <unterstreichen>: stellt die Schrift auf Attribut unterstreichen um
    if ui.unterstreichen.isChecked():
        ui.infotext.setFontUnderline(True)
    else:
        ui.infotext.setFontUnderline(False)

    # prüft ob ein Textblock selektiert wurde, führt ggf ein repaint aus, um den Textblock auf unterstreichen umzustellen
    schreibmarke = ui.infotext.textCursor()
    if len(schreibmarke.selectedText()) > 0:
        ui.unterstreichen.setChecked(False)
        ui.unterstreichen.repaint()

def infotext_kursiv():
    # Button <kursiv>: stellt Schrift auf kursiv um
    if ui.kursivschrift.isChecked():
        ui.infotext.setFontItalic(True)
    else:
        ui.infotext.setFontItalic(False)

    # prüft ob ein Textblock selektiert wurde, führt ggf ein repaint aus, um den Textblock auf kursiv umzustellen
    schreibmarke = ui.infotext.textCursor()
    if len(schreibmarke.selectedText()) > 0:
        ui.kursivschrift.setChecked(False)
        ui.kursivschrift.repaint()


# *
# Es folgen die Funktionen, die der ComboBox Klinik-Auswahl und dem List-Widget Station-Auswahl zugeordnet sind
# *

def klinik_auswahl():
    # die in der ComboBox aktuell ausgwählte Zeile = Klinik auslesen
    klinik_auswahl = str(ui.kliniken.currentText())
    ui.stationsauswahl.clear()
    # die Liste der Stationen der Klinik aus dem Klinik-Stationen-Dict in das Stationen-Feld schreiben
    ui.stationsauswahl.addItems(klinik_dic[klinik_auswahl])
    # immer erste Station im ListWidget auswählen (erspart einen Mausklick um Bearbeitung zu starten)
    ui.stationsauswahl.setCurrentRow(0)
    # Einlesen und Anzeigen des Info-Textes aufrufen
    stationen_auswahl()


def stationen_auswahl():
    # die im ListWidget aktuell angeklickte Zeile = Station holen
    st_auswahl = str(ui.stationsauswahl.currentItem().text())

    # Überprüfen, welcher Arbeitsmodus (Radio-Buttons) gewählt wurde:
    # Modus Infotexte bearbeiten -> der Info-Text der ausgewählten Station wird in das Text-Edit Feld geladen
    if ui.modus_infotexte.isChecked():
        try:
            with open(info_path + st_auswahl + ".html", "r") as f:
                html_text = f.read()
        except IOError as error:
            message_box(str(error))
            sys.exit(error)

        ui.infotext.setText(html_text)
        # Die Überschrift der Info-Text GroupBox wird um die Station ergänzt, damit klar ist,
        # welcher Stationstext bearbeitet wird
        ui.groupBox_infotext.setTitle("Info-Texte bearbeiten " + st_auswahl)

    # Modus Bestellhistorie: -> die Bestellhistorie wird in das Text-Editfeld geladen
    if ui.modus_bestellhistorie.isChecked():
        ui.infotext.clear()

        # aktuellen Arbeitspfad setzen
        os.chdir(historien_path)
        # Liste aufbauen mit allen Files des Ordners der Bestellhistorien und nach "zuletzt geändert" sortieren
        # jüngste Bestellung zuerst (=reverse)
        files_sorted = sorted(os.listdir(), key=os.path.getmtime, reverse=True)

        # die files_sorted Liste enthält alle Files des Ordners. Es werden jetzt nur html Files die mit der
        # ausgewählten Station beginnen z.B. 961-123456789.html
        historien_filenames = [f for f in files_sorted if (f.endswith('.html')) and (f.startswith(st_auswahl + "-"))]

        # die Liste historien_filenames enthält alle vergangenen Bestellungen der gewählten Station.
        # diese Bestelldateien werden nacheinander in das TextFeld geladen ("insertHtml")
        for files in historien_filenames:
            try:
                with open(historien_path + files, "r", encoding='ISO-8859-1') as f:
                    html_text = f.read()
            except IOError as error:
                message_box(str(error))
                sys.exit(error)

            ui.infotext.insertHtml(html_text)

        # Die Überschrift der Info-Text GroupBox wird um die Station ergänzt, damit klar ist,
        # von welcher Station die Bestellungen angezeigt werden.
        ui.groupBox_infotext.setTitle("Bestellhistorie " + st_auswahl)


def infotext_speichern():

    if not ui.stationsauswahl.currentItem():
        message_box("Bitte zuerst eine Station auswählen!")
        return

    text_html = ui.infotext.toHtml()
    st_auswahl = str(ui.stationsauswahl.currentItem().text())

    if ui.eine_stationen_speichern.isChecked():
        try:
            with open(info_path + st_auswahl + '.html', 'w') as f:
                f.write(text_html)
        except IOError as error:
            message_box(str(error))
            sys.exit(error)
        message_box("Infotext für Station " + st_auswahl + " wurde erfolgreich gespeichert.")

    if ui.alle_stationen_speichern.isChecked():
        klinik_auswahl = str(ui.kliniken.currentText())
        stationen = klinik_dic[klinik_auswahl]
        for station in stationen:
            try:
                with open(info_path + station + '.html', 'w') as f:
                    f.write(text_html)
            except IOError as error:
                message_box(str(error))
                sys.exit(error)
        message_box("Alle Infotexte für " + klinik_auswahl + " wurden erfolgreich gespeichert.")


def kliniken_einlesen():
    # alle Text-Dateien im Info-Seiten Ordner finden und in die Liste kliniken_filenames schreiben
    kliniken_filenames = [f for f in os.listdir(info_path) if f.endswith('.txt')]

    # Datei-Index .txt aus allen Einträgen in der Liste der Klinik-Namen entfernen
    kliniken = sorted([name.strip(".txt") for name in kliniken_filenames])

    # Das Klinik-Dict wird im Folgenden gefüllt:
    # Format: {'sprudelhof-stationen': ['431', '432', '433', '434', '435', '436', '437', '438']}
    klinik_dic = {}

    for klinik in kliniken:
        try:
            with open(info_path+klinik+'.txt', 'r', encoding='utf-8') as f:
                stationen = f.read().splitlines()
        except IOError as error:
            message_box(str(error))
            sys.exit(error)

        # die Liste Stationen wird durchgegangen und nur nichtleere Einträge werden übernommen
        # Hintergrund: in den Textfiles (z.B. marien-stationen.txt) befinden sich manchmal am Ende Leerzeilen
        stationen = [x for x in stationen if x]
        # Die Liste der Stationen wird jetzt der Klinik im Dict zugeordnet
        klinik_dic[klinik] = stationen

    return klinik_dic

def modus_bestellhistorie():
    ui.groupBox_infotext.setTitle("Bestellhistorie")
    ui.infotext.clear()
    ui.alle_stationen_speichern.setDisabled(True)
    ui.eine_stationen_speichern.setDisabled(True)
    ui.speichern_button.setDisabled(True)
    ui.fettschrift.setDisabled(True)
    ui.kursivschrift.setDisabled(True)
    ui.unterstreichen.setDisabled(True)
    ui.rot.setDisabled(True)
    ui.normal.setDisabled(True)
    ui.datum.setDisabled(True)

    ui.kliniken.setDisabled(False)
    ui.stationsauswahl.setDisabled(False)

    ui.infotext.setReadOnly(True)

def modus_bestellhistorie_alle():
    ui.groupBox_infotext.setTitle("Bestellhistorie aller Kliniken")
    ui.infotext.clear()
    ui.alle_stationen_speichern.setDisabled(True)
    ui.eine_stationen_speichern.setDisabled(True)
    ui.speichern_button.setDisabled(True)
    ui.fettschrift.setDisabled(True)
    ui.kursivschrift.setDisabled(True)
    ui.unterstreichen.setDisabled(True)
    ui.rot.setDisabled(True)
    ui.normal.setDisabled(True)
    ui.datum.setDisabled(True)
    # Auswahlmöglichkeit für Klinik/Station deaktivieren, da gesamte Bestellhistorie angezeigt werden soll
    ui.kliniken.setDisabled(True)
    ui.stationsauswahl.setDisabled(True)

    ui.infotext.setReadOnly(True)
    ui.infotext.clear()

    # aktuellen Arbeitspfad setzen
    os.chdir(historien_path)
    # Liste aufbauen mit allen Files des Ordners der Bestellhistorien und nach "zuletzt geändert" sortieren
    # jüngste Bestellung zuerst (=reverse)
    files_sorted = sorted(os.listdir(), key=os.path.getmtime, reverse=True)

    # sicherheitshalber auf html-Files beschränken
    historien_filenames = [f for f in files_sorted if (f.endswith('.html'))]

    # die Liste historien_filenames enthält alle vergangenen Bestellungen.
    # diese Bestelldateien werden nacheinander in das TextFeld geladen ("insertHtml")
    for files in historien_filenames:
        try:
            with open(historien_path + files, "r", encoding='ISO-8859-1') as f:
                html_text = f.read()
        except IOError as error:
            message_box(str(error))
            sys.exit(error)

        ui.infotext.insertHtml(html_text)

    # Die Überschrift der Info-Text GroupBox wird um die Station ergänzt, damit klar ist,
    # von welcher Station die Bestellungen angezeigt werden.
    ui.groupBox_infotext.setTitle("Gesamte Bestellhistorie aller Kliniken!")


def modus_infotexte():
    ui.groupBox_infotext.setTitle("Info-Texte bearbeiten")
    ui.infotext.clear()
    ui.alle_stationen_speichern.setDisabled(False)
    ui.eine_stationen_speichern.setDisabled(False)
    ui.speichern_button.setDisabled(False)
    ui.fettschrift.setDisabled(False)
    ui.kursivschrift.setDisabled(False)
    ui.unterstreichen.setDisabled(False)
    ui.rot.setDisabled(False)
    ui.normal.setDisabled(False)
    ui.datum.setDisabled(False)

    ui.kliniken.setDisabled(False)
    ui.stationsauswahl.setDisabled(False)

    ui.infotext.setReadOnly(False)


def modus_freitext():
    ui.groupBox_infotext.setTitle("aktuelle Freitext Bestellungen")
    infotext_normal()
    ui.infotext.clear()

    ui.alle_stationen_speichern.setDisabled(True)
    ui.eine_stationen_speichern.setDisabled(True)
    ui.speichern_button.setDisabled(True)

    ui.fettschrift.setDisabled(False)
    ui.kursivschrift.setDisabled(False)
    ui.unterstreichen.setDisabled(False)
    ui.rot.setDisabled(False)
    ui.normal.setDisabled(False)
    ui.datum.setDisabled(False)

    ui.kliniken.setDisabled(True)
    ui.stationsauswahl.setDisabled(True)

    ui.infotext.setReadOnly(False)

    os.chdir(freitext_path)
    files_sorted = sorted(os.listdir(), key=os.path.getmtime, reverse=True)

    freitext_filenames = [f for f in files_sorted if f.endswith('.APO')]

    # Datei-Index .txt aus allen Einträgen in der Liste der Klinik-Namen entfernen
    # kliniken = sorted([name.strip(".txt") for name in kliniken_filenames])

    for files in freitext_filenames:
        try:
            with open(freitext_path + files, "r", encoding='ISO-8859-1') as f:
                plain_text = f.read()
        except IOError as error:
            message_box(str(error))
            sys.exit(error)

        ui.infotext.insertPlainText(plain_text)

    ui.infotext.repaint()

def message_box(error):
    msgBox  = QtWidgets.QMessageBox()
    msgBox.setText(error)
    msgBox.setWindowTitle("Information")
    msgBox.exec()


# aus der Parameterdatei werden die Pfade geholt
filepath = Path(__file__).resolve().parent #holt das Workking-Directory
configfile = f'{filepath}/steuerzentrale.ini'
config = ConfigParser()
config.read(configfile)


info_path = config.get('Pfade', 'info_path')
historien_path = config.get('Pfade', 'historien_path')
freitext_path = config.get('Pfade', 'freitext_path')
khonline_link = config.get('URL', 'khonline_link')
nutzerverwaltung_link = config.get('URL', 'nutzerverwaltung_link')

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
ui = Ui_qtWindow()
ui.setupUi(window)
window.setWindowTitle("KH-Online 2.0 Steuerzentrale " + version)

ui.khonline_link.setText(khonline_link)
ui.khonline_link.setOpenExternalLinks(True)
ui.nutzerverwaltung_link.setText(nutzerverwaltung_link)
ui.nutzerverwaltung_link.setOpenExternalLinks(True)

ui.kursivschrift.toggle()
ui.unterstreichen.toggle()
ui.fettschrift.toggle()
ui.rot.toggle()
ui.gruen.toggle()

ui.kursivschrift.setChecked(False)
ui.unterstreichen.setChecked(False)
ui.fettschrift.setChecked(False)
ui.rot.setChecked(False)
ui.gruen.setChecked(False)

ui.speichern_button.clicked.connect(infotext_speichern)
ui.kursivschrift.clicked.connect(infotext_kursiv)
ui.unterstreichen.clicked.connect(infotext_unterstreichen)
ui.fettschrift.clicked.connect(infotext_fett)
ui.rot.clicked.connect(infotext_rot)
ui.gruen.clicked.connect(infotext_gruen)
ui.normal.clicked.connect(infotext_normal)
ui.rot.setStyleSheet('QPushButton {color: red;}')
ui.gruen.setStyleSheet('QPushButton {color: green;}')

ui.kliniken.activated.connect(klinik_auswahl)
ui.stationsauswahl.clicked.connect(stationen_auswahl)
ui.datum.clicked.connect(infotext_datum)
ui.beenden_button.clicked.connect(beenden)
ui.drucken_button.clicked.connect(drucken)

ui.modus_bestellhistorie.clicked.connect(modus_bestellhistorie)
ui.modus_bestellhistorie_alle.clicked.connect(modus_bestellhistorie_alle)
ui.modus_infotexte.clicked.connect(modus_infotexte)
ui.modus_freitext.clicked.connect(modus_freitext)

ui.infotext.setStyleSheet("background-color:white")

klinik_dic = kliniken_einlesen()

ui.kliniken.addItems(list(klinik_dic.keys()))

ui.infotext.setFont(QtGui.QFont('Arial', 12))
ui.infotext.setFontPointSize(12)

# Default-Font für gesamte Application setzen
font = QtGui.QFont("Arial", 14)
app.setFont(font)

window.show()

sys.exit(app.exec())

