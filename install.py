#! /usr/bin/env python3

import os.path
import platform
import sys
import subprocess

filename = "CSKeyboardLayout.keylayout"

if not os.path.isfile(filename):
  print(f"File {filename} not found. Did you move it?")
  sys.exit()

if platform.system() == "Darwin":  # check if Mac
  target = '/Library/Keyboard\\ Layouts/'
  command = f"sudo cp {filename} {target}"
  if os.geteuid() != 0:
    print("We need to copy the layout file to `/Library/Keyboard\ Layouts/`. This requires root privileges, so your OS will ask you for your password.")
    print("If you feel uneasy granting root privileges to some dude on the Internet, feel free to copy the file yourself:")
    print(f"Simply run: `sudo cp {filename} {target}`.")
    print("After copying, you will need to open Apple > System Preferences > Keyboard > Input Sources, click the little \"+\", go to \"others\" and select the CSKeyboardLayout. Voilà!")
    print("Note: if there is already an open System Preferences window, you need to close and re-open it.")
    os.system(command)
else: 
  print("Sorry, We currently only support Mac. You need to install the layout manually.")


