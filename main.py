# Drink Water Notification App :>>>>>   

import time
from plyer import notification 


if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Its Water Time! Lets have a glass",
            message = '''Our Body Needs 6 Liters of water everyday #keepithidrated!!''',
            app_icon = "F:\Python\Harry Brother\CWH Python Practice Question\Q4-Drink Water Reminder Notification\icon.ico.ico",
            timeout = 10
        
        )
        time.sleep(6)
        
        