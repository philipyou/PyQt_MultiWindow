# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vehiclerentaldlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VehicleRentalDlg(object):
    def setupUi(self, VehicleRentalDlg):
        VehicleRentalDlg.setObjectName("VehicleRentalDlg")
        VehicleRentalDlg.resize(206, 246)
        self.gridlayout = QtWidgets.QGridLayout(VehicleRentalDlg)
        self.gridlayout.setContentsMargins(9, 9, 9, 9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(VehicleRentalDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(188, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 3, 0, 1, 1)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.label_6 = QtWidgets.QLabel(VehicleRentalDlg)
        self.label_6.setObjectName("label_6")
        self.hboxlayout.addWidget(self.label_6)
        self.mileageLabel = QtWidgets.QLabel(VehicleRentalDlg)
        self.mileageLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mileageLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mileageLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mileageLabel.setObjectName("mileageLabel")
        self.hboxlayout.addWidget(self.mileageLabel)
        self.gridlayout.addLayout(self.hboxlayout, 2, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(VehicleRentalDlg)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridlayout1 = QtWidgets.QGridLayout(self.page_2)
        self.gridlayout1.setContentsMargins(9, 9, 9, 9)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")
        self.colorComboBox = QtWidgets.QComboBox(self.page_2)
        self.colorComboBox.setObjectName("colorComboBox")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.colorComboBox.addItem("")
        self.gridlayout1.addWidget(self.colorComboBox, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setObjectName("label_4")
        self.gridlayout1.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setObjectName("label_5")
        self.gridlayout1.addWidget(self.label_5, 1, 0, 1, 1)
        self.seatsSpinBox = QtWidgets.QSpinBox(self.page_2)
        self.seatsSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.seatsSpinBox.setMinimum(2)
        self.seatsSpinBox.setMaximum(12)
        self.seatsSpinBox.setProperty("value", 4)
        self.seatsSpinBox.setObjectName("seatsSpinBox")
        self.gridlayout1.addWidget(self.seatsSpinBox, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridlayout2 = QtWidgets.QGridLayout(self.page)
        self.gridlayout2.setContentsMargins(9, 9, 9, 9)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")
        self.weightSpinBox = QtWidgets.QSpinBox(self.page)
        self.weightSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.weightSpinBox.setMinimum(1)
        self.weightSpinBox.setMaximum(8)
        self.weightSpinBox.setObjectName("weightSpinBox")
        self.gridlayout2.addWidget(self.weightSpinBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.gridlayout2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.gridlayout2.addWidget(self.label_2, 0, 0, 1, 1)
        self.volumeSpinBox = QtWidgets.QSpinBox(self.page)
        self.volumeSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.volumeSpinBox.setMinimum(4)
        self.volumeSpinBox.setMaximum(22)
        self.volumeSpinBox.setProperty("value", 10)
        self.volumeSpinBox.setObjectName("volumeSpinBox")
        self.gridlayout2.addWidget(self.volumeSpinBox, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.gridlayout.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.label = QtWidgets.QLabel(VehicleRentalDlg)
        self.label.setObjectName("label")
        self.hboxlayout1.addWidget(self.label)
        self.vehicleComboBox = QtWidgets.QComboBox(VehicleRentalDlg)
        self.vehicleComboBox.setObjectName("vehicleComboBox")
        self.vehicleComboBox.addItem("")
        self.vehicleComboBox.addItem("")
        self.hboxlayout1.addWidget(self.vehicleComboBox)
        self.gridlayout.addLayout(self.hboxlayout1, 0, 0, 1, 1)
        self.label_4.setBuddy(self.colorComboBox)
        self.label_5.setBuddy(self.seatsSpinBox)
        self.label_3.setBuddy(self.volumeSpinBox)
        self.label_2.setBuddy(self.seatsSpinBox)
        self.label.setBuddy(self.vehicleComboBox)

        self.retranslateUi(VehicleRentalDlg)
        self.stackedWidget.setCurrentIndex(0)
        self.vehicleComboBox.currentIndexChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        self.buttonBox.accepted.connect(VehicleRentalDlg.accept)
        self.buttonBox.rejected.connect(VehicleRentalDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(VehicleRentalDlg)

    def retranslateUi(self, VehicleRentalDlg):
        _translate = QtCore.QCoreApplication.translate
        VehicleRentalDlg.setWindowTitle(_translate("VehicleRentalDlg", "Vehicle Rental"))
        self.label_6.setText(_translate("VehicleRentalDlg", "Max. Mileage:"))
        self.mileageLabel.setText(_translate("VehicleRentalDlg", "1000 miles"))
        self.colorComboBox.setItemText(0, _translate("VehicleRentalDlg", "Black"))
        self.colorComboBox.setItemText(1, _translate("VehicleRentalDlg", "Blue"))
        self.colorComboBox.setItemText(2, _translate("VehicleRentalDlg", "Green"))
        self.colorComboBox.setItemText(3, _translate("VehicleRentalDlg", "Red"))
        self.colorComboBox.setItemText(4, _translate("VehicleRentalDlg", "Silver"))
        self.colorComboBox.setItemText(5, _translate("VehicleRentalDlg", "White"))
        self.colorComboBox.setItemText(6, _translate("VehicleRentalDlg", "Yellow"))
        self.label_4.setText(_translate("VehicleRentalDlg", "Co&lor:"))
        self.label_5.setText(_translate("VehicleRentalDlg", "&Seats:"))
        self.weightSpinBox.setSuffix(_translate("VehicleRentalDlg", " tons"))
        self.label_3.setText(_translate("VehicleRentalDlg", "Volu&me:"))
        self.label_2.setText(_translate("VehicleRentalDlg", "&Weight:"))
        self.volumeSpinBox.setSuffix(_translate("VehicleRentalDlg", " cu m"))
        self.label.setText(_translate("VehicleRentalDlg", "&Vehicle Type:"))
        self.vehicleComboBox.setItemText(0, _translate("VehicleRentalDlg", "Car"))
        self.vehicleComboBox.setItemText(1, _translate("VehicleRentalDlg", "Van"))

