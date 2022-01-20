#!/usr/bin/env python3
import psutil
import os.path

# Source: https://github.com/NOP4/Lenovo-Yoga-Ideapad-Autocharge.git

#####################################
# WARNING                           #
# THIS PROGRAM NEEDS TO RUN AS ROOT #
#####################################
# This program uses the conservation_mode of Lonovo Ideapad / Yoga notebook to activate or disable
# battery charging in order to keep battery level below a customizable threshold.
# Battery indicator will still indicate battery is charging, but it will not really charge.

# INSTALLATION
# If necessary, install psutil: sudo pip install psutil
# Copy script where you like, for example /usr/local/bin and set it as executable: chmod +x /usr/local/bin/yoga-autocharge.py
# Test program as root to ensure it can access battery value. There should be no error.
# Add program to crontab to run every minute: run "crontab -e" and add this line (removing the starting #):
# * * * * * /usr/local/bin/yoga-autocharge.py
# Current status can be checked with: cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode


# CONFIGURATION
# Change these settings to your liking
START_CHARGE_THRESH = 65
STOP_CHARGE_THRESH = 70
FORCE_FULL_BATTERY = False # Set to True if you want to temporary charge your battery to full capacity. Set back to False when done.
#FORCE_FULL_BATTERY = True

# DO NOT CHANGE PAST THIS POINT
conservation_mode_file = '/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode'
battery = psutil.sensors_battery()

#print("Current charge: " + str(int(battery.percent)) + "%")
print("Checking battery charge and activate of stop conservation mode if required.")

if ((battery.percent <= START_CHARGE_THRESH) or FORCE_FULL_BATTERY):
    # We need to stop conservation mode
    if (os.path.isfile(conservation_mode_file)):
        f = open(conservation_mode_file, 'r')
        current_content = f.read()
        f.close()
        if (current_content[0] == "1"):
            print("Conservation mode OFF.")
            f = open(conservation_mode_file, 'w')
            f.write('0')
            f.close()

elif (battery.percent >= STOP_CHARGE_THRESH):
    # We need to stop conservation mode
    if (os.path.isfile(conservation_mode_file)):
        f = open(conservation_mode_file, 'r')
        current_content = f.read()
        f.close()
        if (current_content[0] == "0"):
            print("Conservation mode ON.")
            f = open(conservation_mode_file, 'w')
            f.write('1')
            f.close()
