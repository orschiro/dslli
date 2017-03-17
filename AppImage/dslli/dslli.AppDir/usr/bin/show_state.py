#!/usr/bin/env python3
import subprocess
import os
import time
import signal
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3, GObject
from threading import Thread

key = ["org.gnome.settings-daemon.plugins.power",
       "lid-close-ac-action", "lid-close-battery-action"]

currpath = os.path.dirname(os.path.realpath(__file__))

def runs():
    # The test True/False
    return subprocess.check_output([
        "gsettings", "get", key[0], key[1]
        ]).decode("utf-8").strip() == "'suspend'"

class Indicator():
    def __init__(self):
        self.app = 'show_proc'
        iconpath = currpath+"/nocolor.png"
        self.indicator = AppIndicator3.Indicator.new(
            self.app, iconpath,
            AppIndicator3.IndicatorCategory.OTHER)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())
        self.update = Thread(target=self.check_runs)
        # daemonize the thread to make the indicator stopable
        self.update.setDaemon(True)
        self.update.start()

    def check_runs(self):
        # the function (thread), checking for the process to run
        runs1 = None
        while True:
            time.sleep(1)
            runs2 = runs()
            # if there is a change in state, update the icon
            if runs1 != runs2:
                if runs2:
                    # set the icon to show
                    GObject.idle_add(
                        self.indicator.set_icon,
                        currpath+"/nocolor.png",
                        priority=GObject.PRIORITY_DEFAULT
                        )
                else:
                    # set the icon to hide
                    GObject.idle_add(
                        self.indicator.set_icon,
                        currpath+"/green.png",
                        priority=GObject.PRIORITY_DEFAULT
                        )
            runs1 = runs2

    def create_menu(self):
        menu = Gtk.Menu()
        # quit
        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect('activate', self.stop)
        menu.append(item_quit)
        menu.show_all()
        return menu

    def stop(self, source):
        Gtk.main_quit()

Indicator()
GObject.threads_init()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
