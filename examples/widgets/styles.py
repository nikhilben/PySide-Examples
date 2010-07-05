#!/usr/bin/env python

#############################################################################
##
## Copyright (C) 2004-2005 Trolltech AS. All rights reserved.
##
## This file is part of the example classes of the Qt Toolkit.
##
## This file may be used under the terms of the GNU General Public
## License version 2.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## General Public Licensing requirements will be met:
## http://www.trolltech.com/products/qt/opensource.html
##
## If you are unsure which license is appropriate for your use, please
## review the following information:
## http://www.trolltech.com/products/qt/licensing.html or contact the
## sales department at sales@trolltech.com.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
#############################################################################

import sys
from PySide import QtCore, QtGui


class WidgetGallery(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.originalPalette = QtGui.QApplication.palette()

        styleComboBox = QtGui.QComboBox()
        styleComboBox.addItems(QtGui.QStyleFactory.keys())

        styleLabel = QtGui.QLabel(self.tr("&Style:"))
        styleLabel.setBuddy(styleComboBox)

        self.useStylePaletteCheckBox = QtGui.QCheckBox(self.tr("&Use style's standard palette"))
        self.useStylePaletteCheckBox.setChecked(True)

        disableWidgetsCheckBox = QtGui.QCheckBox(self.tr("&Disable widgets"))

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()
        self.createProgressBar()

        self.connect(styleComboBox, QtCore.SIGNAL("activated(const QString &)"), self.changeStyle)
        self.connect(self.useStylePaletteCheckBox, QtCore.SIGNAL("toggled(bool)"), self.changePalette)
        self.connect(disableWidgetsCheckBox, QtCore.SIGNAL("toggled(bool)"), self.topLeftGroupBox, QtCore.SLOT("setDisabled(bool)"))
        self.connect(disableWidgetsCheckBox, QtCore.SIGNAL("toggled(bool)"), self.topRightGroupBox, QtCore.SLOT("setDisabled(bool)"))
        self.connect(disableWidgetsCheckBox, QtCore.SIGNAL("toggled(bool)"), self.bottomLeftTabWidget, QtCore.SLOT("setDisabled(bool)"))
        self.connect(disableWidgetsCheckBox, QtCore.SIGNAL("toggled(bool)"), self.bottomRightGroupBox, QtCore.SLOT("setDisabled(bool)"))

        topLayout = QtGui.QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(styleComboBox)
        topLayout.addStretch(1)
        topLayout.addWidget(self.useStylePaletteCheckBox)
        topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QtGui.QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle(self.tr("Styles"))
        self.changeStyle("Windows")

    def changeStyle(self, styleName):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(styleName))
        self.changePalette()

    def changePalette(self):
        if (self.useStylePaletteCheckBox.isChecked()):
            QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())
        else:
            QtGui.QApplication.setPalette(self.originalPalette)

    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) / 100)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QtGui.QGroupBox(self.tr("Group 1"))

        radioButton1 = QtGui.QRadioButton(self.tr("Radio button 1"))
        radioButton2 = QtGui.QRadioButton(self.tr("Radio button 2"))
        radioButton3 = QtGui.QRadioButton(self.tr("Radio button 3"))
        radioButton1.setChecked(True)

        checkBox = QtGui.QCheckBox(self.tr("Tri-state check box"))
        checkBox.setTristate(True)
        checkBox.setCheckState(QtCore.Qt.PartiallyChecked)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addWidget(checkBox)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QtGui.QGroupBox(self.tr("Group 2"))

        defaultPushButton = QtGui.QPushButton(self.tr("Default Push Button"))
        defaultPushButton.setDefault(True)

        togglePushButton = QtGui.QPushButton(self.tr("Toggle Push Button"))
        togglePushButton.setCheckable(True)
        togglePushButton.setChecked(True)

        flatPushButton = QtGui.QPushButton(self.tr("Flat Push Button"))
        flatPushButton.setFlat(True)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(defaultPushButton)
        layout.addWidget(togglePushButton)
        layout.addWidget(flatPushButton)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QtGui.QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QtGui.QSizePolicy.Preferred,
                                               QtGui.QSizePolicy.Ignored)

        tab1 = QtGui.QWidget()
        tableWidget = QtGui.QTableWidget(10, 10)

        tab1hbox = QtGui.QHBoxLayout()
        tab1hbox.setMargin(5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        tab2 = QtGui.QWidget()
        textEdit = QtGui.QTextEdit()

        textEdit.setPlainText(self.tr("Twinkle, twinkle, little star,\n"
                                      "How I wonder what you are.\n"
                                      "Up above the world so high,\n"
                                      "Like a diamond in the sky.\n"
                                      "Twinkle, twinkle, little star,\n"
                                      "How I wonder what you are!\n"))

        tab2hbox = QtGui.QHBoxLayout()
        tab2.setLayout(tab2hbox)
        tab2hbox.setMargin(5)
        tab2hbox.addWidget(textEdit)

        self.bottomLeftTabWidget.addTab(tab1, self.tr("&Table"))
        self.bottomLeftTabWidget.addTab(tab2, self.tr("Text &Edit"))

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QtGui.QGroupBox(self.tr("Group 3"))
        self.bottomRightGroupBox.setCheckable(True)
        self.bottomRightGroupBox.setChecked(True)

        lineEdit = QtGui.QLineEdit("s3cRe7")
        lineEdit.setEchoMode(QtGui.QLineEdit.Password)

        spinBox = QtGui.QSpinBox(self.bottomRightGroupBox)
        spinBox.setValue(50)

        dateTimeEdit = QtGui.QDateTimeEdit(self.bottomRightGroupBox)
        dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self.bottomRightGroupBox)
        slider.setValue(40)

        scrollBar = QtGui.QScrollBar(QtCore.Qt.Horizontal, self.bottomRightGroupBox)
        scrollBar.setValue(60)

        dial = QtGui.QDial(self.bottomRightGroupBox)
        dial.setValue(30)
        dial.setNotchesVisible(True)

        layout = QtGui.QGridLayout()
        layout.addWidget(lineEdit, 0, 0, 1, 2)
        layout.addWidget(spinBox, 1, 0, 1, 2)
        layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
        layout.addWidget(slider, 3, 0)
        layout.addWidget(scrollBar, 4, 0)
        layout.addWidget(dial, 3, 1, 2, 1)
        layout.setRowStretch(5, 1)
        self.bottomRightGroupBox.setLayout(layout)

    def createProgressBar(self):
        self.progressBar = QtGui.QProgressBar()
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(0)

        timer = QtCore.QTimer(self)
        self.connect(timer, QtCore.SIGNAL("timeout()"), self.advanceProgressBar)
        timer.start(1000)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())
