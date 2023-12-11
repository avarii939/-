
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox, QTextEdit)  
smart_width,smart_height = 600, 500
ma_smart_wi= QWidget()
add_zam = QPushButton('')
li_zam_txt = QLabel('')
li_zam = QListWidget()
del_zam = QPushButton('')
save_zam = QPushButton('')
sea_zam = QPushButton('')
tex_zam = QTextEdit()
li_te_txt = QLabel('')
name_te = QLineEdit()
li_te = QListWidget()
add_te = QPushButton('')
del_te = QPushButton('')

ma_smart_lay = QHBoxLayout()
lay_rig1 = QVBoxLayout()
lay_rig2 = QVBoxLayout()
lay_rig3 = QVBoxLayout()
lay_rig4 = QVBoxLayout()
lay_rig5 = QVBoxLayout()
lay_rig6 = QVBoxLayout()
lay_rig7 = QVBoxLayout()
lay_rig8 = QVBoxLayout()
lay_rig9 = QVBoxLayout()
lay_rig10 = QVBoxLayout()
lay_rig11 = QVBoxLayout()
lay_rig12 = QVBoxLayout()

lay_rig1.addWidget(add_zam)
lay_rig2.addWidget(li_zam_txt)
lay_rig3.addWidget(li_zam)
lay_rig4.addWidget(del_zam)
lay_rig5.addWidget(save_zam)
lay_rig6.addWidget(sea_zam)
lay_rig7.addWidget(tex_zam)
lay_rig8.addWidget(li_te_txt)
lay_rig9.addWidget(name_te)
lay_rig10.addWidget(li_te)
lay_rig11.addWidget(add_te)
lay_rig12.addWidget(del_te)

ma_smart_lay.addLayout(lay_rig1)
ma_smart_lay.addLayout(lay_rig2)
ma_smart_lay.addLayout(lay_rig3)
ma_smart_lay.addLayout(lay_rig4)
ma_smart_lay.addLayout(lay_rig5)
ma_smart_lay.addLayout(lay_rig6)
ma_smart_lay.addLayout(lay_rig7)
ma_smart_lay.addLayout(lay_rig8)
ma_smart_lay.addLayout(lay_rig9)
ma_smart_lay.addLayout(lay_rig10)
ma_smart_lay.addLayout(lay_rig11)
ma_smart_lay.addLayout(lay_rig12)

