# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RESTool/ui/design.ui'
#
# Created: Mon Oct 27 15:14:18 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(444, 456)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.layout_features = QtGui.QVBoxLayout()
        self.layout_features.setObjectName(_fromUtf8("layout_features"))
        self.layout_info = QtGui.QFormLayout()
        self.layout_info.setObjectName(_fromUtf8("layout_info"))
        self.label_os_info = QtGui.QLabel(self.centralwidget)
        self.label_os_info.setObjectName(_fromUtf8("label_os_info"))
        self.layout_info.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_os_info)
        self.label_chrome_file = QtGui.QLabel(self.centralwidget)
        self.label_chrome_file.setObjectName(_fromUtf8("label_chrome_file"))
        self.layout_info.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_chrome_file)
        self.label_firefox_file = QtGui.QLabel(self.centralwidget)
        self.label_firefox_file.setObjectName(_fromUtf8("label_firefox_file"))
        self.layout_info.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_firefox_file)
        self.lbl_os = QtGui.QLabel(self.centralwidget)
        self.lbl_os.setObjectName(_fromUtf8("lbl_os"))
        self.layout_info.setWidget(0, QtGui.QFormLayout.FieldRole, self.lbl_os)
        self.lbl_chrome = QtGui.QLabel(self.centralwidget)
        self.lbl_chrome.setObjectName(_fromUtf8("lbl_chrome"))
        self.layout_info.setWidget(1, QtGui.QFormLayout.FieldRole, self.lbl_chrome)
        self.lbl_firefox = QtGui.QLabel(self.centralwidget)
        self.lbl_firefox.setObjectName(_fromUtf8("lbl_firefox"))
        self.layout_info.setWidget(2, QtGui.QFormLayout.FieldRole, self.lbl_firefox)
        self.label_firefox_profile = QtGui.QLabel(self.centralwidget)
        self.label_firefox_profile.setObjectName(_fromUtf8("label_firefox_profile"))
        self.layout_info.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_firefox_profile)
        self.cbo_ff_profile = QtGui.QComboBox(self.centralwidget)
        self.cbo_ff_profile.setObjectName(_fromUtf8("cbo_ff_profile"))
        self.layout_info.setWidget(3, QtGui.QFormLayout.FieldRole, self.cbo_ff_profile)
        self.layout_features.addLayout(self.layout_info)
        self.h_line_1 = QtGui.QFrame(self.centralwidget)
        self.h_line_1.setFrameShape(QtGui.QFrame.HLine)
        self.h_line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.h_line_1.setObjectName(_fromUtf8("h_line_1"))
        self.layout_features.addWidget(self.h_line_1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.layout_features.addItem(spacerItem)
        self.label_migrate = QtGui.QLabel(self.centralwidget)
        self.label_migrate.setObjectName(_fromUtf8("label_migrate"))
        self.layout_features.addWidget(self.label_migrate)
        self.btn_ch_to_ff = QtGui.QPushButton(self.centralwidget)
        self.btn_ch_to_ff.setObjectName(_fromUtf8("btn_ch_to_ff"))
        self.layout_features.addWidget(self.btn_ch_to_ff)
        self.btn_ff_to_ch = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ff_to_ch.sizePolicy().hasHeightForWidth())
        self.btn_ff_to_ch.setSizePolicy(sizePolicy)
        self.btn_ff_to_ch.setObjectName(_fromUtf8("btn_ff_to_ch"))
        self.layout_features.addWidget(self.btn_ff_to_ch)
        self.h_line_2 = QtGui.QFrame(self.centralwidget)
        self.h_line_2.setFrameShape(QtGui.QFrame.HLine)
        self.h_line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.h_line_2.setObjectName(_fromUtf8("h_line_2"))
        self.layout_features.addWidget(self.h_line_2)
        self.label_backup = QtGui.QLabel(self.centralwidget)
        self.label_backup.setObjectName(_fromUtf8("label_backup"))
        self.layout_features.addWidget(self.label_backup)
        self.btn_backup_ch = QtGui.QPushButton(self.centralwidget)
        self.btn_backup_ch.setObjectName(_fromUtf8("btn_backup_ch"))
        self.layout_features.addWidget(self.btn_backup_ch)
        self.btn_backup_ff = QtGui.QPushButton(self.centralwidget)
        self.btn_backup_ff.setObjectName(_fromUtf8("btn_backup_ff"))
        self.layout_features.addWidget(self.btn_backup_ff)
        self.btn_restore_ch = QtGui.QPushButton(self.centralwidget)
        self.btn_restore_ch.setObjectName(_fromUtf8("btn_restore_ch"))
        self.layout_features.addWidget(self.btn_restore_ch)
        self.btn_restore_ff = QtGui.QPushButton(self.centralwidget)
        self.btn_restore_ff.setObjectName(_fromUtf8("btn_restore_ff"))
        self.layout_features.addWidget(self.btn_restore_ff)
        self.h_line_3 = QtGui.QFrame(self.centralwidget)
        self.h_line_3.setFrameShape(QtGui.QFrame.HLine)
        self.h_line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.h_line_3.setObjectName(_fromUtf8("h_line_3"))
        self.layout_features.addWidget(self.h_line_3)
        self.layout_donations = QtGui.QHBoxLayout()
        self.layout_donations.setObjectName(_fromUtf8("layout_donations"))
        self.btn_paypal_pay = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_paypal_pay.setFont(font)
        self.btn_paypal_pay.setAutoRepeat(False)
        self.btn_paypal_pay.setObjectName(_fromUtf8("btn_paypal_pay"))
        self.layout_donations.addWidget(self.btn_paypal_pay)
        self.cb_paypal_option = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_paypal_option.sizePolicy().hasHeightForWidth())
        self.cb_paypal_option.setSizePolicy(sizePolicy)
        self.cb_paypal_option.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.cb_paypal_option.setFrame(False)
        self.cb_paypal_option.setObjectName(_fromUtf8("cb_paypal_option"))
        self.cb_paypal_option.addItem(_fromUtf8(""))
        self.cb_paypal_option.addItem(_fromUtf8(""))
        self.cb_paypal_option.addItem(_fromUtf8(""))
        self.layout_donations.addWidget(self.cb_paypal_option)
        self.layout_features.addLayout(self.layout_donations)
        self.btn_donate_res = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_donate_res.setFont(font)
        self.btn_donate_res.setObjectName(_fromUtf8("btn_donate_res"))
        self.layout_features.addWidget(self.btn_donate_res)
        self.horizontalLayout.addLayout(self.layout_features)
        self.v_line_1 = QtGui.QFrame(self.centralwidget)
        self.v_line_1.setFrameShape(QtGui.QFrame.VLine)
        self.v_line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.v_line_1.setObjectName(_fromUtf8("v_line_1"))
        self.horizontalLayout.addWidget(self.v_line_1)
        self.layout_backup_files = QtGui.QVBoxLayout()
        self.layout_backup_files.setObjectName(_fromUtf8("layout_backup_files"))
        self.label_backups_list = QtGui.QLabel(self.centralwidget)
        self.label_backups_list.setObjectName(_fromUtf8("label_backups_list"))
        self.layout_backup_files.addWidget(self.label_backups_list)
        self.list_backups = QtGui.QListWidget(self.centralwidget)
        self.list_backups.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.list_backups.setObjectName(_fromUtf8("list_backups"))
        self.layout_backup_files.addWidget(self.list_backups)
        self.btn_del_backup = QtGui.QPushButton(self.centralwidget)
        self.btn_del_backup.setObjectName(_fromUtf8("btn_del_backup"))
        self.layout_backup_files.addWidget(self.btn_del_backup)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.layout_backup_files.addWidget(self.line)
        self.layout_website = QtGui.QHBoxLayout()
        self.layout_website.setObjectName(_fromUtf8("layout_website"))
        self.label_website = QtGui.QLabel(self.centralwidget)
        self.label_website.setObjectName(_fromUtf8("label_website"))
        self.layout_website.addWidget(self.label_website)
        self.lbl_version = QtGui.QLabel(self.centralwidget)
        self.lbl_version.setFrameShape(QtGui.QFrame.NoFrame)
        self.lbl_version.setLineWidth(1)
        self.lbl_version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_version.setMargin(4)
        self.lbl_version.setObjectName(_fromUtf8("lbl_version"))
        self.layout_website.addWidget(self.lbl_version)
        self.layout_backup_files.addLayout(self.layout_website)
        self.horizontalLayout.addLayout(self.layout_backup_files)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cbo_ff_profile.setCurrentIndex(-1)
        self.cb_paypal_option.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "RES Tool", None))
        self.label_os_info.setText(_translate("MainWindow", "Operating System:", None))
        self.label_chrome_file.setText(_translate("MainWindow", "Chrome RES found:", None))
        self.label_firefox_file.setText(_translate("MainWindow", "Firefox RES found:", None))
        self.lbl_os.setToolTip(_translate("MainWindow", "Shows OS info", None))
        self.lbl_os.setText(_translate("MainWindow", "Not detected", None))
        self.lbl_chrome.setToolTip(_translate("MainWindow", "Indicates whether the app was able to find the RES settings file in the default locations on your operating system for this browser.", None))
        self.lbl_chrome.setText(_translate("MainWindow", "Not found!", None))
        self.lbl_firefox.setToolTip(_translate("MainWindow", "Indicates whether the app was able to find the RES settings file in the default locations on your operating system for this browser.", None))
        self.lbl_firefox.setText(_translate("MainWindow", "Not found!", None))
        self.label_firefox_profile.setToolTip(_translate("MainWindow", "User profile to use for applying changes, if more than one exists. If you don\'t use multiple profiles then the default/only one will be used.", None))
        self.label_firefox_profile.setText(_translate("MainWindow", "Firefox profile:", None))
        self.cbo_ff_profile.setToolTip(_translate("MainWindow", "User profile to use for applying changes, if more than one exists. If you don\'t use multiple profiles then the default/only one will be used.", None))
        self.label_migrate.setText(_translate("MainWindow", "Migrating existing data:", None))
        self.btn_ch_to_ff.setToolTip(_translate("MainWindow", "<html><head/><body><p>Migrate settings from RES file on chrome to RES file on firefox, this overwrites the existing firefox file.</p></body></html>", None))
        self.btn_ch_to_ff.setText(_translate("MainWindow", "Chrome to Firefox", None))
        self.btn_ff_to_ch.setToolTip(_translate("MainWindow", "<html><head/><body><p>Migrate settings from RES file on firefox to RES file on chrome, this overwrites the existing chrome file.</p></body></html>", None))
        self.btn_ff_to_ch.setText(_translate("MainWindow", "Firefox to Chrome", None))
        self.label_backup.setText(_translate("MainWindow", "Data backups:", None))
        self.btn_backup_ch.setToolTip(_translate("MainWindow", "<html><head/><body><p>Copy/Backup existing RES settings file from chrome to ./backups folder located in the same location as this application.</p></body></html>", None))
        self.btn_backup_ch.setText(_translate("MainWindow", "Backup Chrome", None))
        self.btn_backup_ff.setToolTip(_translate("MainWindow", "<html><head/><body><p>Copy/Backup existing RES settings file from firefox to ./backups folder located in the same location as this application.</p></body></html>", None))
        self.btn_backup_ff.setText(_translate("MainWindow", "Backup Firefox", None))
        self.btn_restore_ch.setToolTip(_translate("MainWindow", "<html><head/><body><p>Use data from selected backup file and write the settings to RES file on Chrome.</p></body></html>", None))
        self.btn_restore_ch.setText(_translate("MainWindow", "Restore selected backup to Chrome", None))
        self.btn_restore_ff.setToolTip(_translate("MainWindow", "<html><head/><body><p>Use data from selected backup file and write the settings to RES file on Firefox.</p></body></html>", None))
        self.btn_restore_ff.setText(_translate("MainWindow", "Restore selected backup to Firefox", None))
        self.btn_paypal_pay.setToolTip(_translate("MainWindow", "<html><head/><body><p>Checkout using paypal to support further application development</p></body></html>", None))
        self.btn_paypal_pay.setText(_translate("MainWindow", "Pay for RESTool", None))
        self.cb_paypal_option.setToolTip(_translate("MainWindow", "<html><head/><body><p>Amount you wish to pay for this software.</p></body></html>", None))
        self.cb_paypal_option.setItemText(0, _translate("MainWindow", "$1.99", None))
        self.cb_paypal_option.setItemText(1, _translate("MainWindow", "$4.99", None))
        self.cb_paypal_option.setItemText(2, _translate("MainWindow", "$9.99", None))
        self.btn_donate_res.setToolTip(_translate("MainWindow", "<html><head/><body><p>Opens a website with info on how you can donate to RES itself.</p></body></html>", None))
        self.btn_donate_res.setText(_translate("MainWindow", "Donate to RES", None))
        self.label_backups_list.setText(_translate("MainWindow", "RES Settings Backups:", None))
        self.list_backups.setToolTip(_translate("MainWindow", "List will all backupfiles available to use in this application.", None))
        self.btn_del_backup.setToolTip(_translate("MainWindow", "<html><head/><body><p>Permanently remove/delete the selected file from backups folder.</p></body></html>", None))
        self.btn_del_backup.setText(_translate("MainWindow", "Delete selected backup file", None))
        self.label_website.setToolTip(_translate("MainWindow", "Open github.com/nikola-k/RESTool in your default browser", None))
        self.label_website.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://github.com/nikola-k/RESTool\"><span style=\" text-decoration: underline; color:#0000ff;\">Visit github page</span></a></p></body></html>", None))
        self.lbl_version.setText(_translate("MainWindow", "v0.1.0", None))

