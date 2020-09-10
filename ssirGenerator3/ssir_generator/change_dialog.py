
from PyQt5 import QtGui, QtWidgets
#from PyQt5.QtCore import QDialog  

class change_dialog(QtWidgets.QDialog):

    def __init__(self,vals, *args, **kwargs):
        super(change_dialog, self).__init__(*args, **kwargs)
        self.vals=vals
        
        self.setWindowTitle("change segment_no")
        self.layout = QtWidgets.QHBoxLayout()
        
        self.ok_button=QtWidgets.QPushButton()
        self.ok_button.setText('Segment is not in layer')
        self.layout.addWidget(self.ok_button)

        self.cancel_button=QtWidgets.QPushButton()
        self.cancel_button.setText('Cancel')
        self.cancel_button.clicked.connect(self.reject)
        self.layout.addWidget(self.cancel_button)

        self.num=QtWidgets.QSpinBox()
        self.num.setMaximum(max(vals))
        self.num.setMinimum(min(vals))
        
        self.layout.addWidget(self.num)
        
        self.setLayout(self.layout)

    def value_changed(self,value):
        if value in self.vals:
            self.ok_button.setText('OK')
        accept
        
        
cd=change_dialog([1,2,3,4])
cd.show()