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
        icon.addPixmap(QtGui.QPixmap(":/icons/Icon1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WearOfBlades.setWindowIcon(icon)
        WearOfBlades.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(WearOfBlades)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, -1, -1, 30)
        self.gridLayout.setObjectName("gridLayout")
        self.fourth_name2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.fourth_name2.setFont(font)
        self.fourth_name2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fourth_name2.setWordWrap(False)
        self.fourth_name2.setObjectName("fourth_name2")
        self.gridLayout.addWidget(self.fourth_name2, 4, 4, 1, 1)
        self.operatingTimeLneEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.operatingTimeLneEdit_2.setInputMask("")
        self.operatingTimeLneEdit_2.setText("")
        self.operatingTimeLneEdit_2.setClearButtonEnabled(True)
        self.operatingTimeLneEdit_2.setObjectName("operatingTimeLneEdit_2")
        self.gridLayout.addWidget(self.operatingTimeLneEdit_2, 10, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("GOST Type BU")
        font.setPointSize(19)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 6)
        self.operatingTimeLneEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.operatingTimeLneEdit3.setInputMask("")
        self.operatingTimeLneEdit3.setText("")
        self.operatingTimeLneEdit3.setClearButtonEnabled(True)
        self.operatingTimeLneEdit3.setObjectName("operatingTimeLneEdit3")
        self.gridLayout.addWidget(self.operatingTimeLneEdit3, 3, 5, 1, 1)
        self.third_name3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.third_name3.setFont(font)
        self.third_name3.setObjectName("third_name3")
        self.gridLayout.addWidget(self.third_name3, 21, 0, 1, 1)
        self.third_name2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.third_name2.setFont(font)
        self.third_name2.setObjectName("third_name2")
        self.gridLayout.addWidget(self.third_name2, 20, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 8, 0, 1, 6)
        self.fifth_name3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        self.resourceLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.resourceLineEdit.setFont(font)
        self.resourceLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.resourceLineEdit.setText("")
        self.resourceLineEdit.setReadOnly(True)
        self.resourceLineEdit.setClearButtonEnabled(True)
        self.resourceLineEdit.setObjectName("resourceLineEdit")
        self.gridLayout.addWidget(self.resourceLineEdit, 5, 5, 1, 1)
        self.timeTestLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.timeTestLineEdit.setClearButtonEnabled(True)
        self.timeTestLineEdit.setObjectName("timeTestLineEdit")
        self.gridLayout.addWidget(self.timeTestLineEdit, 20, 1, 1, 1)
        self.fifth_name1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.fifth_name1.setFont(font)
        self.fifth_name1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fifth_name1.setWordWrap(False)
        self.fifth_name1.setObjectName("fifth_name1")
        self.gridLayout.addWidget(self.fifth_name1, 10, 4, 1, 1)
        self.radiusLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.radiusLineEdit.setInputMask("")
        self.radiusLineEdit.setText("")
        self.radiusLineEdit.setClearButtonEnabled(True)
        self.radiusLineEdit.setObjectName("radiusLineEdit")
        self.gridLayout.addWidget(self.radiusLineEdit, 10, 1, 1, 1)
        self.beforeTestLineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.beforeTestLineEdit2.setClearButtonEnabled(True)
        self.beforeTestLineEdit2.setObjectName("beforeTestLineEdit2")
        self.gridLayout.addWidget(self.beforeTestLineEdit2, 21, 1, 1, 1)
        self.fourth_name1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.fourth_name1.setFont(font)
        self.fourth_name1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fourth_name1.setWordWrap(False)
        self.fourth_name1.setObjectName("fourth_name1")
        self.gridLayout.addWidget(self.fourth_name1, 3, 4, 1, 1)
        self.widthLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.widthLineEdit.setClearButtonEnabled(True)
        self.widthLineEdit.setObjectName("widthLineEdit")
        self.gridLayout.addWidget(self.widthLineEdit, 11, 1, 1, 1)
        self.third_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.third_title.setFont(font)
        self.third_title.setObjectName("third_title")
        self.gridLayout.addWidget(self.third_title, 18, 0, 1, 2)
        self.ratioLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ratioLineEdit.setFont(font)
        self.ratioLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ratioLineEdit.setReadOnly(True)
        self.ratioLineEdit.setClearButtonEnabled(True)
        self.ratioLineEdit.setObjectName("ratioLineEdit")
        self.gridLayout.addWidget(self.ratioLineEdit, 13, 5, 1, 1)
        self.first_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.first_title.setFont(font)
        self.first_title.setObjectName("first_title")
        self.gridLayout.addWidget(self.first_title, 2, 0, 1, 2)
        self.bluntingLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.bluntingLineEdit.setFont(font)
        self.bluntingLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bluntingLineEdit.setReadOnly(True)
        self.bluntingLineEdit.setClearButtonEnabled(True)
        self.bluntingLineEdit.setObjectName("bluntingLineEdit")
        self.gridLayout.addWidget(self.bluntingLineEdit, 13, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 16, 0, 1, 6)
        self.calculateResourcePushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calculateResourcePushButton.setFont(font)
        self.calculateResourcePushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculateResourcePushButton.setStyleSheet("")
        self.calculateResourcePushButton.setObjectName("calculateResourcePushButton")
        self.gridLayout.addWidget(self.calculateResourcePushButton, 5, 4, 1, 1)
        self.afterTestLineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.afterTestLineEdit2.setClearButtonEnabled(True)
        self.afterTestLineEdit2.setObjectName("afterTestLineEdit2")
        self.gridLayout.addWidget(self.afterTestLineEdit2, 22, 1, 1, 1)
        self.first_name2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)
        self.first_name2.setFont(font)
        self.first_name2.setObjectName("first_name2")
        self.gridLayout.addWidget(self.first_name2, 4, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 6)
        self.frequencLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.frequencLineEdit.setInputMask("")
        self.frequencLineEdit.setText("")
        self.frequencLineEdit.setClearButtonEnabled(True)
        self.frequencLineEdit.setObjectName("frequencLineEdit")
        self.gridLayout.addWidget(self.frequencLineEdit, 19, 1, 1, 1)
        self.timeTestLineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.timeTestLineEdit2.setClearButtonEnabled(True)
        self.timeTestLineEdit2.setObjectName("timeTestLineEdit2")
        self.gridLayout.addWidget(self.timeTestLineEdit2, 11, 5, 1, 1)
        self.operatingTimeLneEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.operatingTimeLneEdit.setFont(font)
        self.operatingTimeLneEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.operatingTimeLneEdit.setReadOnly(True)
        self.operatingTimeLneEdit.setClearButtonEnabled(True)
        self.operatingTimeLneEdit.setObjectName("operatingTimeLneEdit")
        self.gridLayout.addWidget(self.operatingTimeLneEdit, 23, 1, 1, 1)
        self.third_name1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.third_name1.setFont(font)
        self.third_name1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.third_name1.setWordWrap(False)
        self.third_name1.setObjectName("third_name1")
        self.gridLayout.addWidget(self.third_name1, 19, 0, 1, 1)
        self.fifth_name2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)
        self.first_name1.setFont(font)
        self.first_name1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.first_name1.setWordWrap(False)
        self.first_name1.setObjectName("first_name1")
        self.gridLayout.addWidget(self.first_name1, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 18, 4, 1, 2)
        self.afterTestLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.afterTestLineEdit.setClearButtonEnabled(True)
        self.afterTestLineEdit.setObjectName("afterTestLineEdit")
        self.gridLayout.addWidget(self.afterTestLineEdit, 4, 1, 1, 1)
        self.maxSpeedLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.maxSpeedLineEdit.setClearButtonEnabled(True)
        self.maxSpeedLineEdit.setObjectName("maxSpeedLineEdit")
        self.gridLayout.addWidget(self.maxSpeedLineEdit, 4, 5, 1, 1)
        self.start_plot_push_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.start_plot_push_button.setFont(font)
        self.start_plot_push_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_plot_push_button.setStyleSheet("")
        self.start_plot_push_button.setObjectName("start_plot_push_button")
        self.gridLayout.addWidget(self.start_plot_push_button, 19, 4, 3, 2)
        self.second_name1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.second_name2.setFont(font)
        self.second_name2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.second_name2.setWordWrap(False)
        self.second_name2.setObjectName("second_name2")
        self.gridLayout.addWidget(self.second_name2, 11, 0, 1, 1)
        self.calculateRatioPushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calculateRatioPushButton.setFont(font)
        self.calculateRatioPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculateRatioPushButton.setStyleSheet("")
        self.calculateRatioPushButton.setObjectName("calculateRatioPushButton")
        self.gridLayout.addWidget(self.calculateRatioPushButton, 13, 4, 1, 1)
        self.second_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.second_title.setFont(font)
        self.second_title.setObjectName("second_title")
        self.gridLayout.addWidget(self.second_title, 9, 0, 1, 2)
        self.wearLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.wearLineEdit.setFont(font)
        self.wearLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.wearLineEdit.setReadOnly(True)
        self.wearLineEdit.setClearButtonEnabled(True)
        self.wearLineEdit.setObjectName("wearLineEdit")
        self.gridLayout.addWidget(self.wearLineEdit, 5, 1, 1, 1)
        self.calculateOperatingTimePushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calculateOperatingTimePushButton.setFont(font)
        self.calculateOperatingTimePushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculateOperatingTimePushButton.setStyleSheet("")
        self.calculateOperatingTimePushButton.setObjectName("calculateOperatingTimePushButton")
        self.gridLayout.addWidget(self.calculateOperatingTimePushButton, 23, 0, 1, 1)
        self.calculateBluntingPushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calculateBluntingPushButton.setFont(font)
        self.calculateBluntingPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculateBluntingPushButton.setStyleSheet("")
        self.calculateBluntingPushButton.setObjectName("calculateBluntingPushButton")
        self.gridLayout.addWidget(self.calculateBluntingPushButton, 13, 0, 1, 1)
        self.second_line = QtWidgets.QFrame(self.centralwidget)
        self.second_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.second_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.second_line.setObjectName("second_line")
        self.gridLayout.addWidget(self.second_line, 15, 3, 1, 1)
        self.third_name4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.third_name4.setFont(font)
        self.third_name4.setObjectName("third_name4")
        self.gridLayout.addWidget(self.third_name4, 22, 0, 1, 1)
        self.maxSpeedLineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.maxSpeedLineEdit2.setClearButtonEnabled(True)
        self.maxSpeedLineEdit2.setObjectName("maxSpeedLineEdit2")
        self.gridLayout.addWidget(self.maxSpeedLineEdit2, 12, 5, 1, 1)
        self.fifth_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fifth_title.setFont(font)
        self.fifth_title.setObjectName("fifth_title")
        self.gridLayout.addWidget(self.fifth_title, 9, 4, 1, 2)
        self.calculateWearPushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calculateWearPushButton.setFont(font)
        self.calculateWearPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculateWearPushButton.setStyleSheet("")
        self.calculateWearPushButton.setObjectName("calculateWearPushButton")
        self.gridLayout.addWidget(self.calculateWearPushButton, 5, 0, 1, 1)
        self.fourth_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fourth_title.setFont(font)
        self.fourth_title.setObjectName("fourth_title")
        self.gridLayout.addWidget(self.fourth_title, 2, 4, 1, 2)
        self.beforeTestLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.beforeTestLineEdit.setInputMask("")
        self.beforeTestLineEdit.setText("")
        self.beforeTestLineEdit.setClearButtonEnabled(True)
        self.beforeTestLineEdit.setObjectName("beforeTestLineEdit")
        self.gridLayout.addWidget(self.beforeTestLineEdit, 3, 1, 1, 1)
        WearOfBlades.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(WearOfBlades)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setObjectName("menuBar")
        self.about_menu = QtWidgets.QMenu(self.menuBar)
        self.about_menu.setSeparatorsCollapsible(False)
        self.about_menu.setObjectName("about_menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        WearOfBlades.setMenuBar(self.menuBar)
        self.about_action = QtWidgets.QAction(WearOfBlades)
        self.about_action.setShortcut("")
        self.about_action.setObjectName("about_action")
        self.authors_action = QtWidgets.QAction(WearOfBlades)
        self.authors_action.setObjectName("authors_action")
        self.about_menu.addSeparator()
        self.about_menu.addAction(self.about_action)
        self.about_menu.addAction(self.authors_action)
        self.menuBar.addAction(self.about_menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(WearOfBlades)
        QtCore.QMetaObject.connectSlotsByName(WearOfBlades)

    def retranslateUi(self, WearOfBlades):
        _translate = QtCore.QCoreApplication.translate
        WearOfBlades.setWindowTitle(_translate("WearOfBlades", "WearOfBlades"))
        self.fourth_name2.setText(_translate("WearOfBlades", "Макс. скорость резания, мин"))
        self.operatingTimeLneEdit_2.setPlaceholderText(_translate("WearOfBlades", "Значение, м"))
        self.label_2.setText(_translate("WearOfBlades", "WearOfBlades"))
        self.operatingTimeLneEdit3.setPlaceholderText(_translate("WearOfBlades", "Значение, м"))
        self.third_name3.setText(_translate("WearOfBlades", " <b>Диаметр ножа до испытания, мм</b>"))
        self.third_name2.setText(_translate("WearOfBlades", " <b>Время исптания ножа, мин</b>"))
        self.fifth_name3.setText(_translate("WearOfBlades", "Макс. скорость резания, м/мин"))
        self.resourceLineEdit.setPlaceholderText(_translate("WearOfBlades", "Ресурс ножа, ч"))
        self.timeTestLineEdit.setPlaceholderText(_translate("WearOfBlades", "Значение, мин"))
        self.fifth_name1.setText(_translate("WearOfBlades", "Предельная наработка ножа, м"))
        self.radiusLineEdit.setPlaceholderText(_translate("WearOfBlades", "Значение, мм"))
        self.beforeTestLineEdit2.setPlaceholderText(_translate("WearOfBlades", "Значение, мм"))
        self.fourth_name1.setText(_translate("WearOfBlades", "Предельная наработка ножа, м"))
        self.widthLineEdit.setPlaceholderText(_translate("WearOfBlades", "Значение, мм"))
        self.third_title.setText(_translate("WearOfBlades", " 3. Предельная наработка дискового ножа, м"))
        self.ratioLineEdit.setPlaceholderText(_translate("WearOfBlades", "Коэф. ускоренных испытаний"))
        self.first_title.setText(_translate("WearOfBlades", " 1. Величина износа дискового ножа, мм"))
        self.bluntingLineEdit.setPlaceholderText(_translate("WearOfBlades", "Относительное затупление, %"))
        self.calculateResourcePushButton.setText(_translate("WearOfBlades", "Рассчитать"))
        self.afterTestLineEdit2.setPlaceholderText(_translate("WearOfBlades", "Значение, мм"))
        self.first_name2.setText(_translate("WearOfBlades", " <b>После испытаний, мм</b>"))
        self.frequencLineEdit.setPlaceholderText(_translate("WearOfBlades", "Значение, об/мин"))
        self.timeTestLineEdit2.setPlaceholderText(_translate("WearOfBlades", "Значение, мин"))
        self.operatingTimeLneEdit.setPlaceholderText(_translate("WearOfBlades", "Предельная наработка, м"))
        self.third_name1.setText(_translate("WearOfBlades", "Частота вращения ножа, об/мин"))
        self.fifth_name2.setText(_translate("WearOfBlades", "Время испытания ножа, мин"))
        self.first_name1.setText(_translate("WearOfBlades", "До испытаний, мм"))
        self.label.setText(_translate("WearOfBlades", "6. Построение графика"))
        self.afterTestLineEdit.setPlaceholderText(_translate("WearOfBlades", "Значение, мм"))
        self.maxSpeedLineEdit.setPlaceholderText(_translate("WearOfBlades", "Значение, мин"))
        self.start_plot_push_button.setText(_translate("WearOfBlades", "Построение графика износа ножа"))
        self.second_name1.setText(_translate("WearOfBlades", "Радиус затупления, мм"))
        self.second_name2.setText(_translate("WearOfBlades", "Толщина лезвия, мм"))
        self.calculateRatioPushButton.setText(_translate("WearOfBlades", "Рассчитать"))
        self.second_title.setText(_translate("WearOfBlades", " 2. Относительное затупление дискового ножа, %"))
        self.wearLineEdit.setPlaceholderText(_translate("WearOfBlades", "Величина износа, мм"))
        self.calculateOperatingTimePushButton.setText(_translate("WearOfBlades", "Рассчитать"))
        self.calculateBluntingPushButton.setText(_translate("WearOfBlades", "Рассчитать"))
        self.third_name4.setText(_translate("WearOfBlades", " <b>Диаметр ножа после испытания, мм</b>"))
        self.maxSpeedLineEdit2.setPlaceholderText(_translate("WearOfBlades", "Значение, м/мин"))
        self.fifth_title.setText(_translate("WearOfBlades", " 5. Коэф. ускоренных испытаний дискового ножа"))
        self.calculateWearPushButton.setText(_translate("WearOfBlades", "Рассчитать"))
        self.fourth_title.setText(_translate("WearOfBlades", " 4. Ресурс дискового ножа, ч"))
        self.beforeTestLineEdit.setPlaceholderText(_translate("WearOfBlades", "Значение, мм"))
        self.about_menu.setTitle(_translate("WearOfBlades", "О программе"))
        self.menu_2.setTitle(_translate("WearOfBlades", "Помощь"))
        self.about_action.setText(_translate("WearOfBlades", "Описание"))
        self.authors_action.setText(_translate("WearOfBlades", "Авторы"))
