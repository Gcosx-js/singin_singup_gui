from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets


class SingUp_UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1363, 816)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, -7, 1491, 831))
        self.label.setStyleSheet("image: url(:/newPrefix/login_bg.png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/login_bg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.singup_username_lineedit = QtWidgets.QLineEdit(Form)
        self.singup_username_lineedit.setGeometry(QtCore.QRect(770, 210, 511, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.singup_username_lineedit.setFont(font)
        self.singup_username_lineedit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.singup_username_lineedit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.singup_username_lineedit.setStyleSheet("QLineEdit{\n"
"    border: 2px solid gray;\n"
"    border-radius: 28px;\n"
"    color: rgb(88, 88, 88);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 3px solid green;\n"
"    border-radius: 28px;\n"
"    color: rgb(88, 88, 88);\n"
"    \n"
"}")
        self.singup_username_lineedit.setText("")
        self.singup_username_lineedit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.singup_username_lineedit.setObjectName("singup_username_lineedit")
        self.username_label = QtWidgets.QLabel(Form)
        self.username_label.setGeometry(QtCore.QRect(770, 150, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color: rgb(139, 139, 139);")
        self.username_label.setObjectName("username_label")
        self.email_label = QtWidgets.QLabel(Form)
        self.email_label.setGeometry(QtCore.QRect(770, 300, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("color: rgb(139, 139, 139);")
        self.email_label.setObjectName("email_label")
        self.singup_email_lineedit = QtWidgets.QLineEdit(Form)
        self.singup_email_lineedit.setGeometry(QtCore.QRect(770, 360, 511, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.singup_email_lineedit.setFont(font)
        self.singup_email_lineedit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.singup_email_lineedit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.singup_email_lineedit.setStyleSheet("QLineEdit{\n"
"    border: 2px solid gray;\n"
"    border-radius: 28px;\n"
"    color: rgb(88, 88, 88);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 3px solid green;\n"
"    border-radius: 28px;\n"
"    color: rgb(88, 88, 88);\n"
"}")
        self.singup_email_lineedit.setText("")
        self.singup_email_lineedit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.singup_email_lineedit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.singup_email_lineedit.setObjectName("singup_email_lineedit")
        self.login_title_label = QtWidgets.QLabel(Form)
        self.login_title_label.setGeometry(QtCore.QRect(60, 50, 445, 111))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(48)
        self.login_title_label.setFont(font)
        self.login_title_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.login_title_label.setObjectName("login_title_label")
        self.have_an_acc_label = QtWidgets.QLabel(Form)
        self.have_an_acc_label.setGeometry(QtCore.QRect(60, 180, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(22)
        self.have_an_acc_label.setFont(font)
        self.have_an_acc_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.have_an_acc_label.setWordWrap(True)
        self.have_an_acc_label.setObjectName("have_an_acc_label")
        self.singin_pushbutton = QtWidgets.QPushButton(Form)
        self.singin_pushbutton.setGeometry(QtCore.QRect(50, 300, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.singin_pushbutton.setFont(font)
        self.singin_pushbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.singin_pushbutton.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    border:2px solid white;\n"
"    border-radius:33px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:transparent;\n"
"    border:2px solid black;\n"
"    border-radius:33px;\n"
"    \n"
"    color:white;\n"
"}\n"
"")
        self.singin_pushbutton.setObjectName("singin_pushbutton")
        self.singup_pushbutton = QtWidgets.QPushButton(Form)
        self.singup_pushbutton.setGeometry(QtCore.QRect(830, 730, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.singup_pushbutton.setFont(font)
        self.singup_pushbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.singup_pushbutton.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    border:3px solid green;\n"
"    border-radius:33px;\n"
"    color: green;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:transparent;\n"
"    border:3px solid black;\n"
"    border-radius:33px;\n"
"    color:green;\n"
"}\n"
"")
        self.singup_pushbutton.setObjectName("singup_pushbutton")
        self.singup_password_lineedit = QtWidgets.QLineEdit(Form)
        self.singup_password_lineedit.setGeometry(QtCore.QRect(770, 510, 511, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.singup_password_lineedit.setFont(font)
        self.singup_password_lineedit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.singup_password_lineedit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.singup_password_lineedit.setStyleSheet("QLineEdit{\n"
"    border: 2px solid gray;\n"
"    border-radius: 28px;\n"
"    color: rgb(88, 88, 88);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 3px solid green;\n"
"    border-radius: 28px;\n"
"    color: rgb(88, 88, 88);\n"
"}")
        self.singup_password_lineedit.setText("")
        self.singup_password_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.singup_password_lineedit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.singup_password_lineedit.setObjectName("singup_password_lineedit")
        self.password_label = QtWidgets.QLabel(Form)
        self.password_label.setGeometry(QtCore.QRect(770, 450, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("color: rgb(139, 139, 139);")
        self.password_label.setObjectName("password_label")
        self.singup_confirm_pass_lineedit = QtWidgets.QLineEdit(Form)
        self.singup_confirm_pass_lineedit.setGeometry(QtCore.QRect(770, 650, 511, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.singup_confirm_pass_lineedit.setFont(font)
        self.singup_confirm_pass_lineedit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.singup_confirm_pass_lineedit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.singup_confirm_pass_lineedit.setStyleSheet("QLineEdit{\n"
"    border: 2px solid gray;\n"
"    border-radius: 28px;\n"
"    color: rgb(88, 88, 88);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 3px solid green;\n"
"    border-radius: 28px;\n"
"    color: rgb(88, 88, 88);\n"
"}")
        self.singup_confirm_pass_lineedit.setText("")
        self.singup_confirm_pass_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.singup_confirm_pass_lineedit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.singup_confirm_pass_lineedit.setObjectName("singup_confirm_pass_lineedit")
        self.confirm_password_label = QtWidgets.QLabel(Form)
        self.confirm_password_label.setGeometry(QtCore.QRect(770, 590, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.confirm_password_label.setFont(font)
        self.confirm_password_label.setStyleSheet("color: rgb(139, 139, 139);")
        self.confirm_password_label.setObjectName("confirm_password_label")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(830, 40, 351, 80))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.register_title_label = QtWidgets.QLabel(self.groupBox)
        self.register_title_label.setGeometry(QtCore.QRect(30, -10, 301, 101))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(33)
        self.register_title_label.setFont(font)
        self.register_title_label.setStyleSheet("color: black;")
        self.register_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.register_title_label.setObjectName("register_title_label")
        self.settings_button = QtWidgets.QPushButton(Form)
        self.settings_button.setGeometry(QtCore.QRect(20, 640, 71, 71))
        self.settings_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_button.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    image: url(:/newPrefix/pngwing.com.png);\n"
"}\n"
"")
        self.settings_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/pngwing.com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/pngwing.com.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.settings_button.setIcon(icon)
        self.settings_button.setIconSize(QtCore.QSize(400, 70))
        self.settings_button.setObjectName("settings_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.username_label.setText(_translate("Form", "Username"))
        self.email_label.setText(_translate("Form", "Email address"))
        self.login_title_label.setText(_translate("Form", "Login"))
        self.have_an_acc_label.setText(_translate("Form", "Already have an account?"))
        self.singin_pushbutton.setText(_translate("Form", "Sing In"))
        self.singup_pushbutton.setText(_translate("Form", "Sing Up"))
        self.password_label.setText(_translate("Form", "Password"))
        self.confirm_password_label.setText(_translate("Form", "Confirm password"))
        self.register_title_label.setText(_translate("Form", "Register"))
import images



class Settings_UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(373, 453)
        self.openGLWidget = QtWidgets.QOpenGLWidget(Form)
        self.openGLWidget.setGeometry(QtCore.QRect(-110, -30, 611, 571))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        self.openGLWidget.setFont(font)
        self.openGLWidget.setStyleSheet("")
        self.openGLWidget.setObjectName("openGLWidget")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(-40, 250, 421, 181))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(130, 90, 181, 71))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.mod_slider = QtWidgets.QSlider(self.groupBox)
        self.mod_slider.setGeometry(QtCore.QRect(10, 10, 160, 50))
        self.mod_slider.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.mod_slider.setStyleSheet("QSlider {\n"
"    min-height: 50px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 black, stop:1 black);\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 black, stop:1 yellow);\n"
"    border: 1px solid #777;\n"
"    width: 50px;\n"
"    margin: -25px 0;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:checked {\n"
"    background: yellow;\n"
"}\n"
"")
        self.mod_slider.setMaximum(1)
        self.mod_slider.setOrientation(QtCore.Qt.Horizontal)
        self.mod_slider.setTickInterval(1)
        self.mod_slider.setObjectName("mod_slider")
        self.mod_info_label = QtWidgets.QLabel(self.groupBox_2)
        self.mod_info_label.setGeometry(QtCore.QRect(130, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Nova")
        font.setPointSize(26)
        self.mod_info_label.setFont(font)
        self.mod_info_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.mod_info_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.mod_info_label.setObjectName("mod_info_label")
        self.az_dili_radiobutton = QtWidgets.QRadioButton(Form)
        self.az_dili_radiobutton.setGeometry(QtCore.QRect(90, 30, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(18)
        self.az_dili_radiobutton.setFont(font)
        self.az_dili_radiobutton.setStyleSheet("color: rgb(255, 255, 255);")
        self.az_dili_radiobutton.setObjectName("az_dili_radiobutton")
        self.ingilis_dili_radiobutton = QtWidgets.QRadioButton(Form)
        self.ingilis_dili_radiobutton.setGeometry(QtCore.QRect(90, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(18)
        self.ingilis_dili_radiobutton.setFont(font)
        self.ingilis_dili_radiobutton.setStyleSheet("color: rgb(255, 255, 255);")
        self.ingilis_dili_radiobutton.setObjectName("ingilis_dili_radiobutton")
        self.rusdili_radiobutton = QtWidgets.QRadioButton(Form)
        self.rusdili_radiobutton.setGeometry(QtCore.QRect(90, 170, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(18)
        self.rusdili_radiobutton.setFont(font)
        self.rusdili_radiobutton.setStyleSheet("color: rgb(255, 255, 255);")
        self.rusdili_radiobutton.setObjectName("rusdili_radiobutton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.mod_info_label.setText(_translate("Form", "Light mod"))
        self.az_dili_radiobutton.setText(_translate("Form", "Azərbaycan"))
        self.ingilis_dili_radiobutton.setText(_translate("Form", "English"))
        self.rusdili_radiobutton.setText(_translate("Form", "Pусский"))


    

class SingIn_UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1363, 816)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, -7, 1491, 831))
        self.label.setStyleSheet("image: url(:/newPrefix/login_bg.png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/login_bg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.login_username_lineedit = QtWidgets.QLineEdit(Form)
        self.login_username_lineedit.setGeometry(QtCore.QRect(770, 270, 511, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.login_username_lineedit.setFont(font)
        self.login_username_lineedit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.login_username_lineedit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_username_lineedit.setStyleSheet("QLineEdit{\n"
"    border: 2px solid gray;\n"
"    border-radius: 28px;\n"
"    color: rgb(88, 88, 88);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 3px solid green;\n"
"    border-radius: 28px;\n"
"    color: rgb(88, 88, 88);\n"
"    \n"
"}")
        self.login_username_lineedit.setText("")
        self.login_username_lineedit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.login_username_lineedit.setObjectName("login_username_lineedit")
        self.login_label = QtWidgets.QLabel(Form)
        self.login_label.setGeometry(QtCore.QRect(770, 90, 331, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(33)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("color: rgb(93, 93, 93);")
        self.login_label.setObjectName("login_label")
        self.username_label = QtWidgets.QLabel(Form)
        self.username_label.setGeometry(QtCore.QRect(770, 210, 591, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color: rgb(139, 139, 139);")
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(Form)
        self.password_label.setGeometry(QtCore.QRect(770, 360, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("color: rgb(139, 139, 139);")
        self.password_label.setObjectName("password_label")
        self.login_sifre_lineedit = QtWidgets.QLineEdit(Form)
        self.login_sifre_lineedit.setGeometry(QtCore.QRect(770, 420, 511, 71))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(22)
        self.login_sifre_lineedit.setFont(font)
        self.login_sifre_lineedit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.login_sifre_lineedit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_sifre_lineedit.setStyleSheet("QLineEdit{\n"
"    border: 2px solid gray;\n"
"    border-radius: 28px;\n"
"    color: rgb(88, 88, 88);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 3px solid green;\n"
"    border-radius: 28px;\n"
"    color: rgb(88, 88, 88);\n"
"}")
        self.login_sifre_lineedit.setText("")
        self.login_sifre_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_sifre_lineedit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.login_sifre_lineedit.setObjectName("login_sifre_lineedit")
        self.welcome_label = QtWidgets.QLabel(Form)
        self.welcome_label.setGeometry(QtCore.QRect(60, 50, 581, 111))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(48)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.welcome_label.setObjectName("welcome_label")
        self.crt_y_acc_label = QtWidgets.QLabel(Form)
        self.crt_y_acc_label.setGeometry(QtCore.QRect(70, 160, 351, 121))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(22)
        self.crt_y_acc_label.setFont(font)
        self.crt_y_acc_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.crt_y_acc_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.crt_y_acc_label.setWordWrap(True)
        self.crt_y_acc_label.setObjectName("crt_y_acc_label")
        self.singup_pushbutton = QtWidgets.QPushButton(Form)
        self.singup_pushbutton.setGeometry(QtCore.QRect(60, 300, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.singup_pushbutton.setFont(font)
        self.singup_pushbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.singup_pushbutton.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    border:2px solid white;\n"
"    border-radius:33px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:transparent;\n"
"    border:2px solid black;\n"
"    border-radius:33px;\n"
"    \n"
"    color:white;\n"
"}\n"
"")
        self.singup_pushbutton.setObjectName("singup_pushbutton")
        self.sing_in_pushbutton = QtWidgets.QPushButton(Form)
        self.sing_in_pushbutton.setGeometry(QtCore.QRect(770, 530, 511, 71))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.sing_in_pushbutton.setFont(font)
        self.sing_in_pushbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sing_in_pushbutton.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    border:3px solid green;\n"
"    border-radius:33px;\n"
"    color: green;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:transparent;\n"
"    border:3px solid black;\n"
"    border-radius:33px;\n"
"    color:green;\n"
"}\n"
"")
        self.sing_in_pushbutton.setObjectName("sing_in_pushbutton")
        self.forgot_pushbutton = QtWidgets.QPushButton(Form)
        self.forgot_pushbutton.setGeometry(QtCore.QRect(780, 630, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.forgot_pushbutton.setFont(font)
        self.forgot_pushbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgot_pushbutton.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    color:green;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:transparent;\n"
"    color:red;\n"
"}")
        self.forgot_pushbutton.setObjectName("forgot_pushbutton")
        self.settings_button = QtWidgets.QPushButton(Form)
        self.settings_button.setGeometry(QtCore.QRect(20, 640, 71, 71))
        self.settings_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_button.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    image: url(:/newPrefix/pngwing.com.png);\n"
"}\n"
"")
        self.settings_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/pngwing.com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/pngwing.com.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.settings_button.setIcon(icon)
        self.settings_button.setIconSize(QtCore.QSize(400, 70))
        self.settings_button.setObjectName("settings_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.login_label.setText(_translate("Form", "Login"))
        self.username_label.setText(_translate("Form", "Username/Email address"))
        self.password_label.setText(_translate("Form", "Password"))
        self.welcome_label.setText(_translate("Form", "Welcome!"))
        self.crt_y_acc_label.setText(_translate("Form", "Create your account. For Free!"))
        self.singup_pushbutton.setText(_translate("Form", "Start!"))
        self.sing_in_pushbutton.setText(_translate("Form", "Sing In"))
        self.forgot_pushbutton.setText(_translate("Form", "Forgot password?"))
import images

#python -m PyQt5.uic.pyuic -x dosya_adi.ui -o python_adi.py
import sys
from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import re


class Singin_page(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.singin_page = SingIn_UI()
        self.singin_page.setupUi(self)
        self.singin_page.settings_button.clicked.connect(self.settings_ac)
        self.settings_page = Settings_page()
        self.settings_page.dil_deyis.connect(self.cevir)
        self.singin_page.singup_pushbutton.clicked.connect(self.switch_window)
        self.settings_page.mod_deyis_signal.connect(self.mod_deyisme)
        try:
            with open('config.data','r') as file:
                data = file.read()
                matches = re.findall(r'mode:(\w+)', data)
                mode_data = [str(i) for i in matches][0]
                matches = re.findall(r'lang:(\w+)',data)
                lang_data = [str(i) for i in matches][0]
                if mode_data=='l':
                    self.mod_deyisme(2)
                elif mode_data=='d':
                    self.mod_deyisme(1)
                if lang_data=='az':
                    self.cevir(1)
                elif lang_data=='eng':
                    self.cevir(2)
                elif lang_data=='ru':
                    self.cevir(3)
        except FileNotFoundError:
            self.file_not_found()
        except IOError as e:
            #print(e)
            self.io_error()
        def file_not_found(self):
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Warning)
                message_box.setWindowTitle("config.data Not Found")
                message_box.setText("The specified file or directory could not be found. Please check the file path and ensure that the file exists. Verify that you have the necessary permissions to access the file or directory. This error typically occurs when attempting to perform file operations on a non-existent or inaccessible file or directory. Double-check the file path and try again.")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.exec_()
                sys.exit(app.exec_())
        def io_error(self):
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Warning)
                message_box.setWindowTitle("config.data IO Error")
                message_box.setText("An Input/Output (IO) error occurred during the execution of the Python program. This error usually indicates issues related to file operations, network connections, or other input/output processes. Possible reasons for this error include file not found, permission issues, connection problems, or hardware failures.")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.exec_()
                sys.exit(app.exec_())
    def switch_window(self):
        singup_pencere = SingUp_page()
        self.window().setCentralWidget(singup_pencere)

    def showEvent(self, event):
        self.show()
        self.window().setCentralWidget(self)
    
    def darka_kec(self):
            self.singin_page.label.setPixmap(QtGui.QPixmap(":/dark/dark_bg.png"))
            self.singin_page.label.setScaledContents(True)
            self.singin_page.username_label.setStyleSheet('color:black;')
            self.singin_page.password_label.setStyleSheet('color:black;')
            self.settings_page.settings_page.mod_slider.setValue(1)
            self.singin_page.login_username_lineedit.setStyleSheet('''
            QLineEdit{
	border: 2px solid black;
	border-radius: 28px;
	color: rgb(88, 88, 88);
}
QLineEdit:focus{
	border: 3px solid green;
	border-radius: 28px;
	color: rgb(88, 88, 88);
	
}''')
            self.singin_page.login_sifre_lineedit.setStyleSheet('''
                                                                
            QLineEdit{
	border: 2px solid black;
	border-radius: 28px;
	color: rgb(88, 88, 88);
}
QLineEdit:focus{
	border: 3px solid green;
	border-radius: 28px;
	color: rgb(88, 88, 88);
	
}                                                    ''')
            self.singin_page.sing_in_pushbutton.setStyleSheet('''
            QPushButton{
	background:transparent;
	border:3px solid black;
	border-radius:33px;
	color: black;
}
QPushButton:pressed{
	background:black;
	border:3px solid green;
	border-radius:33px;
	color:white;
}
                                                  ''')
            self.settings_page.settings_page.mod_info_label.setText('Dark')
            self.singin_page.forgot_pushbutton.setStyleSheet('''
            QPushButton{
	background:transparent;
	color:black;
}
QPushButton:pressed{
	background:transparent;
	color:red;
}                                                 ''')
    
    def light_kec(self):
            self.singin_page.label.setPixmap(QtGui.QPixmap(":/newPrefix/login_bg.png"))
            self.settings_page.settings_page.mod_info_label.setText('Light')
            self.singin_page.username_label.setStyleSheet('color: rgb(139, 139, 139);')
            self.singin_page.password_label.setStyleSheet('color: rgb(139, 139, 139);')
            self.settings_page.settings_page.mod_slider.setValue(0)
            self.singin_page.forgot_pushbutton.setStyleSheet('''
            QPushButton{
	background:transparent;
	color:green;
}
QPushButton:pressed{
	background:transparent;
	color:red;
}                                                 ''')
            self.singin_page.sing_in_pushbutton.setStyleSheet('''
            QPushButton{
	background:transparent;
	border:3px solid green;
	border-radius:33px;
	color: green;
}
QPushButton:pressed{
	background:transparent;
	border:3px solid black;
	border-radius:33px;
	color:green;
}
                                                  ''')
            self.singin_page.login_username_lineedit.setStyleSheet('''
            QLineEdit{
	border: 2px solid gray;
	border-radius: 28px;
	color: rgb(88, 88, 88);
}
QLineEdit:focus{
	border: 3px solid green;
	border-radius: 28px;
	color: rgb(88, 88, 88);
	
}                                                       ''')
            self.singin_page.login_sifre_lineedit.setStyleSheet('''
            QLineEdit{
	border: 2px solid gray;
	border-radius: 28px;
	color: rgb(88, 88, 88);
}
QLineEdit:focus{
	border: 3px solid green;
	border-radius: 28px;
	color: rgb(88, 88, 88);
	
}                                                    ''')
    
    def settings_ac(self):
        self.settings_page.show()
    
    def mod_deyisme(self,i):
        try:
            if i==1:
                self.darka_kec()
                with open('config.data', 'r+') as file:
                    data = file.read()
                    updated_data = re.sub(r'mode:(\w+)', r'mode:d', data)
                    file.seek(0)
                    file.write(updated_data)
                    file.truncate()
            elif i==0: 
                self.light_kec()
                with open('config.data', 'r+') as file:
                    data = file.read()
                    updated_data = re.sub(r'mode:(\w+)', r'mode:l', data)
                    file.seek(0)
                    file.write(updated_data)
                    file.truncate()
                
        except FileNotFoundError:
            self.file_not_found()
        except IOError as e:
            #print(e)
            self.io_error()
    
    def cevir(self,i):
        # 1- az dili 
        # 2- ingilis dili 
        # 3- rus dili
        if i==1:
            self.singin_page.forgot_pushbutton.setText("Şifrəni unutdun?")
            self.singin_page.welcome_label.setText('Xoş gəlmisiniz!')
            self.singin_page.username_label.setText('İstifadəçi adı/Email adres')
            self.singin_page.password_label.setText('Şifrə')
            self.singin_page.crt_y_acc_label.setText('Hesabınız yoxdur? Elə indi yarat!') 
            self.singin_page.sing_in_pushbutton.setText('Daxil ol')
            self.singin_page.singup_pushbutton.setText('Başla!')
            self.singin_page.login_label.setText('Giriş et')
            
            with open('config.data', 'r+') as file:
                data = file.read()
                updated_data = re.sub(r'lang:(\w+)', r'lang:az', data)
                file.seek(0)
                file.write(updated_data)
                file.truncate()
                
                    
        elif i==2:
            self.singin_page.forgot_pushbutton.setText("Forgot password?")
            self.singin_page.welcome_label.setText('Welcome!')
            self.singin_page.username_label.setText('Username/Email address')
            self.singin_page.password_label.setText('Password')
            self.singin_page.crt_y_acc_label.setText('Create your account. For Free!') 
            self.singin_page.sing_in_pushbutton.setText('Sing In')
            self.singin_page.singup_pushbutton.setText('Start!')
            self.singin_page.login_label.setText('Login')
            with open('config.data', 'r+') as file:
                data = file.read()
                updated_data = re.sub(r'lang:(\w+)', r'lang:eng', data)
                file.seek(0)
                file.write(updated_data)
                file.truncate()
            
        elif i==3:
            self.singin_page.forgot_pushbutton.setText("Забыли пароль?")
            self.singin_page.welcome_label.setText('Добро пожаловать!')
            font = self.singin_page.welcome_label.font()
            font.setPointSize(37)
            self.singin_page.welcome_label.setFont(font)
            self.singin_page.username_label.setText('Имя пользователя/э. адрес')
            self.singin_page.password_label.setText('Пароль')
            self.singin_page.crt_y_acc_label.setText('Завести аккаунт. Бесплатно!') 
            self.singin_page.sing_in_pushbutton.setText('Войти')
            self.singin_page.singup_pushbutton.setText('Начинать!')
            self.singin_page.login_label.setText('Авторизоваться')
            with open('config.data', 'r+') as file:
                data = file.read()
                updated_data = re.sub(r'lang:(\w+)', r'lang:ru', data)
                file.seek(0)
                file.write(updated_data)
                file.truncate()

        
class Settings_page(QWidget):
    dil_deyis = pyqtSignal(int)
    mod_deyis_signal = pyqtSignal(int)
    def __init__(self) -> None:
        super().__init__()
        self.settings_page = Settings_UI()
        self.settings_page.setupUi(self)
        self.settings_page.az_dili_radiobutton.clicked.connect(lambda: self.gonder(1))
        self.settings_page.ingilis_dili_radiobutton.clicked.connect(lambda: self.gonder(2))
        self.settings_page.rusdili_radiobutton.clicked.connect(lambda: self.gonder(3))
        self.settings_page.mod_slider.valueChanged.connect(self.mod_deyis)
    
    def gonder(self,i):
        self.dil_deyis.emit(i)
    def mod_deyis(self):
        self.mod_deyis_signal.emit(int(self.settings_page.mod_slider.value()))
        
class SingUp_page(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.singup_page = SingUp_UI()
        self.singup_page.setupUi(self)
        self.singup_page.singin_pushbutton.clicked.connect(self.switch_window)
        self.singup_page.settings_button.clicked.connect(self.settings_ac)
        self.settingsd_page = Settings_page()
        self.settingsd_page.dil_deyis.connect(self.cevir)
        self.settingsd_page.mod_deyis_signal.connect(self.mod_deyisme)
    
        try:
            with open('config.data','r') as file:
                data = file.read()
                matches = re.findall(r'mode:(\w+)', data)
                mode_data = [str(i) for i in matches][0]
                matches = re.findall(r'lang:(\w+)',data)
                lang_data = [str(i) for i in matches][0]
                if mode_data=='l':
                    self.mod_deyisme(2)
                elif mode_data=='d':
                    self.mod_deyisme(1)
                if lang_data=='az':
                    self.cevir(1)
                elif lang_data=='eng':
                    self.cevir(2)
                elif lang_data=='ru':
                    self.cevir(3)
        except FileNotFoundError:
            self.file_not_found()
        except IOError as e:
            self.io_error()
            
    def file_not_found(self):
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Warning)
                message_box.setWindowTitle("config.data Not Found")
                message_box.setText("The specified file or directory could not be found. Please check the file path and ensure that the file exists. Verify that you have the necessary permissions to access the file or directory. This error typically occurs when attempting to perform file operations on a non-existent or inaccessible file or directory. Double-check the file path and try again.")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.exec_()
                sys.exit(app.exec_())
    def io_error(self):
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Warning)
                message_box.setWindowTitle("config.data IO Error")
                message_box.setText("An Input/Output (IO) error occurred during the execution of the Python program. This error usually indicates issues related to file operations, network connections, or other input/output processes. Possible reasons for this error include file not found, permission issues, connection problems, or hardware failures.")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.exec_()
                sys.exit(app.exec_())
    
    def darka_kec(self):
        self.singup_page.label.setPixmap(QtGui.QPixmap(":/dark/dark_bg.png"))
        self.singup_page.label.setScaledContents(True)
        self.singup_page.username_label.setStyleSheet('color:black;')
        self.singup_page.password_label.setStyleSheet('color:black;')
        self.singup_page.email_label.setStyleSheet('color:black;')
        self.singup_page.confirm_password_label.setStyleSheet('color:black;')
        self.singup_page.singup_pushbutton.setStyleSheet('''
        QPushButton{
	background:transparent;
	border:3px solid black;
	border-radius:33px;
	color: black;
}
QPushButton:pressed{
	background:black;
	border:3px solid green;
	border-radius:33px;
	color:white;
}
                                                  ''')
        self.singup_page.singup_confirm_pass_lineedit.setStyleSheet('''
        QLineEdit{
	border: 2px solid black;
	border-radius: 28px;
	color: rgb(88, 88, 88);
}
QLineEdit:focus{
	border: 3px solid green;
	border-radius: 28px;
	color: rgb(88, 88, 88);
	
}                                                             ''')
        self.singup_page.singup_email_lineedit.setStyleSheet('''
        QLineEdit{
	border: 2px solid black;
	border-radius: 28px;
	color: rgb(88, 88, 88);
}
QLineEdit:focus{
	border: 3px solid green;
	border-radius: 28px;
	color: rgb(88, 88, 88);
	
}                                                      ''')
        self.singup_page.singup_username_lineedit.setStyleSheet('''
        QLineEdit{
	border: 2px solid black;
	border-radius: 28px;
	color: rgb(88, 88, 88);
}
QLineEdit:focus{
	border: 3px solid green;
	border-radius: 28px;
	color: rgb(88, 88, 88);
	
}                                                      ''')
        self.singup_page.singup_password_lineedit.setStyleSheet('''
        QLineEdit{
	border: 2px solid black;
	border-radius: 28px;
	color: rgb(88, 88, 88);
}
QLineEdit:focus{
	border: 3px solid green;
	border-radius: 28px;
	color: rgb(88, 88, 88);
	
}                                                      ''')
    def light_kec(self):
        self.singup_page.label.setPixmap(QtGui.QPixmap(":/newPrefix/login_bg.png"))
        self.singup_page.label.setScaledContents(True)
        self.singup_page.username_label.setStyleSheet('color: rgb(139, 139, 139);')
        self.singup_page.password_label.setStyleSheet('color: rgb(139, 139, 139);')
        self.singup_page.email_label.setStyleSheet('color: rgb(139, 139, 139);')
        self.singup_page.confirm_password_label.setStyleSheet('color:rgb(139, 139, 139);')
        self.singup_page.singup_pushbutton.setStyleSheet('''
        QPushButton{
	background:transparent;
	border:3px solid green;
	border-radius:33px;
	color: green;
}
QPushButton:pressed{
	background:transparent;
	border:3px solid black;
	border-radius:33px;
	color:green;
}''')
        self.singup_page.singup_confirm_pass_lineedit.setStyleSheet('''
        QLineEdit{
	border: 2px solid gray;
	border-radius: 28px;
	color: rgb(88, 88, 88);
}
QLineEdit:focus{
	border: 3px solid green;
	border-radius: 28px;
	color: rgb(88, 88, 88);
	
}                                                             ''')
        self.singup_page.singup_email_lineedit.setStyleSheet('''
        QLineEdit{
	border: 2px solid gray;
	border-radius: 28px;
	color: rgb(88, 88, 88);
}
QLineEdit:focus{
	border: 3px solid green;
	border-radius: 28px;
	color: rgb(88, 88, 88);
	
}                                                      ''')
        self.singup_page.singup_username_lineedit.setStyleSheet('''
        QLineEdit{
	border: 2px solid gray;
	border-radius: 28px;
	color: rgb(88, 88, 88);
}
QLineEdit:focus{
	border: 3px solid green;
	border-radius: 28px;
	color: rgb(88, 88, 88);
	
}                                                      ''')
        self.singup_page.singup_password_lineedit.setStyleSheet('''
        QLineEdit{
	border: 2px solid gray;
	border-radius: 28px;
	color: rgb(88, 88, 88);
}
QLineEdit:focus{
	border: 3px solid green;
	border-radius: 28px;
	color: rgb(88, 88, 88);
	
}''')
    def mod_deyisme(self,i):
            if i==1:
                self.darka_kec()
                with open('config.data', 'r+') as file:
                    data = file.read()
                    updated_data = re.sub(r'mode:(\w+)', r'mode:d', data)
                    file.seek(0)
                    file.write(updated_data)
                    file.truncate()
            else:
                self.light_kec()
                with open('config.data', 'r+') as file:
                    data = file.read()
                    updated_data = re.sub(r'mode:(\w+)', r'mode:l', data)
                    file.seek(0)
                    file.write(updated_data)
                    file.truncate()
                
    def cevir(self,i):
        if i==1:
            self.singup_page.confirm_password_label.setText('Şifrəni təsdiqlə')
            self.singup_page.password_label.setText('Şifrə')
            self.singup_page.register_title_label.setText('Qeydiyyat')
            self.singup_page.login_title_label.setText('Giriş et')
            self.singup_page.singin_pushbutton.setText('Daxil ol')
            self.singup_page.have_an_acc_label.setText('Artıq bir hesabınız varmı?')
            self.singup_page.email_label.setText('Email adresi')
            self.singup_page.username_label.setText('İstifadəçi adı')
            self.singup_page.singup_pushbutton.setText('Qeydiyyatdan keç')
            with open('config.data', 'r+') as file:
                data = file.read()
                updated_data = re.sub(r'lang:(\w+)', r'lang:az', data)
                file.seek(0)
                file.write(updated_data)
                file.truncate()

        elif i==2:
            self.singup_page.confirm_password_label.setText('Confirm password')
            self.singup_page.password_label.setText('Password')
            self.singup_page.register_title_label.setText('Register')
            self.singup_page.login_title_label.setText('Login')
            self.singup_page.singin_pushbutton.setText('Sing In')
            self.singup_page.have_an_acc_label.setText('Already have an account?')
            self.singup_page.email_label.setText('Email address')
            self.singup_page.username_label.setText('Username')
            self.singup_page.singup_pushbutton.setText('Sing Up')
            with open('config.data', 'r+') as file:
                data = file.read()
                updated_data = re.sub(r'lang:(\w+)', r'lang:eng', data)
                file.seek(0)
                file.write(updated_data)
                file.truncate()

        elif i==3:
            self.singup_page.confirm_password_label.setText('Подтвердите пароль')
            self.singup_page.password_label.setText('Пароль')
            self.singup_page.register_title_label.setText('Pегистр')
            self.singup_page.login_title_label.setText('Авторизоваться')
            self.singup_page.singin_pushbutton.setText('Начать')
            self.singup_page.have_an_acc_label.setText('Уже есть аккаунт?')
            self.singup_page.email_label.setText('Электронная почта')
            self.singup_page.username_label.setText('Имя пользователя')
            self.singup_page.singup_pushbutton.setText('Заканчивать')
            with open('config.data', 'r+') as file:
                data = file.read()
                updated_data = re.sub(r'lang:(\w+)', r'lang:ru', data)
                file.seek(0)
                file.write(updated_data)
                file.truncate()

            
            
    
    def settings_ac(self):
        self.settingsd_page.show()

    def switch_window(self):
        window1 = Singin_page()
        self.window().setCentralWidget(window1)

app = QApplication(sys.argv)
ekran = Singin_page()
ana_ekran = QMainWindow()
ana_ekran.setCentralWidget(ekran)
ana_ekran.resize(1363, 816)
ana_ekran.show()
sys.exit(app.exec_())