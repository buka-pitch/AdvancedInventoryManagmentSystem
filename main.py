# This Python file uses the following encoding: utf-8
"""main entry module of the application"""

import os
import sys

from PySide6.QtWidgets import QApplication, QWidget

from Login import Login


app = QApplication(sys.argv)
widget = Login()
widget.show()
sys.exit(app.exec())
