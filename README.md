## Description
This program uses the conservation_mode of Lonovo Ideapad / Yoga notebook to activate or disable
battery charging in order to keep battery level below a customizable threshold.

Battery indicator will still indicate battery is charging, but it will not really charge.

## Installation
If necessary, install psutil: ```sudo pip install psutil```

Copy script where you like, for example in ```/usr/local/bin``` and set it as executable: ```chmod +x /usr/local/bin/yoga-autocharge.py```

Test program as **root** to ensure it can access battery value. There should be no error.

Add program to crontab to run every minute: run ```crontab -e``` and add this line:
```* * * * * /usr/local/bin/yoga-autocharge.py```

Current status can be checked with: ```cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode```


## Configuration
Change these settings to your liking
```
START_CHARGE_THRESH = 65
STOP_CHARGE_THRESH = 70
FORCE_FULL_BATTERY = False # Set to True if you want to temporary charge your battery to full capacity. Set back to False when done.
```
