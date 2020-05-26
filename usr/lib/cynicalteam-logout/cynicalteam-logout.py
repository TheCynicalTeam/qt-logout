#!/usr/bin/python3

import sys
import getpass
import os
import subprocess
import shutil
import Functions as fn
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ShutdownMenu(QDialog):
    # - LOGOUT - SUSPEND - RESTART - SHUTDOWN- HIBERNATE- LOCK
    logout_button = None
    suspend_button = None
    restart_button = None
    shutdown_button = None
    hibernate_button = None
    lock_button = None

    def __init__(self):
        super().__init__()
        if not fn.os.path.isdir(fn.home + "/.config/cynicalteam-logout"):
            fn.os.mkdir(fn.home + "/.config/cynicalteam-logout")

        if not fn.os.path.isfile(fn.home + "/.config/cynicalteam-logout/settings.conf"):
            shutil.copy(fn.root_config, fn.home + "/.config/cynicalteam-logout/settings.conf")

        fn.get_config(self, fn.config)
        self.icon_size = int(self.icon_size)
        self.icon_font_size = str(self.icon_font_size)
        self.title_font_size = str(self.title_font_size)
        self.icon_font_weight = str(self.icon_font_weight)
        self.title_font_weight = str(self.title_font_weight)
        self.opacity = str(self.opacity)
        self.buttons = str(self.buttons)
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        self.setWindowTitle("Shutdown menu")

        self.text = QLabel("Hello, " + getpass.getuser() + "! What would you like to do?")
        self.text.setStyleSheet("QLabel {background-color:transparent;font-size: "+self.title_font_size+"pt;font-weight: "+self.title_font_weight+";border: none;}")

        hbox = QGridLayout()
        hbox.setSpacing(0)

        self.logout_button = QToolButton()
        self.logout_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.logout_button.setIcon(QIcon.fromTheme("system-log-out"))
        self.logout_button.setIconSize(QSize(self.icon_size, self.icon_size))
        self.logout_button.setToolTip("system-log-out")
        self.logout_button.setText("Logout")
        self.logout_button.setStyleSheet("QToolButton {background-color:transparent;font-size: "+self.icon_font_size+"pt;font-weight: "+self.icon_font_weight+";border: none;}")
        self.logout_button.setShortcut("ctrl+e")
        self.logout_button.move(0,0)
        self.logout_button.clicked.connect(self.logout)

        self.suspend_button = QToolButton()
        self.suspend_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.suspend_button.setIcon(QIcon.fromTheme("system-suspend"))
        self.suspend_button.setIconSize(QSize(self.icon_size, self.icon_size))
        self.suspend_button.setToolTip("system-suspend")
        self.suspend_button.setText("Suspend")
        self.suspend_button.setStyleSheet("QToolButton {background-color:transparent;font-size: "+self.icon_font_size+"pt;font-weight: "+self.icon_font_weight+";border: none;}")
        self.suspend_button.setShortcut("ctrl+s")
        self.suspend_button.move(0,0)
        self.suspend_button.clicked.connect(self.suspend)

        self.restart_button = QToolButton()
        self.restart_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.restart_button.setIcon(QIcon.fromTheme("system-reboot"))
        self.restart_button.setIconSize(QSize(self.icon_size, self.icon_size))
        self.restart_button.setToolTip("system-reboot")
        self.restart_button.setText("Restart")
        self.restart_button.setStyleSheet("QToolButton {background-color:transparent;font-size: "+self.icon_font_size+"pt;font-weight: "+self.icon_font_weight+";border: none;}")
        self.restart_button.setShortcut("ctrl+r")
        self.restart_button.move(0,0)
        self.restart_button.clicked.connect(self.restart)

        self.shutdown_button = QToolButton()
        self.shutdown_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.shutdown_button.setIcon(QIcon.fromTheme("system-shutdown"))
        self.shutdown_button.setIconSize(QSize(self.icon_size, self.icon_size))
        self.shutdown_button.setToolTip("system-shutdown")
        self.shutdown_button.setText("Shutdown")
        self.shutdown_button.setStyleSheet("QToolButton {background-color:transparent;font-size: "+self.icon_font_size+"pt;font-weight: "+self.icon_font_weight+";border: none;}")
        self.shutdown_button.setShortcut("ctrl+p")
        self.shutdown_button.move(0,0)
        self.shutdown_button.clicked.connect(self.shutdown)

        self.hibernate_button = QToolButton()
        self.hibernate_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.hibernate_button.setIcon(QIcon.fromTheme("system-suspend-hibernate"))
        self.hibernate_button.setIconSize(QSize(self.icon_size, self.icon_size))
        self.hibernate_button.setToolTip("system-hibernate")
        self.hibernate_button.setText("Hibernate")
        self.hibernate_button.setStyleSheet("QToolButton {background-color:transparent;font-size: "+self.icon_font_size+"pt;font-weight: "+self.icon_font_weight+";border: none;}")
        self.hibernate_button.setShortcut("ctrl+p")
        self.hibernate_button.move(0,0)
        self.hibernate_button.clicked.connect(self.hibernate)

        self.lock_button = QToolButton()
        self.lock_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.lock_button.setIcon(QIcon.fromTheme("system-lock-screen"))
        self.lock_button.setIconSize(QSize(self.icon_size, self.icon_size))
        self.lock_button.setToolTip("system-lock-screen")
        self.lock_button.setText("Lock-Screen")
        self.lock_button.setStyleSheet("QToolButton {background-color:transparent;font-size: "+self.icon_font_size+"pt;font-weight: "+self.icon_font_weight+";border: none;}")
        self.lock_button.setShortcut("ctrl+p")
        self.lock_button.move(0,0)
        self.lock_button.clicked.connect(self.lock)

        vbox.addWidget(self.text)
        if 'logout' in self.buttons:
            hbox.addWidget(self.logout_button,1,0, Qt.AlignTop)
        if 'suspend' in self.buttons:
            hbox.addWidget(self.suspend_button,1,1, Qt.AlignTop)
        if 'restart' in self.buttons:
            hbox.addWidget(self.restart_button,1,2, Qt.AlignTop)
        if 'shutdown' in self.buttons:
            hbox.addWidget(self.shutdown_button,1,3, Qt.AlignTop)
        if 'hibernate' in self.buttons:
            hbox.addWidget(self.hibernate_button,1,4, Qt.AlignTop)
        if 'lock' in self.buttons:
            hbox.addWidget(self.lock_button,1,5, Qt.AlignTop)
        vbox.addLayout(hbox)

        base = QWidget()
        base.setObjectName("base")
        base.setLayout(vbox)

        baseLyt = QVBoxLayout()
        baseLyt.addWidget(base)
        baseLyt.setContentsMargins(QMargins())
        self.setLayout(baseLyt)

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("QWidget {background-color: rgba(0,0,0,"+self.opacity+");}")

    def logout(self):
        self.disable_buttons()
        logout_systemctl()
        self.close()

    def suspend(self):
        self.disable_buttons()
        suspend_systemctl()
        self.close()

    def restart(self):
        self.disable_buttons()
        reboot_systemctl()
        self.close()

    def shutdown(self):
        self.disable_buttons()
        shutdown_systemctl()
        self.close()

    def hibernate(self):
        self.disable_buttons()
        hibernate_systemctl()
        self.close()

    def lock(self):
        self.disable_buttons()
        lock_systemctl(self.cmd_lock)
        self.close()
    def cancel(self):
        self.disable_buttons()
        self.close()

    def disable_buttons(self):
        self.logout_button.setEnabled(False)
        self.suspend_button.setEnabled(False)
        self.restart_button.setEnabled(False)
        self.shutdown_button.setEnabled(False)
        self.hibernate_button.setEnabled(False)
        self.lock_button.setEnabled(False)


