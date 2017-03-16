#!/usr/bin/env python3
import subprocess

key = ["org.gnome.settings-daemon.plugins.power",
       "lid-close-ac-action", "lid-close-battery-action"]

currstate = subprocess.check_output(["gsettings", "get",
    key[0], key[1]]).decode("utf-8").strip()

if currstate == "'suspend'":
    command = "'nothing'"
    subprocess.Popen(["notify-send", "Lid closes with no action"])
else:
    command = "'suspend'"
    subprocess.Popen(["notify-send", "Suspend will be activated when lid closes"])

for k in [key[1], key[2]]:
    subprocess.Popen(["gsettings", "set", key[0], k, command])
