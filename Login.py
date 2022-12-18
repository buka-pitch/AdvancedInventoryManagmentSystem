# This Python file uses the following encoding: utf-8
"""Login class of the application"""
#import os
from pathlib import Path

#from PySide6 import QtCore
from PySide6 import QtWidgets


from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets
import icons


class Login(QtWidgets.QWidget):
    """class containing the login logic and widget

    Args:
        QtWidgets (QtWidget): A window Widget for the login
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()
        self.img = self.findChild(QtWidgets.QLabel,"ImgView")
        self.username = self.findChild(QtWidgets.QLineEdit, "UsernameValue")
        self.password = self.findChild(QtWidgets.QLineEdit, "PasswordValue")
        self.loginBtn = self.findChild(QtWidgets.QPushButton, "LoginBtn")

        # signal connected for temporary printing functionality
        self.loginBtn.clicked.connect(lambda: print(f"{self.username.text()} {self.password.text()}"))

    def load_ui(self):
        """loading the ui for the parrent
        """
        loader = QUiLoader()
        path = Path(__file__).resolve().parent / "login.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()
        


#TODO Add a logining in logic
