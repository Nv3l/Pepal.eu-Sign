# ========== PROJECT INFORMATION ==========
# Title: Pepal.eu Auto Signature
# Publish Date: 23/05/2023
# Author: Chicoch
# Discord : Chicoch#7678
# Website: https://www.pepal.eu/
# Version: 2.0
# Tested on: Python 3.8.5
# Disclaimer: This script is for educational purposes only.

# ========== SETUP ==========
# pip install requests
# pip install re
# Replace the username and password variable with your own
# like this: username = "etu.callard" and password = "CPasClaire1234"


# ========== USAGE ==========
# python pepalSign.py
# To automate this, you can use the Windows Task Scheduler
# or the Linux CronTab
# You can also compile this script into an executable with pyinstaller like so:
# pip install -U pyinstaller
# pyinstaller --onefile pepalSign.py
# Then you can run the executable file in the dist folder
# It would generate a pepalSign.exe file that you can run


from requests import Session
from re import split, findall

# account credentials
username = "etu.callard"
password = "CPasClaire1234"

with Session() as s:
    # Setup the cookie for the session
    pepal_cookie = s.get("https://www.pepal.eu").cookies["sdv"]

    # Login to https://www.pepal.eu
    s.post("https://www.pepal.eu/include/php/ident.php", data={"login": username, "pass": password}, cookies={"sdv": pepal_cookie})

    # Get all the classroom code possible
    links = [split("/", link)[3] for link in findall("/presences/s/.......", s.get("https://www.pepal.eu/presences").text)]

    # Try to sign for all the classroom code
    for link in links:
        s.post("https://www.pepal.eu/student/upload.php", data={"act": "set_present", "seance_pk": link}, cookies={"sdv": pepal_cookie})