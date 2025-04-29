import subprocess


def open_application(app_name):
    # Dictionary of common applications and their respective launch commands
    applications = {
        "calculator": "calc",  # Opens Calculator
        "notepad": "notepad",  # Opens Notepad
        "paint": "mspaint",  # Opens Paint
        "wordpad": "write",  # Opens Wordpad
        "cmd": "cmd",  # Opens Command Prompt
        "control panel": "control",  # Opens Control Panel
        "task manager": "taskmgr",  # Opens Task Manager
        "explorer": "explorer",  # Opens File Explorer
        "registry editor": "regedit",  # Opens Registry Editor
        "snipping tool": "snippingtool",  # Opens Snipping Tool
        "powershell": "powershell",  # Opens PowerShell
        "terminal": "wt",  # Opens Windows Terminal
        "settings": "start ms-settings:",  # Opens Windows Settings
        "browser": "start chrome",  # Opens Google Chrome
        "edge": "start msedge",  # Opens Microsoft Edge
        "internet explorer": "iexplore",  # Opens Internet Explorer
        "media player": "wmplayer",  # Opens Windows Media Player
        "word": "start winword",  # Opens Microsoft Word
        "excel": "start excel",  # Opens Microsoft Excel
        "steam": "start steam",  # Opens Steam
        "xbox": "start xbox",  # Opens Xbox App
        "spotify": "start spotify",  # Opens Spotify
        "discord": "start discord",  # Opens Discord
        "slack": "start slack",  # Opens Slack
    }

    # Normalize app name to lowercase
    app_name = app_name.lower()

    if app_name in applications:
        app_command = applications[app_name]

        if app_command.startswith("start") or "ms-settings" in app_command:
            # Use shell=True for "start" or ms-settings commands
            subprocess.Popen(app_command, shell=True)
        else:
            subprocess.Popen(app_command)

        print(f"{app_name.capitalize()} opened!")
    else:
        print(f"Application '{app_name}' not recognized!")

# Example usage:
# open_application("calculator")
# open_application("paint")
# open_application("word")
# open_application("settings")
