# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import rc_resources

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(825, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginForm.sizePolicy().hasHeightForWidth())
        LoginForm.setSizePolicy(sizePolicy)
        LoginForm.setMouseTracking(True)
        icon = QIcon()
        icon.addFile(u":/new/icons/Pollock-Icons2-FillRates.png", QSize(), QIcon.Normal, QIcon.Off)
        LoginForm.setWindowIcon(icon)
        LoginForm.setAutoFillBackground(False)
        LoginForm.setStyleSheet(u"QFrame#Border{\n"
"	border:2px solid green;\n"
"	border-radius:20px;\n"
"background:url(:/aDF4vy.jpg);\n"
"}\n"
"\n"
"QLabel#LoginLabel{\n"
"	color:white;\n"
"	font-family:Elephant;\n"
"	font-weight:bold;\n"
"	\n"
"}\n"
"\n"
"QLineEdit#UsernameValue{\n"
"	height:40px;\n"
"border-radius:20px;\n"
"padding:6px;\n"
"border:2px solid green;\n"
"}\n"
"\n"
"QLineEdit#PasswordValue{\n"
"	height:40px;\n"
"border-radius:20px;\n"
"padding:6px;\n"
"border:2px solid green;\n"
"}\n"
"\n"
"QPushButton#LoginBtn{\n"
"	border-radius:20px;\n"
"background-color:green;\n"
"height:40px;\n"
"font-weight:bold;\n"
"font-size:20px;\n"
"}\n"
"\n"
"QPushButton#LoginBtn:hover{\n"
"	border-radius:20px;\n"
"background-color:#7ef542;\n"
"height:40px;\n"
"font-weight:bold;\n"
"font-size:20px;\n"
"}")
        self.verticalLayout = QVBoxLayout(LoginForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Border = QFrame(LoginForm)
        self.Border.setObjectName(u"Border")
        self.Border.setFrameShape(QFrame.StyledPanel)
        self.Border.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Border)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.LoginLabel_2 = QLabel(self.Border)
        self.LoginLabel_2.setObjectName(u"LoginLabel_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LoginLabel_2.sizePolicy().hasHeightForWidth())
        self.LoginLabel_2.setSizePolicy(sizePolicy1)
        self.LoginLabel_2.setMinimumSize(QSize(50, 50))
        self.LoginLabel_2.setMaximumSize(QSize(50, 50))
        self.LoginLabel_2.setPixmap(QPixmap(u":/ico"))
        self.LoginLabel_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.LoginLabel_2)

        self.LoginLabel = QLabel(self.Border)
        self.LoginLabel.setObjectName(u"LoginLabel")
        sizePolicy.setHeightForWidth(self.LoginLabel.sizePolicy().hasHeightForWidth())
        self.LoginLabel.setSizePolicy(sizePolicy)
        self.LoginLabel.setScaledContents(True)
        self.LoginLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.LoginLabel.setIndent(0)

        self.horizontalLayout_2.addWidget(self.LoginLabel)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_5.setContentsMargins(20, 10, 60, 10)
        self.label = QLabel(self.Border)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.UsernameLabel = QLabel(self.Border)
        self.UsernameLabel.setObjectName(u"UsernameLabel")
        sizePolicy.setHeightForWidth(self.UsernameLabel.sizePolicy().hasHeightForWidth())
        self.UsernameLabel.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.UsernameLabel)

        self.UsernameValue = QLineEdit(self.Border)
        self.UsernameValue.setObjectName(u"UsernameValue")

        self.verticalLayout_5.addWidget(self.UsernameValue)

        self.PasswordLabel = QLabel(self.Border)
        self.PasswordLabel.setObjectName(u"PasswordLabel")
        sizePolicy.setHeightForWidth(self.PasswordLabel.sizePolicy().hasHeightForWidth())
        self.PasswordLabel.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.PasswordLabel)

        self.PasswordValue = QLineEdit(self.Border)
        self.PasswordValue.setObjectName(u"PasswordValue")
        self.PasswordValue.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.PasswordValue.setInputMask(u"")
        self.PasswordValue.setEchoMode(QLineEdit.Password)
        self.PasswordValue.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.PasswordValue)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.LoginBtn = QPushButton(self.Border)
        self.LoginBtn.setObjectName(u"LoginBtn")

        self.verticalLayout_5.addWidget(self.LoginBtn)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.ImgView = QLabel(self.Border)
        self.ImgView.setObjectName(u"ImgView")
        self.ImgView.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ImgView.sizePolicy().hasHeightForWidth())
        self.ImgView.setSizePolicy(sizePolicy)
        self.ImgView.setMinimumSize(QSize(350, 400))
        self.ImgView.setMaximumSize(QSize(350, 400))
        self.ImgView.setPixmap(QPixmap(u":/ico"))
        self.ImgView.setScaledContents(True)
        self.ImgView.setAlignment(Qt.AlignCenter)
        self.ImgView.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.ImgView)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.Border)


        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Login | Inventory Managment Sysytem", None))
        self.LoginLabel_2.setText("")
        self.LoginLabel.setText(QCoreApplication.translate("LoginForm", u"Log In | BTech Inventory Managment System", None))
        self.label.setText(QCoreApplication.translate("LoginForm", u"Company NAme", None))
        self.UsernameLabel.setText(QCoreApplication.translate("LoginForm", u"UserName", None))
        self.UsernameValue.setPlaceholderText(QCoreApplication.translate("LoginForm", u"Username", None))
        self.PasswordLabel.setText(QCoreApplication.translate("LoginForm", u"Password", None))
        self.PasswordValue.setText("")
        self.PasswordValue.setPlaceholderText(QCoreApplication.translate("LoginForm", u"Password", None))
        self.LoginBtn.setText(QCoreApplication.translate("LoginForm", u"Log In", None))
        self.ImgView.setText("")
    # retranslateUi

