#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Idéalement : ce programme est appelé une fois toutes les dix minutes, affichant un popup pour l'utilisateur
import platform
import os
import sys

title = "WalkReminder"
message = "Pensez à détacher les yeux de l'écran et de regarder au loin quelque temps ;)"

if platform.system() == "Linux":
    command = f'notify-send "{title}" "{message}"'
elif platform.system() == "Darwin":
    command = f"osascript -e 'display notification \"{message}\" with title \"{title}\"'"
else:  # fuck windows
    sys.exit()

os.system(command)
