import time
from plyer import notification

while True:
    print("please drink a sip of water")
    notification.notify(title="Drink Water Reminder",message="It's time to drink water!")
    time.sleep(60*60)