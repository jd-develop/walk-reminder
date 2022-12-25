#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Idéalement : ce programme est appelé une fois toutes les dix minutes, affichant un popup pour l'utilisateur
import platform
import os
import sys


def notify(msg: str = "eyes from screen"):
    title = "WalkReminder"
    if msg == "eyes from screen":
        message = "Pensez à détacher les yeux de l'écran et à regarder au loin quelque temps ;)"
    else:
        message = "Pensez à vous dégourdir les jambes, dans votre bureau voire dehors ;)"

    if platform.system() == "Linux":
        command = f'notify-send "{title}" "{message}"'
    elif platform.system() == "Darwin":
        command = f"osascript -e 'display notification \"{message}\" with title \"{title}\"'"
    else:  # fuck windows
        sys.exit()

    os.system(command)
