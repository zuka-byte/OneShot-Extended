#  OneShot-Extended (WPS penetration testing utility) is a fork of the tool with extra features
#  Copyright (C) 2026 chkndrp
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

import os
import subprocess
import csv

from datetime import datetime
from shutil import which
from src import logger

import src.wifi.android
import src.utils

class WiFiCollector:
    """Allows for collecting result, pin or network."""

    def __init__(self):
        self.ANDROID_NETWORK = src.wifi.android.AndroidNetwork()

    @staticmethod
    def writeResult(bssid: str, essid: str, wps_pin: str, wpa_psk: str):
        """Writes the success result to a stored.{txt,csv} file."""

        reports_dir = src.utils.REPORTS_DIR
        filename = reports_dir + 'stored'

        # Prevent duplicate writes if the BSSID + PSK combo already exists
        if os.path.isfile(filename + '.csv'):
            with open(filename + '.csv', 'r', encoding='utf-8') as file:
                if any(f'"{bssid}"' in line and f'"{wpa_psk}"' in line for line in file):
                    return logger.info(f'[*] Credentials for {essid} ({bssid}) are already saved.')

        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)

        write_table_header = not os.path.isfile(filename + '.csv')
        date_str = datetime.now().strftime('%d.%m.%Y %H:%M')

        with open(filename + '.txt', 'a', encoding='utf-8') as file:
            file.write('{}\nBSSID: {}\nESSID: {}\nWPS PIN: {}\nWPA PSK: {}\n\n'.format(
                date_str, bssid, essid, wps_pin, wpa_psk
            ))

        with open(filename + '.csv', 'a', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file,
                delimiter=';', quoting=csv.QUOTE_ALL
            )

            if write_table_header:
                csv_writer.writerow(['Date', 'BSSID', 'ESSID', 'WPS PIN', 'WPA PSK'])

            csv_writer.writerow([date_str, bssid, essid, wps_pin, wpa_psk])

        logger.info(f'[*] Credentials saved to {filename}.txt, {filename}.csv')

    @staticmethod
    def writePin(bssid: str, pin: str):
        """Writes PIN to a file for later use."""

        pixiewps_dir = src.utils.PIXIEWPS_DIR
        filename = f'''{pixiewps_dir}{bssid.replace(':', '').upper()}.run'''

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(pin)

        logger.info(f'[*] PIN saved in {filename}')
