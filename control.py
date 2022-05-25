# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(426, 348)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.row_count_spin_box = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.row_count_spin_box.sizePolicy().hasHeightForWidth())
        self.row_count_spin_box.setSizePolicy(sizePolicy)
        self.row_count_spin_box.setMinimumSize(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.row_count_spin_box.setFont(font)
        self.row_count_spin_box.setMaximum(999)
        self.row_count_spin_box.setObjectName("row_count_spin_box")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.row_count_spin_box)
        self.row_count_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.row_count_button.sizePolicy().hasHeightForWidth())
        self.row_count_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.row_count_button.setFont(font)
        self.row_count_button.setObjectName("row_count_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.row_count_button)
        self.plot_count_spin_box = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_count_spin_box.sizePolicy().hasHeightForWidth())
        self.plot_count_spin_box.setSizePolicy(sizePolicy)
        self.plot_count_spin_box.setMinimumSize(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.plot_count_spin_box.setFont(font)
        self.plot_count_spin_box.setMinimum(1)
        self.plot_count_spin_box.setMaximum(999)
        self.plot_count_spin_box.setObjectName("plot_count_spin_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.plot_count_spin_box)
        self.plot_count_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_count_button.sizePolicy().hasHeightForWidth())
        self.plot_count_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.plot_count_button.setFont(font)
        self.plot_count_button.setObjectName("plot_count_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plot_count_button)
        self.plot_button = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.plot_button.setFont(font)
        self.plot_button.setObjectName("plot_button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.plot_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.plot_avg_buttin = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.plot_avg_buttin.setFont(font)
        self.plot_avg_buttin.setObjectName("plot_avg_buttin")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.plot_avg_buttin)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.row_count_button.setText(_translate("Form", "Выбрать кол-во строк"))
        self.plot_count_button.setText(_translate("Form", "Выбрать кол-во графиков"))
        self.plot_button.setText(_translate("Form", "Построить график"))
        self.plot_avg_buttin.setText(_translate("Form", "Построить средний график"))
