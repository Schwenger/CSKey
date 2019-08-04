#! /usr/bin/env python3

import os.path
import platform
import sys
import subprocess

def check_exists(name):
  if not os.path.isfile(name):
    print(f"File {name} not found. Did you move it?")
    sys.exit()

layout_with_um = "CSKeyWithUmlauts.keylayout"
layout = "CSKey.keylayout"
target = '/Library/Keyboard\ Layouts/'
cp_layout = f"sudo cp {layout} {target}"
cp_layout_with_um = f"sudo cp {layout_with_um} {target}"

commands = [cp_layout, cp_layout_with_um]

check_exists(layout)
check_exists(layout_with_um)

if platform.system() == "Darwin":   # Check if system is Mac.
  if not os.path.isdir(target.replace('\\', '')):  # Check if target directory is there.
    print("Your Keyboard Layout directory cannot be found. Something is strange with your system...")
    sys.exit()
  if os.geteuid() != 0:
    print(f"We need to copy the layout file to `{target}`. This requires root privileges, so your OS will ask you for your password.")
    print("If you feel uneasy granting root privileges to some dude on the Internet, feel free to copy the file yourself:")
    print(f"Simply run: `{';'.join(commands)}`.")
    print("After copying, you will need to open Apple > System Preferences > Keyboard > Input Sources, click the little \"+\", go to \"others\" and select the CSKey layout with or without Umlauts. Voilà!")
    print("Note: if there is already an open System Preferences window, you need to close and re-open it.")
    for cmd in commands:
      os.system(cmd)
else: 
  print("Sorry, We currently only support Mac. You need to install the layout manually.")


