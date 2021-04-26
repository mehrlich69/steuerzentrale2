# set_up File für cx_freeze
# Erzeugt eine aus Python-Files EXE-Files. Muss auf der Zielplattform ausgeführt werden
# (z.B. eine Windows 10 Installation in einer VM)
# hier verwendet um steuerzentrale2.py in steuerzentrale2.exe zu überführen
# Wichtig ist der Eintrag base = "Win32GUI", dadurch wird verhindert, dass zusätzlich ein Konsolenfenster erscheint.
# Aufruf auf dem Zielrechner: python setup.py build
# Die erzeugten Dateienfinden sich dann im Unterordner "build"



import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "sys"]}

# GUI applications require a different base on Windows (the default is for a
# console application).

base = "Win32GUI"

setup(  name = "steuerzentrale2",
        version = "0.6",
        description = "Steuerzentrale KH-Online 2",
        options = {"build_exe": build_exe_options},
        executables = [Executable("steuerzentrale2.py", base=base)])