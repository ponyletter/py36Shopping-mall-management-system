# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customer_ui/buy_goods.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_buy_goods(object):
    def setupUi(self, buy_goods):
        buy_goods.setObjectName("buy_goods")
        buy_goods.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(buy_goods)
        self.centralwidget.setObjectName("centralwidget")
        self.tomain = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.tomain.setGeometry(QtCore.QRect(490, 320, 91, 51))
        self.tomain.setObjectName("tomain")
        self.buy_bt = QtWidgets.QPushButton(self.centralwidget)
        self.buy_bt.setGeometry(QtCore.QRect(310, 410, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buy_bt.setFont(font)
        self.buy_bt.setObjectName("buy_bt")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(190, 50, 391, 245))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.goods_name = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.goods_name.setFont(font)
        self.goods_name.setObjectName("goods_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.goods_name)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.buy_num = QtWidgets.QSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buy_num.setFont(font)
        self.buy_num.setMaximum(9999)
        self.buy_num.setObjectName("buy_num")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.buy_num)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.goods_type = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.goods_type.setFont(font)
        self.goods_type.setObjectName("goods_type")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.goods_type)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.goods_price = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.goods_price.setFont(font)
        self.goods_price.setObjectName("goods_price")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.goods_price)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.goods_rest = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.goods_rest.setFont(font)
        self.goods_rest.setObjectName("goods_rest")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.goods_rest)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.shop_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.shop_name.setFont(font)
        self.shop_name.setObjectName("shop_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.shop_name)
        buy_goods.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(buy_goods)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        buy_goods.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(buy_goods)
        self.statusbar.setObjectName("statusbar")
        buy_goods.setStatusBar(self.statusbar)

        self.retranslateUi(buy_goods)
        QtCore.QMetaObject.connectSlotsByName(buy_goods)

    def retranslateUi(self, buy_goods):
        _translate = QtCore.QCoreApplication.translate
        buy_goods.setWindowTitle(_translate("buy_goods", "购买"))
        self.tomain.setText(_translate("buy_goods", "首页"))
        self.buy_bt.setText(_translate("buy_goods", "购买商品"))
        self.label.setText(_translate("buy_goods", "商品名称"))
        self.label_2.setText(_translate("buy_goods", "购买数量"))
        self.label_7.setText(_translate("buy_goods", "商品类型"))
        self.label_8.setText(_translate("buy_goods", "价格"))
        self.label_9.setText(_translate("buy_goods", "库存"))
        self.label_3.setText(_translate("buy_goods", "店铺名称"))
