# Website-Blocker-Using-Python-and-Datetime

This Python script blocks access to specific websites during a scheduled time period.
It uses the built-in datetime module to check the current time and modify the system’s hosts file to block or unblock the specified websites automatically.

Features:

    Block access to distracting websites during work hours.

    Automatically unblock websites outside the blocked time range.

    Lightweight and easy to customize.

    No third-party libraries required — uses only built-in Python modules.

How It Works:

    The script continuously monitors the current time.

    If the time falls within the defined "working hours," it redirects the specified websites to 127.0.0.1 (localhost) by modifying the system’s hosts file.

    Outside working hours, it removes the blocking entries from the hosts file to restore access.

Requirements:

    Python 3.x

    Admin/root access to modify the hosts file
