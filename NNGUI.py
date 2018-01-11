"""
Creating a GUI that can be launched from terminal and from which a user may select specific frames to track, if they so choose.
"""

import sys
#import RNELBanner_rc
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QPalette
import math
import os

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi()
    
    def setupUi(self):

        self.setWindowTitle("RNEL Rodent Headtracking")
        rowSpacer = QtGui.QSpacerItem(1, 20)
        columnSpacer = QtGui.QSpacerItem(50, 1)

        # Highlight input that is currently selected
        self.setFocusPolicy(QtCore.Qt.ClickFocus)

        # Create UI elements
        label_banner = QtGui.QLabel()
        label_banner.setText("")
        #label_banner.setPixmap(QtGui.QPixmap(":/RNELicon/RNELBanner.png"))

        font = QtGui.QFont("Helvetica", 12, 75)
        font.setBold(True)
        
        # label_motorState = QtGui.QLabel("Stepper Motor Parameters")
        # label_motorState.setFont(font)
        label_time = QtGui.QLabel("Select Display Speed:")
        label_endframe = QtGui.QLabel("End Frame Selection:")
        label_stframe = QtGui.QLabel("Beginning Frame Selection:")
#        label_mode = QtGui.QLabel("Mode:")		
        label_headPosition = QtGui.QLabel("Head Position: ") #LOOK HERE	
        label_headPosition.setFont(font)

        self.headPosition = QtGui.QLCDNumber(self) #LOOK HERE 
        self.headPosition.setFont(font)
        palette = QPalette()
       # palette.setBrush(QtGui.QPalette.Light, QtCore.Qt.black)
        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        self.headPosition.setPalette(palette)

        self.headPosition.setDigitCount(8)
        self.threadclass = HeadPosition()
        self.threadclass.start()
		
        self.connect(self.threadclass, QtCore.SIGNAL('POS'), self.updateHeadPosition)        
        
        self.headPosition.display(0,0) # just so something is there
                
        self.comboBox_time = QtGui.QComboBox()
        self.comboBox_time.addItems(["0.5X Speed","Real Time Speed","2X Speed"])
        self.comboBox_time.setCurrentIndex(1)
        self.lineEdit_stframe = QtGui.QLineEdit()
        self.lineEdit_stframe.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_stframe.setText("0")
        self.lineEdit_endframe = QtGui.QLineEdit()
        self.lineEdit_endframe.setMaximumSize(QtCore.QSize(100, 30))
        # Implement some way to determine amount of frames in video in NNTracker
        # and feed through to endframe default
        self.lineEdit_endframe.setText("-")
        
        self.preset_checkbox = QtGui.QCheckBox("Manually Select Frames to be Run")
        self.preset_checkbox.setCheckState(False)
        #label_level = QtGui.QLabel("Level:")
        #self.comboBox_level = QtGui.QComboBox()
        #self.comboBox_level.addItems(["1", "2", "3"])
        #self.comboBox_level.setEnabled(False)

        # label_assign = QtGui.QLabel("Assign position to level?")
        # self.btn_assign = QtGui.QPushButton("Assign")
        # self.btn_assign.setEnabled(False)

        # self.btn_run = QtGui.QPushButton("Run")
        # self.btn_doorstat = QtGui.QPushButton("Open/Close")
        # self.progress_bar = QtGui.QProgressBar()
        # self.btn_doorstat = QtGui.QPushButton("Open/Close")

        label_history = QtGui.QLabel("Command History")
        label_history.setFont(font)
        self.command_history = QtGui.QPlainTextEdit()
        self.command_history.setMaximumSize(QtCore.QSize(1000, 500))
        self.command_history.setReadOnly(True)
        # self.command_history.appendPlainText("Note: The speed will be scaled according to the microstepping mode.")
        self.command_history.appendPlainText("Note: By choosing a slower speed, the head tracking approximations may be more accurate.")
        self.command_history.appendPlainText("")

        font = QtGui.QFont("Helvetica", 12)
        label_instructions = QtGui.QLabel("Please visit the following site for instructions:")
        label_instructions.setFont(font)

        label_website = QtGui.QLabel()
        label_website.setFont(font)
        label_website.setText("<a href=\"https://github.com/arielfeldman/NNVideoTracking/\">RNEL Head Tracking Program</a>")
        label_website.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        label_website.setOpenExternalLinks(True)

        # Format UI elements
        formLayout = QtGui.QFormLayout()
        formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        formLayout.setLabelAlignment(QtCore.Qt.AlignLeft)
        formLayout.addRow(label_time, self.comboBox_time)
        formLayout.addRow(label_endframe, self.lineEdit_stframe)
        #formLayout.addRow(label_direction, self.comboBox_direction)
        #formLayout.addRow(label_mode, self.comboBox_mode)
        #formLayout.addRow(label_torque, self.comboBox_torque)
       
        formLayout2 = QtGui.QFormLayout()
        formLayout2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        formLayout2.setLabelAlignment(QtCore.Qt.AlignLeft)
        #formLayout2.addRow(label_level, self.comboBox_level)

        formLayout2.addRow(label_headPosition, self.headPosition) #LOOK HERE

        verticalLayout = QtGui.QVBoxLayout()
        verticalLayout.addWidget(self.preset_checkbox)
        verticalLayout.addLayout(formLayout2)
        verticalLayout.addStretch()
        verticalLayout.addWidget(label_assign)
        verticalLayout.addWidget(self.btn_assign, 0, QtCore.Qt.AlignHCenter)

        horizontalLayout = QtGui.QHBoxLayout()
        horizontalLayout.addLayout(formLayout)
        horizontalLayout.addSpacerItem(columnSpacer)
        horizontalLayout.addLayout(verticalLayout)

        verticalLayout2 = QtGui.QVBoxLayout(self)
        verticalLayout2.setContentsMargins(30, 20, 30, 20)
        verticalLayout2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        verticalLayout2.addWidget(label_banner, 0, QtCore.Qt.AlignHCenter)
        verticalLayout2.addSpacerItem(rowSpacer)
        verticalLayout2.addWidget(label_motorState)
        verticalLayout2.addLayout(horizontalLayout)
        verticalLayout2.addWidget(self.btn_run, 0, QtCore.Qt.AlignHCenter)
        verticalLayout2.addWidget(self.btn_doorstat, 0, QtCore.Qt.AlignRight)
        verticalLayout2.addWidget(self.progress_bar)
        verticalLayout2.addSpacerItem(rowSpacer)
        formLayout3 = QtGui.QFormLayout()
        verticalLayout2.addLayout(formLayout3)

        formLayout3.addRow(label_headPosition, self.headPosition) #LOOK HERE
     
        verticalLayout2.addWidget(label_history)
        verticalLayout2.addWidget(self.command_history)
        verticalLayout2.addSpacerItem(rowSpacer)
        verticalLayout2.addWidget(label_instructions)
        verticalLayout2.addWidget(label_website)

        # self.btn_run.clicked.connect(self.collectMotorData)
        # self.btn_doorstat.clicked.connect(self.sendServoData)
        self.preset_checkbox.stateChanged.connect(self.updateUI)
        #self.comboBox_level.currentIndexChanged.connect(self.updateUI)
        #self.btn_assign.clicked.connect(self.assignPosition)
        self.btn_assign.clicked.connect(self.updateUI)
    
    def updateUI(self):
        if self.preset_checkbox.checkState() == 0:
            self.lineEdit_stframe.setEnabled(True)
            self.lineEdit_stframe.setText("0")
            #self.comboBox_direction.setEnabled(True)
            #self.comboBox_level.setEnabled(False)
            self.btn_assign.setEnabled(False)
        
        #if self.preset_checkbox.checkState() == 2:
            #self.lineEdit_stframe.setEnabled(False)
            #self.lineEdit_stframe.setText(str(steps))
            #self.comboBox_direction.setEnabled(False)
        
            #if direction == "Up":
                #self.comboBox_direction.setCurrentIndex(0)
        
            # else:
            #     self.comboBox_direction.setCurrentIndex(1)
        
            # self.comboBox_level.setEnabled(True)
            # self.btn_assign.setEnabled(True)

    def updateHeadPosition(self, val):
        self.headPosition.display(val)

if __name__ == '__main__':
    # allows us to run the GUI from the command line
    app = QtGui.QApplication(sys.argv)
    
    ex = Ui_Form()
    ex.show()
        
    ex.raise_()
    
    sys.exit(app.exec_())