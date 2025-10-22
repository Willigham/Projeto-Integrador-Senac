# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormTelaEstoqueVJJpRX.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_FormTelaEstoque(object):
    def setupUi(self, FormTelaEstoque):
        if not FormTelaEstoque.objectName():
            FormTelaEstoque.setObjectName(u"FormTelaEstoque")
        FormTelaEstoque.resize(800, 601)
        self.labelEstoque = QLabel(FormTelaEstoque)
        self.labelEstoque.setObjectName(u"labelEstoque")
        self.labelEstoque.setGeometry(QRect(300, 70, 231, 51))
        font = QFont()
        font.setPointSize(26)
        self.labelEstoque.setFont(font)
        self.labelEstoque.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame = QFrame(FormTelaEstoque)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(140, 140, 541, 44))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonBebidas = QPushButton(self.frame)
        self.pushButtonBebidas.setObjectName(u"pushButtonBebidas")

        self.horizontalLayout.addWidget(self.pushButtonBebidas)

        self.pushButtonTiraGostos = QPushButton(self.frame)
        self.pushButtonTiraGostos.setObjectName(u"pushButtonTiraGostos")

        self.horizontalLayout.addWidget(self.pushButtonTiraGostos)

        self.pushButtonVoltarEstoque = QPushButton(FormTelaEstoque)
        self.pushButtonVoltarEstoque.setObjectName(u"pushButtonVoltarEstoque")
        self.pushButtonVoltarEstoque.setGeometry(QRect(130, 90, 75, 24))
        self.stackedWidget = QStackedWidget(FormTelaEstoque)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(140, 200, 551, 351))
        self.pageBebidas = QWidget()
        self.pageBebidas.setObjectName(u"pageBebidas")
        self.horizontalLayout_2 = QHBoxLayout(self.pageBebidas)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidgetBebidas = QTableWidget(self.pageBebidas)
        if (self.tableWidgetBebidas.columnCount() < 3):
            self.tableWidgetBebidas.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetBebidas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetBebidas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetBebidas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidgetBebidas.setObjectName(u"tableWidgetBebidas")

        self.horizontalLayout_2.addWidget(self.tableWidgetBebidas)

        self.stackedWidget.addWidget(self.pageBebidas)
        self.pageTiraGosto = QWidget()
        self.pageTiraGosto.setObjectName(u"pageTiraGosto")
        self.verticalLayout = QVBoxLayout(self.pageTiraGosto)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidgetTiraGostos = QTableWidget(self.pageTiraGosto)
        if (self.tableWidgetTiraGostos.columnCount() < 3):
            self.tableWidgetTiraGostos.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetTiraGostos.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetTiraGostos.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidgetTiraGostos.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidgetTiraGostos.setObjectName(u"tableWidgetTiraGostos")

        self.verticalLayout.addWidget(self.tableWidgetTiraGostos)

        self.stackedWidget.addWidget(self.pageTiraGosto)

        self.retranslateUi(FormTelaEstoque)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FormTelaEstoque)
    # setupUi

    def retranslateUi(self, FormTelaEstoque):
        FormTelaEstoque.setWindowTitle(QCoreApplication.translate("FormTelaEstoque", u"Tela Estoque", None))
        self.labelEstoque.setText(QCoreApplication.translate("FormTelaEstoque", u"Estoque", None))
        self.pushButtonBebidas.setText(QCoreApplication.translate("FormTelaEstoque", u"Bebidas", None))
        self.pushButtonTiraGostos.setText(QCoreApplication.translate("FormTelaEstoque", u"Tira Gosto", None))
        self.pushButtonVoltarEstoque.setText(QCoreApplication.translate("FormTelaEstoque", u"Voltar", None))
        ___qtablewidgetitem = self.tableWidgetBebidas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormTelaEstoque", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidgetBebidas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormTelaEstoque", u"Quantidade", None));
        ___qtablewidgetitem2 = self.tableWidgetBebidas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormTelaEstoque", u"Valor", None));
        ___qtablewidgetitem3 = self.tableWidgetTiraGostos.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormTelaEstoque", u"Nome", None));
        ___qtablewidgetitem4 = self.tableWidgetTiraGostos.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormTelaEstoque", u"Quantidade", None));
        ___qtablewidgetitem5 = self.tableWidgetTiraGostos.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormTelaEstoque", u"Valor", None));
    # retranslateUi