def logout_systemctl():
    out = subprocess.run(["sh", "-c", "env | grep DESKTOP_SESSION"],
                         shell=False, stdout=subprocess.PIPE)
    desktop = out.stdout.decode().split("=")[1].strip()

    if desktop in ("herbstluftwm", "/usr/share/xsessions/herbstluftwm"):
        return "herbstclient quit"
    elif desktop in ("bspwm", "/usr/share/xsessions/bspwm"):
        return "pkill bspwm"
    elif desktop in ("jwm", "/usr/share/xsessions/jwm"):
        return "pkill jwm"
    elif desktop in ("openbox", "/usr/share/xsessions/openbox"):
        return "pkill openbox"
    elif desktop in ("awesome", "/usr/share/xsessions/awesome"):
        return "pkill awesome"
    elif desktop in ("qtile", "/usr/share/xsessions/qtile"):
        return "pkill qtile"
    elif desktop in ("xmonad", "/usr/share/xsessions/xmonad"):
        return "pkill xmonad"
    elif desktop in ("dwm", "/usr/share/xsessions/dwm"):
        return "pkill dwm"
    elif desktop in ("i3", "/usr/share/xsessions/i3"):
        return "pkill i3"
    elif desktop in ("lxqt", "/usr/share/xsessions/lxqt"):
        return "pkill lxqt"
    elif desktop in ("spectrwm", "/usr/share/xsessions/spectrwm"):
        return "pkill spectrwm"
    elif desktop in ("xfce", "/usr/share/xsessions/xfce"):
        return "pkill xfce"
    elif desktop in ("sway", "/usr/share/xsessions/sway"):
        return "pkill sway"

    return None


def suspend_systemctl():
    os.system("systemctl suspend")

def reboot_systemctl():
    os.system("systemctl reboot")

def shutdown_systemctl():
    os.system("systemctl poweroff")

def hibernate_systemctl():
    os.system("systemctl hibernate")

def lock_systemctl(command):
    os.system(command)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        app = QApplication(sys.argv)
        Gui = ShutdownMenu()
        Gui.showFullScreen()
        sys.exit(app.exec_())
    else:
        if sys.argv[1] == "logout":
            logout_systemctl()
        elif sys.argv[1] == "suspend":
            suspend_systemctl()
        elif sys.argv[1] == "reboot":
            reboot_systemctl()
        elif sys.argv[1] == "shutdown":
            shutdown_systemctl()
        elif sys.argv[1] == "hibernate":
            hibernate_systemctl()
        elif sys.argv[1] == "lock":
            lock_systemctl('betterlockscreen -l dimblur -- --timestr="%H:%M"')
