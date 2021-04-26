# Wandelt die XML-Designbeschreibungen des Qt5 Creators in Python um
# z.B. form.ui -> form.py
# form.py kann dann mittels import in das Hauptprogramm eingebunden werden.
# Dieses Script muss immer ausgeführt werden, wenn an der GUI im Qt5 Creator etwas geändert wurde.


from PyQt5 import uic

uic.compileUiDir("/Users/markusehrlich/Python-Entwicklung/PyQt/Steuerzentrale2/ui")
#uic.compileUiDir("Pi_Temp_Monitor")
#uic.compileUiDir("Pi_Temp_Monitor_SmallDisplay")
