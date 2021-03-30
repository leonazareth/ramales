# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'block_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BlockDialog(object):
    def setupUi(self, BlockDialog):
        BlockDialog.setObjectName("BlockDialog")
        BlockDialog.resize(729, 619)
        self.gridLayout_2 = QtWidgets.QGridLayout(BlockDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(BlockDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 5, 0, 1, 2)
        self.generalBox = QtWidgets.QGroupBox(BlockDialog)
        self.generalBox.setObjectName("generalBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.generalBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.dateLabel = QtWidgets.QLabel(self.generalBox)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dateLabel)
        self.date = QtWidgets.QDateEdit(self.generalBox)
        self.date.setCalendarPopup(True)
        self.date.setObjectName("date")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.date)
        self.block = QtWidgets.QLabel(self.generalBox)
        self.block.setObjectName("block")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.block)
        self.blockName = QtWidgets.QLineEdit(self.generalBox)
        self.blockName.setObjectName("blockName")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.blockName)
        self.watershedLabel = QtWidgets.QLabel(self.generalBox)
        self.watershedLabel.setObjectName("watershedLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.watershedLabel)
        self.watershed = QtWidgets.QLineEdit(self.generalBox)
        self.watershed.setObjectName("watershed")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.watershed)
        self.minDepthLabel = QtWidgets.QLabel(self.generalBox)
        self.minDepthLabel.setObjectName("minDepthLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.minDepthLabel)
        self.minDepth = QtWidgets.QDoubleSpinBox(self.generalBox)
        self.minDepth.setObjectName("minDepth")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.minDepth)
        self.minSlopeLabel = QtWidgets.QLabel(self.generalBox)
        self.minSlopeLabel.setObjectName("minSlopeLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.minSlopeLabel)
        self.minSlope = QtWidgets.QDoubleSpinBox(self.generalBox)
        self.minSlope.setDecimals(3)
        self.minSlope.setObjectName("minSlope")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.minSlope)
        self.gridLayout_2.addWidget(self.generalBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(BlockDialog)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 223))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.revisionLabel = QtWidgets.QLabel(self.groupBox_2)
        self.revisionLabel.setObjectName("revisionLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.revisionLabel)
        self.revision = QtWidgets.QLineEdit(self.groupBox_2)
        self.revision.setObjectName("revision")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.revision)
        self.revisionDateLabel = QtWidgets.QLabel(self.groupBox_2)
        self.revisionDateLabel.setObjectName("revisionDateLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.revisionDateLabel)
        self.revisionDate = QtWidgets.QDateEdit(self.groupBox_2)
        self.revisionDate.setCalendarPopup(True)
        self.revisionDate.setObjectName("revisionDate")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.revisionDate)
        self.totalLengthLabel = QtWidgets.QLabel(self.groupBox_2)
        self.totalLengthLabel.setObjectName("totalLengthLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.totalLengthLabel)
        self.totalLength = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.totalLength.setEnabled(False)
        self.totalLength.setObjectName("totalLength")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.totalLength)
        self.observationsLabel = QtWidgets.QLabel(self.groupBox_2)
        self.observationsLabel.setObjectName("observationsLabel")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.observationsLabel)
        self.observations = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.observations.setMaximumSize(QtCore.QSize(16777215, 80))
        self.observations.setObjectName("observations")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.observations)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(BlockDialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 4, 0, 1, 2)

        self.retranslateUi(BlockDialog)
        self.buttonBox.accepted.connect(BlockDialog.accept)
        self.buttonBox.rejected.connect(BlockDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BlockDialog)
        BlockDialog.setTabOrder(self.date, self.blockName)
        BlockDialog.setTabOrder(self.blockName, self.watershed)
        BlockDialog.setTabOrder(self.watershed, self.minDepth)
        BlockDialog.setTabOrder(self.minDepth, self.minSlope)
        BlockDialog.setTabOrder(self.minSlope, self.revision)
        BlockDialog.setTabOrder(self.revision, self.revisionDate)
        BlockDialog.setTabOrder(self.revisionDate, self.totalLength)

    def retranslateUi(self, BlockDialog):
        _translate = QtCore.QCoreApplication.translate
        BlockDialog.setWindowTitle(_translate("BlockDialog", "Manzana"))
        self.generalBox.setTitle(_translate("BlockDialog", "Generales"))
        self.dateLabel.setText(_translate("BlockDialog", "Fecha"))
        self.date.setDisplayFormat(_translate("BlockDialog", "dd/MM/yyyy"))
        self.block.setText(_translate("BlockDialog", "Manzana"))
        self.watershedLabel.setText(_translate("BlockDialog", "Cuenca"))
        self.minDepthLabel.setText(_translate("BlockDialog", "Profundidad mínima"))
        self.minSlopeLabel.setText(_translate("BlockDialog", "Pendiente mínima"))
        self.groupBox_2.setTitle(_translate("BlockDialog", "Cuantitativos"))
        self.revisionLabel.setText(_translate("BlockDialog", "Revisión"))
        self.revisionDateLabel.setText(_translate("BlockDialog", "Fecha Revisión"))
        self.revisionDate.setDisplayFormat(_translate("BlockDialog", "dd/MM/yyyy"))
        self.totalLengthLabel.setText(_translate("BlockDialog", "Longitud total"))
        self.observationsLabel.setText(_translate("BlockDialog", "Observaciones"))
