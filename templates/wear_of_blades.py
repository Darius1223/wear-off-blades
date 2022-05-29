# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templates\wear_of_blades.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WearOfBlades(object):
    def setupUi(self, WearOfBlades):
        WearOfBlades.setObjectName("WearOfBlades")
        WearOfBlades.resize(900, 650)
        WearOfBlades.setMinimumSize(QtCore.QSize(900, 650))
        WearOfBlades.setMaximumSize(QtCore.QSize(800, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/Icon1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        WearOfBlades.setWindowIcon(icon)
        WearOfBlades.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(WearOfBlades)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.fourth_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fourth_pushButton.setFont(font)
        self.fourth_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fourth_pushButton.setStyleSheet("")
        self.fourth_pushButton.setObjectName("fourth_pushButton")
        self.gridLayout.addWidget(self.fourth_pushButton, 5, 4, 1, 2)
        self.fourth_name2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.fourth_name2.setFont(font)
        self.fourth_name2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fourth_name2.setWordWrap(False)
        self.fourth_name2.setObjectName("fourth_name2")
        self.gridLayout.addWidget(self.fourth_name2, 4, 4, 1, 1)
        self.fifth_lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.fifth_lineEdit1.setInputMask("")
        self.fifth_lineEdit1.setText("")
        self.fifth_lineEdit1.setClearButtonEnabled(True)
        self.fifth_lineEdit1.setObjectName("fifth_lineEdit1")
        self.gridLayout.addWidget(self.fifth_lineEdit1, 10, 5, 1, 1)
        self.fifth_lineEdit4 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.fifth_lineEdit4.setFont(font)
        self.fifth_lineEdit4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fifth_lineEdit4.setClearButtonEnabled(True)
        self.fifth_lineEdit4.setObjectName("fifth_lineEdit4")
        self.gridLayout.addWidget(self.fifth_lineEdit4, 14, 4, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("GOST Type BU")
        font.setPointSize(19)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 6)
        self.fourth_lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.fourth_lineEdit1.setInputMask("")
        self.fourth_lineEdit1.setText("")
        self.fourth_lineEdit1.setClearButtonEnabled(True)
        self.fourth_lineEdit1.setObjectName("fourth_lineEdit1")
        self.gridLayout.addWidget(self.fourth_lineEdit1, 3, 5, 1, 1)
        self.third_name3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.third_name3.setFont(font)
        self.third_name3.setObjectName("third_name3")
        self.gridLayout.addWidget(self.third_name3, 20, 0, 1, 1)
        self.third_name2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.third_name2.setFont(font)
        self.third_name2.setObjectName("third_name2")
        self.gridLayout.addWidget(self.third_name2, 19, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 8, 0, 1, 6)
        self.fifth_name3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.fifth_name3.setFont(font)
        self.fifth_name3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fifth_name3.setWordWrap(False)
        self.fifth_name3.setObjectName("fifth_name3")
        self.gridLayout.addWidget(self.fifth_name3, 12, 4, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 7, 3, 1, 1)
        self.first_lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.first_lineEdit1.setInputMask("")
        self.first_lineEdit1.setText("")
        self.first_lineEdit1.setClearButtonEnabled(True)
        self.first_lineEdit1.setObjectName("first_lineEdit1")
        self.gridLayout.addWidget(self.first_lineEdit1, 3, 1, 1, 1)
        self.fifth_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fifth_pushButton.setFont(font)
        self.fifth_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fifth_pushButton.setStyleSheet("")
        self.fifth_pushButton.setObjectName("fifth_pushButton")
        self.gridLayout.addWidget(self.fifth_pushButton, 13, 4, 1, 2)
        self.third_lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.third_lineEdit2.setClearButtonEnabled(True)
        self.third_lineEdit2.setObjectName("third_lineEdit2")
        self.gridLayout.addWidget(self.third_lineEdit2, 19, 1, 1, 1)
        self.third_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.third_pushButton.setFont(font)
        self.third_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.third_pushButton.setStyleSheet("")
        self.third_pushButton.setObjectName("third_pushButton")
        self.gridLayout.addWidget(self.third_pushButton, 22, 0, 1, 2)
        self.fifth_name1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.fifth_name1.setFont(font)
        self.fifth_name1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fifth_name1.setWordWrap(False)
        self.fifth_name1.setObjectName("fifth_name1")
        self.gridLayout.addWidget(self.fifth_name1, 10, 4, 1, 1)
        self.second_lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.second_lineEdit1.setInputMask("")
        self.second_lineEdit1.setText("")
        self.second_lineEdit1.setClearButtonEnabled(True)
        self.second_lineEdit1.setObjectName("second_lineEdit1")
        self.gridLayout.addWidget(self.second_lineEdit1, 10, 1, 1, 1)
        self.third_lineEdit5 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.third_lineEdit5.setFont(font)
        self.third_lineEdit5.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.third_lineEdit5.setClearButtonEnabled(True)
        self.third_lineEdit5.setObjectName("third_lineEdit5")
        self.gridLayout.addWidget(self.third_lineEdit5, 23, 0, 1, 2)
        self.third_lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.third_lineEdit3.setClearButtonEnabled(True)
        self.third_lineEdit3.setObjectName("third_lineEdit3")
        self.gridLayout.addWidget(self.third_lineEdit3, 20, 1, 1, 1)
        self.fourth_name1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.fourth_name1.setFont(font)
        self.fourth_name1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fourth_name1.setWordWrap(False)
        self.fourth_name1.setObjectName("fourth_name1")
        self.gridLayout.addWidget(self.fourth_name1, 3, 4, 1, 1)
        self.second_lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.second_lineEdit2.setClearButtonEnabled(True)
        self.second_lineEdit2.setObjectName("second_lineEdit2")
        self.gridLayout.addWidget(self.second_lineEdit2, 11, 1, 1, 1)
        self.third_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.third_title.setFont(font)
        self.third_title.setObjectName("third_title")
        self.gridLayout.addWidget(self.third_title, 17, 0, 1, 2)
        self.first_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.first_title.setFont(font)
        self.first_title.setObjectName("first_title")
        self.gridLayout.addWidget(self.first_title, 2, 0, 1, 2)
        self.fourth_lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.fourth_lineEdit3.setFont(font)
        self.fourth_lineEdit3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fourth_lineEdit3.setText("")
        self.fourth_lineEdit3.setClearButtonEnabled(True)
        self.fourth_lineEdit3.setObjectName("fourth_lineEdit3")
        self.gridLayout.addWidget(self.fourth_lineEdit3, 6, 4, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 16, 0, 1, 6)
        self.third_lineEdit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.third_lineEdit4.setClearButtonEnabled(True)
        self.third_lineEdit4.setObjectName("third_lineEdit4")
        self.gridLayout.addWidget(self.third_lineEdit4, 21, 1, 1, 1)
        self.first_name2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.first_name2.setFont(font)
        self.first_name2.setObjectName("first_name2")
        self.gridLayout.addWidget(self.first_name2, 4, 0, 1, 1)
        self.third_lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.third_lineEdit1.setInputMask("")
        self.third_lineEdit1.setText("")
        self.third_lineEdit1.setClearButtonEnabled(True)
        self.third_lineEdit1.setObjectName("third_lineEdit1")
        self.gridLayout.addWidget(self.third_lineEdit1, 18, 1, 1, 1)
        self.first_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.first_pushButton.setFont(font)
        self.first_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.first_pushButton.setStyleSheet("")
        self.first_pushButton.setObjectName("first_pushButton")
        self.gridLayout.addWidget(self.first_pushButton, 5, 0, 1, 2)
        self.fifth_lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.fifth_lineEdit2.setClearButtonEnabled(True)
        self.fifth_lineEdit2.setObjectName("fifth_lineEdit2")
        self.gridLayout.addWidget(self.fifth_lineEdit2, 11, 5, 1, 1)
        self.third_name1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.third_name1.setFont(font)
        self.third_name1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.third_name1.setWordWrap(False)
        self.third_name1.setObjectName("third_name1")
        self.gridLayout.addWidget(self.third_name1, 18, 0, 1, 1)
        self.fifth_name2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.fifth_name2.setFont(font)
        self.fifth_name2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fifth_name2.setWordWrap(False)
        self.fifth_name2.setObjectName("fifth_name2")
        self.gridLayout.addWidget(self.fifth_name2, 11, 4, 1, 1)
        self.first_name1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.first_name1.setFont(font)
        self.first_name1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.first_name1.setWordWrap(False)
        self.first_name1.setObjectName("first_name1")
        self.gridLayout.addWidget(self.first_name1, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 17, 4, 1, 2)
        self.first_lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.first_lineEdit2.setClearButtonEnabled(True)
        self.first_lineEdit2.setObjectName("first_lineEdit2")
        self.gridLayout.addWidget(self.first_lineEdit2, 4, 1, 1, 1)
        self.first_lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.first_lineEdit3.setFont(font)
        self.first_lineEdit3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.first_lineEdit3.setClearButtonEnabled(True)
        self.first_lineEdit3.setObjectName("first_lineEdit3")
        self.gridLayout.addWidget(self.first_lineEdit3, 6, 0, 1, 2)
        self.fourth_lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.fourth_lineEdit2.setClearButtonEnabled(True)
        self.fourth_lineEdit2.setObjectName("fourth_lineEdit2")
        self.gridLayout.addWidget(self.fourth_lineEdit2, 4, 5, 1, 1)
        self.start_plot_push_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.start_plot_push_button.setFont(font)
        self.start_plot_push_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.start_plot_push_button.setStyleSheet("")
        self.start_plot_push_button.setObjectName("start_plot_push_button")
        self.gridLayout.addWidget(self.start_plot_push_button, 18, 4, 3, 2)
        self.second_name1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.second_name1.setFont(font)
        self.second_name1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.second_name1.setWordWrap(False)
        self.second_name1.setObjectName("second_name1")
        self.gridLayout.addWidget(self.second_name1, 10, 0, 1, 1)
        self.second_name2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.second_name2.setFont(font)
        self.second_name2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.second_name2.setWordWrap(False)
        self.second_name2.setObjectName("second_name2")
        self.gridLayout.addWidget(self.second_name2, 11, 0, 1, 1)
        self.second_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.second_title.setFont(font)
        self.second_title.setObjectName("second_title")
        self.gridLayout.addWidget(self.second_title, 9, 0, 1, 2)
        self.second_line = QtWidgets.QFrame(self.centralwidget)
        self.second_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.second_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.second_line.setObjectName("second_line")
        self.gridLayout.addWidget(self.second_line, 15, 3, 1, 1)
        self.third_name4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.third_name4.setFont(font)
        self.third_name4.setObjectName("third_name4")
        self.gridLayout.addWidget(self.third_name4, 21, 0, 1, 1)
        self.fifth_lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.fifth_lineEdit3.setClearButtonEnabled(True)
        self.fifth_lineEdit3.setObjectName("fifth_lineEdit3")
        self.gridLayout.addWidget(self.fifth_lineEdit3, 12, 5, 1, 1)
        self.fifth_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fifth_title.setFont(font)
        self.fifth_title.setObjectName("fifth_title")
        self.gridLayout.addWidget(self.fifth_title, 9, 4, 1, 2)
        self.fourth_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fourth_title.setFont(font)
        self.fourth_title.setObjectName("fourth_title")
        self.gridLayout.addWidget(self.fourth_title, 2, 4, 1, 2)
        self.second_lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.second_lineEdit3.setFont(font)
        self.second_lineEdit3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.second_lineEdit3.setClearButtonEnabled(True)
        self.second_lineEdit3.setObjectName("second_lineEdit3")
        self.gridLayout.addWidget(self.second_lineEdit3, 14, 0, 1, 2)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 6)
        self.second_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.second_pushButton.setFont(font)
        self.second_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.second_pushButton.setStyleSheet("")
        self.second_pushButton.setObjectName("second_pushButton")
        self.gridLayout.addWidget(self.second_pushButton, 13, 0, 1, 2)
        WearOfBlades.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(WearOfBlades)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setSeparatorsCollapsible(False)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        WearOfBlades.setMenuBar(self.menuBar)
        self.about = QtWidgets.QAction(WearOfBlades)
        self.about.setObjectName("about")
        self.authors = QtWidgets.QAction(WearOfBlades)
        self.authors.setObjectName("authors")
        self.menu.addSeparator()
        self.menu.addAction(self.about)
        self.menu.addAction(self.authors)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(WearOfBlades)
        QtCore.QMetaObject.connectSlotsByName(WearOfBlades)

    def retranslateUi(self, WearOfBlades):
        _translate = QtCore.QCoreApplication.translate
        WearOfBlades.setWindowTitle(_translate("WearOfBlades", "WearOfBlades"))
        self.fourth_pushButton.setText(_translate("WearOfBlades", "Рассчитать"))
        self.fourth_name2.setText(
            _translate("WearOfBlades", "Макс. скорость резания, мин")
        )
        self.fifth_lineEdit1.setPlaceholderText(
            _translate("WearOfBlades", "Значение, м")
        )
        self.fifth_lineEdit4.setPlaceholderText(
            _translate("WearOfBlades", "Коэф. ускоренных испытаний")
        )
        self.label_2.setText(_translate("WearOfBlades", "WearOfBlades"))
        self.fourth_lineEdit1.setPlaceholderText(
            _translate("WearOfBlades", "Значение, м")
        )
        self.third_name3.setText(
            _translate("WearOfBlades", " <b>Диаметр ножа до испытания, мм</b>")
        )
        self.third_name2.setText(
            _translate("WearOfBlades", " <b>Время исптания ножа, мин</b>")
        )
        self.fifth_name3.setText(
            _translate("WearOfBlades", "Макс. скорость резания, м/мин")
        )
        self.first_lineEdit1.setPlaceholderText(
            _translate("WearOfBlades", "Значение, мм")
        )
        self.fifth_pushButton.setText(_translate("WearOfBlades", "Рассчитать"))
        self.third_lineEdit2.setPlaceholderText(
            _translate("WearOfBlades", "Значение, мин")
        )
        self.third_pushButton.setText(_translate("WearOfBlades", "Рассчитать"))
        self.fifth_name1.setText(
            _translate("WearOfBlades", "Предельная наработка ножа, м")
        )
        self.second_lineEdit1.setPlaceholderText(
            _translate("WearOfBlades", "Значение, мм")
        )
        self.third_lineEdit5.setPlaceholderText(
            _translate("WearOfBlades", "Предельная наработка, м")
        )
        self.third_lineEdit3.setPlaceholderText(
            _translate("WearOfBlades", "Значение, мм")
        )
        self.fourth_name1.setText(
            _translate("WearOfBlades", "Предельная наработка ножа, м")
        )
        self.second_lineEdit2.setPlaceholderText(
            _translate("WearOfBlades", "Значение, мм")
        )
        self.third_title.setText(
            _translate("WearOfBlades", " 3. Предельная наработка дискового ножа, м")
        )
        self.first_title.setText(
            _translate("WearOfBlades", " 1. Величина износа дискового ножа, мм")
        )
        self.fourth_lineEdit3.setPlaceholderText(
            _translate("WearOfBlades", "Ресурс ножа, ч")
        )
        self.third_lineEdit4.setPlaceholderText(
            _translate("WearOfBlades", "Значение, мм")
        )
        self.first_name2.setText(
            _translate("WearOfBlades", " <b>После испытаний, мм</b>")
        )
        self.third_lineEdit1.setPlaceholderText(
            _translate("WearOfBlades", "Значение, об/мин")
        )
        self.first_pushButton.setText(_translate("WearOfBlades", "Рассчитать"))
        self.fifth_lineEdit2.setPlaceholderText(
            _translate("WearOfBlades", "Значение, мин")
        )
        self.third_name1.setText(
            _translate("WearOfBlades", "Частота вращения ножа, об/мин")
        )
        self.fifth_name2.setText(
            _translate("WearOfBlades", "Время испытания ножа, мин")
        )
        self.first_name1.setText(_translate("WearOfBlades", "До испытаний, мм"))
        self.label.setText(_translate("WearOfBlades", "6. Построение графика"))
        self.first_lineEdit2.setPlaceholderText(
            _translate("WearOfBlades", "Значение, мм")
        )
        self.first_lineEdit3.setPlaceholderText(
            _translate("WearOfBlades", "Величина износа, мм")
        )
        self.fourth_lineEdit2.setPlaceholderText(
            _translate("WearOfBlades", "Значение, мин")
        )
        self.start_plot_push_button.setText(
            _translate("WearOfBlades", "Построение графика износа ножа")
        )
        self.second_name1.setText(_translate("WearOfBlades", "Радиус затупления, мм"))
        self.second_name2.setText(_translate("WearOfBlades", "Толщина лезвия, мм"))
        self.second_title.setText(
            _translate("WearOfBlades", " 2. Относительное затупление дискового ножа, %")
        )
        self.third_name4.setText(
            _translate("WearOfBlades", " <b>Диаметр ножа после испытания, мм</b>")
        )
        self.fifth_lineEdit3.setPlaceholderText(
            _translate("WearOfBlades", "Значение, м/мин")
        )
        self.fifth_title.setText(
            _translate("WearOfBlades", " 5. Коэф. ускоренных испытаний дискового ножа")
        )
        self.fourth_title.setText(
            _translate("WearOfBlades", " 4. Ресурс дискового ножа, ч")
        )
        self.second_lineEdit3.setPlaceholderText(
            _translate("WearOfBlades", "Относительное затупление, %")
        )
        self.second_pushButton.setText(_translate("WearOfBlades", "Рассчитать"))
        self.menu.setTitle(_translate("WearOfBlades", "О программе"))
        self.menu_2.setTitle(_translate("WearOfBlades", "Помощь"))
        self.about.setText(_translate("WearOfBlades", "Описание"))
        self.authors.setText(_translate("WearOfBlades", "Авторы"))
