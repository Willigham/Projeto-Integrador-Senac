# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormTelaAtendimentoOBxSYI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_FormTelaAtendimento(object):
    def setupUi(self, FormTelaAtendimento):
        if not FormTelaAtendimento.objectName():
            FormTelaAtendimento.setObjectName(u"FormTelaAtendimento")
        FormTelaAtendimento.resize(800, 600)
        self.labelPedidos = QLabel(FormTelaAtendimento)
        self.labelPedidos.setObjectName(u"labelPedidos")
        self.labelPedidos.setGeometry(QRect(130, 85, 171, 31))
        font = QFont()
        font.setPointSize(26)
        self.labelPedidos.setFont(font)
        self.labelPedidos.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame = QFrame(FormTelaAtendimento)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(480, 140, 291, 371))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButtonMesa5 = QPushButton(self.frame)
        self.pushButtonMesa5.setObjectName(u"pushButtonMesa5")

        self.gridLayout.addWidget(self.pushButtonMesa5, 1, 1, 1, 1)

        self.pushButtonMesa6 = QPushButton(self.frame)
        self.pushButtonMesa6.setObjectName(u"pushButtonMesa6")

        self.gridLayout.addWidget(self.pushButtonMesa6, 1, 2, 1, 1)

        self.pushButtonMesa1 = QPushButton(self.frame)
        self.pushButtonMesa1.setObjectName(u"pushButtonMesa1")
        self.pushButtonMesa1.setEnabled(True)

        self.gridLayout.addWidget(self.pushButtonMesa1, 0, 0, 1, 1)

        self.pushButtonMesa7 = QPushButton(self.frame)
        self.pushButtonMesa7.setObjectName(u"pushButtonMesa7")

        self.gridLayout.addWidget(self.pushButtonMesa7, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.pushButtonMesa4 = QPushButton(self.frame)
        self.pushButtonMesa4.setObjectName(u"pushButtonMesa4")

        self.gridLayout.addWidget(self.pushButtonMesa4, 1, 0, 1, 1)

        self.pushButtonMesa3 = QPushButton(self.frame)
        self.pushButtonMesa3.setObjectName(u"pushButtonMesa3")

        self.gridLayout.addWidget(self.pushButtonMesa3, 0, 2, 1, 1)

        self.pushButtonMesa10 = QPushButton(self.frame)
        self.pushButtonMesa10.setObjectName(u"pushButtonMesa10")

        self.gridLayout.addWidget(self.pushButtonMesa10, 3, 0, 1, 1)

        self.pushButtonMesa12 = QPushButton(self.frame)
        self.pushButtonMesa12.setObjectName(u"pushButtonMesa12")

        self.gridLayout.addWidget(self.pushButtonMesa12, 3, 2, 1, 1)

        self.pushButtonMesa8 = QPushButton(self.frame)
        self.pushButtonMesa8.setObjectName(u"pushButtonMesa8")

        self.gridLayout.addWidget(self.pushButtonMesa8, 2, 1, 1, 1)

        self.pushButtonMesa9 = QPushButton(self.frame)
        self.pushButtonMesa9.setObjectName(u"pushButtonMesa9")

        self.gridLayout.addWidget(self.pushButtonMesa9, 2, 2, 1, 1)

        self.pushButtonMesa11 = QPushButton(self.frame)
        self.pushButtonMesa11.setObjectName(u"pushButtonMesa11")

        self.gridLayout.addWidget(self.pushButtonMesa11, 3, 1, 1, 1)

        self.tableWidgetPedidos = QTableWidget(FormTelaAtendimento)
        if (self.tableWidgetPedidos.columnCount() < 4):
            self.tableWidgetPedidos.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetPedidos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetPedidos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetPedidos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetPedidos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidgetPedidos.setObjectName(u"tableWidgetPedidos")
        self.tableWidgetPedidos.setGeometry(QRect(20, 150, 411, 361))
        self.labelMesas = QLabel(FormTelaAtendimento)
        self.labelMesas.setObjectName(u"labelMesas")
        self.labelMesas.setGeometry(QRect(540, 80, 171, 31))
        self.labelMesas.setFont(font)
        self.labelMesas.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButtonVoltarAtendimento = QPushButton(FormTelaAtendimento)
        self.pushButtonVoltarAtendimento.setObjectName(u"pushButtonVoltarAtendimento")
        self.pushButtonVoltarAtendimento.setGeometry(QRect(20, 40, 75, 24))

        self.retranslateUi(FormTelaAtendimento)

        QMetaObject.connectSlotsByName(FormTelaAtendimento)
    # setupUi

    def retranslateUi(self, FormTelaAtendimento):
        FormTelaAtendimento.setWindowTitle(QCoreApplication.translate("FormTelaAtendimento", u"Tela Atendimento", None))
        self.labelPedidos.setText(QCoreApplication.translate("FormTelaAtendimento", u"Pedidos", None))
        self.pushButtonMesa5.setText(QCoreApplication.translate("FormTelaAtendimento", u"5", None))
        self.pushButtonMesa6.setText(QCoreApplication.translate("FormTelaAtendimento", u"6", None))
        self.pushButtonMesa1.setText(QCoreApplication.translate("FormTelaAtendimento", u"1", None))
        self.pushButtonMesa7.setText(QCoreApplication.translate("FormTelaAtendimento", u"7", None))
        self.pushButton.setText(QCoreApplication.translate("FormTelaAtendimento", u"2", None))
        self.pushButtonMesa4.setText(QCoreApplication.translate("FormTelaAtendimento", u"4", None))
        self.pushButtonMesa3.setText(QCoreApplication.translate("FormTelaAtendimento", u"3", None))
        self.pushButtonMesa10.setText(QCoreApplication.translate("FormTelaAtendimento", u"10", None))
        self.pushButtonMesa12.setText(QCoreApplication.translate("FormTelaAtendimento", u"12", None))
        self.pushButtonMesa8.setText(QCoreApplication.translate("FormTelaAtendimento", u"8", None))
        self.pushButtonMesa9.setText(QCoreApplication.translate("FormTelaAtendimento", u"9", None))
        self.pushButtonMesa11.setText(QCoreApplication.translate("FormTelaAtendimento", u"11", None))
        ___qtablewidgetitem = self.tableWidgetPedidos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormTelaAtendimento", u"Mesa", None));
        ___qtablewidgetitem1 = self.tableWidgetPedidos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormTelaAtendimento", u"Pedido", None));
        ___qtablewidgetitem2 = self.tableWidgetPedidos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormTelaAtendimento", u"Quantidade", None));
        ___qtablewidgetitem3 = self.tableWidgetPedidos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormTelaAtendimento", u"Status", None));
        self.labelMesas.setText(QCoreApplication.translate("FormTelaAtendimento", u"Mesas", None))
        self.pushButtonVoltarAtendimento.setText(QCoreApplication.translate("FormTelaAtendimento", u"Voltar", None))
    # retranslateUi

