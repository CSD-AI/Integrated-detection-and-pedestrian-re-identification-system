# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'targetSelect.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1091, 604)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 2, 1, 2)
        self.lbl_msg = QtWidgets.QLabel(Dialog)
        self.lbl_msg.setText("")
        self.lbl_msg.setObjectName("lbl_msg")
        self.gridLayout.addWidget(self.lbl_msg, 4, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 0.8)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 2, 2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout.addWidget(self.btn_cancel, 6, 2, 1, 2)
        self.btn_yes = QtWidgets.QPushButton(Dialog)
        self.btn_yes.setObjectName("btn_yes")
        self.gridLayout.addWidget(self.btn_yes, 5, 2, 1, 2)
        self.scrollArea_vertical = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_vertical.setWidgetResizable(True)
        self.scrollArea_vertical.setObjectName("scrollArea_vertical")
        self.scrollAreaWidgetContents_vertical = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_vertical.setGeometry(QtCore.QRect(0, 0, 956, 548))
        self.scrollAreaWidgetContents_vertical.setObjectName("scrollAreaWidgetContents_vertical")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_vertical)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea_vertical.setWidget(self.scrollAreaWidgetContents_vertical)
        self.gridLayout.addWidget(self.scrollArea_vertical, 2, 0, 6, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "选择"))
        self.label.setText(_translate("Dialog", "请选择追踪目标"))
        self.label_2.setText(_translate("Dialog", "置信度"))
        self.btn_cancel.setText(_translate("Dialog", "取消"))
        self.btn_yes.setText(_translate("Dialog", "确定"))
